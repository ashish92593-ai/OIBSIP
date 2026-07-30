#VOICE ASSISTANT

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Setup text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is not working right now.")
        return ""

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        topic = command.replace("search", "").strip()
        if topic:
            speak(f"Searching for {topic}")
            webbrowser.open(f"https://www.google.com/search?q={topic}")
        else:
            speak("What would you like me to search for?")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I don't understand that command yet.")

    return True

# Main program
speak("Voice assistant is ready. Say 'hello' to start.")
running = True
while running:
    command = listen()
    if command:
        running = handle_command(command)
