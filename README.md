# AI Assistant

## Project Overview

The **AI Assistant** is a proof-of-concept web application that leverages a Large Language Model (LLM) to generate creative text ideas based on user prompts. This project demonstrates key skills in Generative AI, LLM integration, and essential MLOps practices for deploying AI models.

**Purpose:** To provide a simple API endpoint for creative brainstorming, showcasing the power of generative AI in a practical application.

## Skills Demonstrated

This project effectively showcases the following skills:

* **Generative AI:** Core functionality relies on text generation using advanced AI models.
* **Large Language Models (LLMs):** Direct application and integration of a pre-trained LLM (`gpt2` by Hugging Face).
* **Python:** Backend API development using Flask.
* **MLOps:**
    * **Containerization (Docker):** Packaging the AI application and its dependencies into a portable Docker image.
    * **Orchestration (Kubernetes):** Defining scalable deployment strategies using Kubernetes YAML configurations.
    * **API Development:** Creating a clean RESTful API endpoint to expose the AI service.
    * **Version Control (Git/GitHub):** Structured project repository for collaborative development and code management.

## Technologies Used

* **Python 3.9+**
* **Flask:** Web framework for the API.
* **Hugging Face Transformers:** For LLM integration (`gpt2` model).
* **PyTorch:** Deep learning framework (dependency of Transformers).
* **Docker:** For building and running containers.
* **Kubernetes:** For orchestrating deployment (via `deployment.yaml`).

## Setup and Running Instructions

Follow these steps to set up and run the IdeaForge AI Assistant locally.

### Prerequisites

* Python 3.9+ installed
* Docker Desktop (includes Docker Engine and Kubernetes for local development) installed and running.

### 1. Clone the Repository

```bash
git clone [https://github.com/YourGitHubUsername/AI-Assistant.git]
cd AI-Assistant