# test_api.py
import requests
import json

API_URL = "http://localhost:5000/generate_idea"
HEADERS = {"Content-Type": "application/json"}

def get_ai_idea(prompt_text, max_tokens=100):
    payload = {"prompt": prompt_text, "max_tokens": max_tokens}
    print(f"Sending request for prompt: '{prompt_text}'...")
    try:
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()
        response_data = response.json()
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the API or receiving response: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None

if __name__ == "__main__":
    print("--- IdeaForge AI Assistant API Tester ---")
    prompts = [
        "Write a short story idea about a cat that can talk.",
        "Generate a catchy slogan for an eco-friendly laundry detergent.",
        "Write the first few lines of a poem about a lonely star."
    ]
    for i, p in enumerate(prompts):
        idea = get_ai_idea(p, max_tokens=80) # Using 80 tokens for consistency
        if idea:
            print(f"\n--- Generated Idea {i+1} ---")
            print(f"Prompt: {idea.get('prompt')}")
            print(f"Idea: {idea.get('generated_idea')}")
            print("------------------------")
    print("\nAPI testing complete.")