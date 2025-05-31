# app/main.py
from flask import Flask, request, jsonify
from transformers import pipeline
import logging
import os
import torch 

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# --- LLM Setup ---
LLM_MODEL = os.getenv("LLM_MODEL", "gpt2") 


if torch.backends.mps.is_available():
    device = "mps" # Apple Silicon's Metal Performance Shaders
    logging.info("Using MPS (Apple Silicon GPU acceleration).")
elif torch.cuda.is_available():
    device = "cuda" # NVIDIA GPU
    logging.info("Using CUDA (NVIDIA GPU acceleration).")
else:
    device = "cpu" # Fallback to CPU
    logging.info("Using CPU (may be slow, but compatible).")

print(f"Loading LLM model '{LLM_MODEL}' on device '{device}'...")
try:
    generator = pipeline("text-generation", model=LLM_MODEL, device=device)
    logging.info(f"LLM model '{LLM_MODEL}' loaded successfully on {device}.")
except Exception as e:
    logging.error(f"Failed to load LLM model {LLM_MODEL}: {e}")
    generator = None

@app.route('/generate_idea', methods=['POST'])
def generate_idea():
    if generator is None:
        return jsonify({"error": "AI model not loaded or failed to initialize."}), 500

    data = request.get_json()
    user_prompt = data.get('prompt')
    max_tokens = data.get('max_tokens', 100) # Default to 100 tokens

    if not user_prompt:
        return jsonify({"error": "Prompt is required."}), 400

    logging.info(f"Received prompt: '{user_prompt}', max_tokens: {max_tokens}")

    try:
        # Explicitly set max_new_tokens to avoid warnings and ensure desired length
        generated_text = generator(
            user_prompt,
            max_new_tokens=max_tokens,
            num_return_sequences=1,
            do_sample=True,      # Enable sampling (randomness)
            temperature=0.7,     # Controls creativity (higher = more creative, lower = more focused)
            top_k=50,            # Considers only top 50 most probable next tokens
            top_p=0.95,           # Considers a cumulative probability of 95% for top tokens
            repetition_penalty=1.2 
        )[0]['generated_text']

        logging.info(f"Generated text for prompt '{user_prompt[:30]}...': {generated_text[:50]}...")

        return jsonify({"prompt": user_prompt, "generated_idea": generated_text})

    except Exception as e:
        logging.error(f"Error during text generation: {e}", exc_info=True) # exc_info to get full traceback
        return jsonify({"error": "Failed to generate idea.", "details": str(e)}), 500

@app.route('/')
def home():
    return "IdeaForge AI Assistant is running! Send a POST request to /generate_idea."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)