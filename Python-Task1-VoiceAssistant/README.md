# 🎙️ Voice Assistant

A Python-based voice assistant that listens to spoken commands and responds with useful actions like greetings, time, date, and web search.

## 📸 Screenshots
*(add a screenshot of the program running here)*

## 🛠️ Built With
- Python 3
- `speech_recognition` (voice input)
- `pyttsx3` (text-to-speech)
- `datetime`
- `webbrowser`

## ✅ Features
- Captures voice input using the microphone
- Responds to "hello" with a greeting
- Tells the current time and date on request
- Performs a web search on a user-specified topic
- Graceful error handling — asks the user to repeat if unclear
- Text-to-speech feedback for all responses

## 🚀 How to Run
```bash
pip install SpeechRecognition pyttsx3 PyAudio
python voice_assistant.py
```
Say "hello" to start, then try commands like "what's the time", "what's the date", or "search Python tutorials". Say "exit" or "stop" to quit.

## 📖 What I Learned
- Working with real-time audio input using `speech_recognition`
- Converting text to speech with `pyttsx3`
- Handling recognition errors gracefully (unclear audio, service errors)
- Structuring command-handling logic with conditional checks

## 👤 Author
Anant Kumar Agarwal — B.Tech CSE, RIT

## 📄 License
This project is licensed under the MIT License.
