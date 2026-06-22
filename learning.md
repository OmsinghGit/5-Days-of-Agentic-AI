# Day 3 Learning Notes – AI Study Assistant

## What I Built

* Built a modular AI Study Assistant using Python.
* Integrated NVIDIA Nemotron API through the OpenAI SDK.
* Created separate files for configuration, AI service logic, and application entry point.
* Used environment variables for secure API key management.

---

## Project Structure

Day-3/

├── main.py

├── ai_service.py

├── config.py

└── .env

### Responsibilities

* `main.py` → Handles user input and output.
* `ai_service.py` → Sends requests to the AI model and receives responses.
* `config.py` → Loads configuration variables.
* `.env` → Stores secret API keys securely.

---

## Challenges Faced

### Issue: API Key Not Loading

While testing the application, the API returned authentication errors.

Error:

* `os.getenv("NVIDIA_API_KEY")` returned `None`
* OpenAI client raised a missing credentials error

### Debugging Process

* Checked hidden files using terminal commands.
* Searched the repository for `.env`.
* Printed the environment variable value.
* Verified whether `.env` was being loaded correctly.

### Solution

* Recreated/verified the `.env` file.
* Confirmed that `load_dotenv()` was loading variables.
* Verified that `os.getenv("NVIDIA_API_KEY")` returned the correct value.

---

## Key Concepts Learned

### Environment Variables

Store sensitive information such as API keys outside the source code.

### load_dotenv()

Loads variables from the `.env` file into the application environment.

### os.getenv()

Reads values stored in environment variables.

### Modular Architecture

Separating responsibilities into different files makes projects easier to maintain and scale.

### Imports & Dependencies

Understanding how files depend on each other:

main.py
↓
ai_service.py
↓
config.py

If a dependency breaks, dependent files will fail as well.

---

## Most Important Lesson

As developers, we do not need to memorize every line of code.

What matters is:

* Understanding the architecture.
* Knowing how components connect.
* Debugging effectively.
* Building reliable solutions.

---

## Next Goal

Day 4: Improve the AI Study Assistant with better prompts, structured learning responses, and enhanced study-focused capabilities.
