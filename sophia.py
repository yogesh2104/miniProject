import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import time
import wikipedia #pip install wikipedia
import webbrowser
import os

assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
# print(voices)
assistant.setProperty('voice', voices[2].id)


def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()

def recognize():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        print("Recognizing...")    
        query = command.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query
# print(sr.Microphone.list_microphone_names()) # also pass device_index=1,2,3,0 etc


    
def startup():
    speak("All systems have been activated")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    strTime = datetime.datetime.now().strftime('%H:%M:%S')
    speak(f"Currently it is {strTime}")
    speak("I am Nova. Online and ready sir. Please tell me how may I help you")


if __name__ == "__main__":
    # startup()
    while True:
        query = recognize().lower()
        # Logic for executing tasks based on query
         
        if "hello" in query:
            speak("hello sir how can i help.")
        elif "how are you" in query:
            speak("I am fine sir What about you")
        elif "fine" in query:
            speak("ok, sir")
        elif "bye" in query:
            speak("bye sir, you can call me any time")
            break
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("www.youtube.com")
        elif "open google" in query:
            speak("Opening google")
            webbrowser.open("www.google.com")
        elif "open github" in query:
            speak("Opening github")
            webbrowser.open("www.github.com")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Currently it is {strTime}")