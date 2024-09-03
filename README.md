# GPT Assistant Using Llama 3 Model

This project is an AI-powered voice assistant that utilizes the Llama 3 model for generating responses. The assistant can perform various tasks such as answering questions, executing web-based actions, and providing vocal feedback.

## Features

- **Speech Recognition**: Converts spoken input into text.
- **Text-to-Speech**: Converts text responses into spoken words.
- **AI-Powered Responses**: Uses the Groq API with the Llama 3 model to generate intelligent answers.
- **Web Browsing**: Opens websites like YouTube and Google based on voice commands.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sukantabhun/GPT-Assistant-using-Llama-3-model.git
Navigate to the project directory:
bash
Copy code
cd GPT-Assistant-using-Llama-3-model
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Configuration
API Key: Replace the api_data placeholder in apikey.py with your actual API key from Groq.
Microphone: Ensure you have a working microphone connected for speech input.
Usage
Run the script:
bash
Copy code
python app.py
The assistant will greet you and start listening for your commands.
Use voice commands to interact with the assistant.
Example Commands
"Open YouTube": Opens the YouTube website.
"Open Google": Opens the Google website.
"Bye": Exits the program.
Dependencies
speech_recognition
pyttsx3
Groq API
