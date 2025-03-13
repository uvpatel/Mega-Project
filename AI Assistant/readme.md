# Alexa-Like Voice Assistant

An AI-powered voice assistant built using Python that can recognize speech, respond to voice commands, and perform various tasks like playing songs on YouTube, fetching Wikipedia summaries, telling jokes, and more.

## Features
- 🎵 **Play Songs**: Say "Play [song name]" to play songs on YouTube.
- 🕒 **Tell Time**: Ask "What time is it?" to get the current time.
- 📖 **Search Wikipedia**: Say "Who is [person's name]" or "Tell me about [topic]" to get a Wikipedia summary.
- 😂 **Tell Jokes**: Say "Tell me a joke" for some fun.
- 💡 **Relationship Status**: Ask "Are you single?" for a witty response.
- 🚪 **Exit Program**: Say "Exit" or "Stop" to close the assistant.

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Install Required Dependencies
Run the following command to install the necessary libraries:
```sh
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes
```

## Usage
Run the script by executing:
```sh
python assistant.py
```
Then, speak commands like:
- "Play Shape of You"
- "What time is it?"
- "Who is Elon Musk?"
- "Tell me a joke"
- "Exit"

## File Structure
```
📂 Alexa-Assistant
│── assistant.py   # Main script
│── README.md      # Project documentation
```

## Troubleshooting
- If speech recognition doesn't work, ensure your microphone is working and permissions are granted.
- If YouTube playback fails, check your internet connection.

## Contributing
Feel free to fork this project, add new features, and create a pull request! 🚀

## License
This project is licensed under the MIT License.
