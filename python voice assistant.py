#!/usr/bin/env python
# coding: utf-8

# In[3]:


import speech_recognition as sr
import pyttsx3
import webbrowser
import threading
import wikipedia

# Initialize the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-US")
        print("User:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error recognizing your speech.")
        return ""

# Function to perform tasks based on user commands
def perform_task(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "how are you" in command:
        speak("I'm doing well, thank you for asking!")
    elif "what is your name" in command:
        speak("I am a voice assistant created with Python.")
    elif 'are you' in command:
        speak("I am voice assistant ")
    elif 'wikipedia' in command:
        speak("Searching Wikipedia ...")
        command = command.replace("wikipedia", '')
        results = wikipedia.summary(command, sentences=2)
        speak("According to wikipedia")
        speak(results)
    elif 'open youtube' in command:
        speak("opening youtube")
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        speak("opening google")
        webbrowser.open("google.com")
    elif 'open github' in command:
        speak("opening github")
        webbrowser.open("github.com")
    elif 'open stackoverflow' in command:
        speak("opening stackoverflow")
        webbrowser.open("stackoverflow.com")
    elif 'open spotify' in command:
        speak("opening spotify")
        webbrowser.open("spotify.com")
    elif 'play music' in command:
        speak("opening music")
        webbrowser.open("spotify.com")
    elif 'local disk d' in command:
        speak("opening local disk D")
        webbrowser.open("D://")
    elif 'local disk c drive' in command:
        speak("opening local disk C")
        webbrowser.open("C://")
    elif 'local disk e drive' in command:
        speak("opening local disk E")
        webbrowser.open("E://")
    elif 'sleep' or 'exit'in command:
        speak("goodbye!")
        exit_program.set()
    else:
        speak("Sorry, I couldn't understand that command.")

# Main function to run the voice assistant
def main():
    speak("Hello! I'm your voice assistant. How can I assist you?")
    while True:
        command = listen()
        if command:
            perform_task(command)
def main():
    speak("hello,Iam your voice assistant how can I help you?.")
    global exit_program
    exit_program=threading.Event()
    while not exit_program.is_set():
        try:
            command=listen()
            if command:
                perform_task(command)
        except KeyboardInterrupt:
            print("keyboard interrupt detected.Exiting...")
            exit_program.set()
            

if __name__ == "__main__":
    main()
    
    


# In[ ]:




