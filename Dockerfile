# Dockerfile
# Use a Python 3.11 slim image for smaller size and compatibility
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app # Your Flask app will run from this directory

# Copy the requirements file and install dependencies
# Copy requirements.txt directly to the WORKDIR
COPY app/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of your application code
# This copies the *contents* of your local 'app/' directory into the container's '/app' directory
COPY app/. .
# Expose the port your Flask app runs on
EXPOSE 5000

# Set environment variables for the Flask app
ENV FLASK_APP=main.py 
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=5000
ENV LLM_MODEL="gpt2"

# Command to run the Flask application
CMD ["flask", "run"]