import pyttsx3
import speech_recognition as sr
# import time

assistant = pyttsx3.init('sapi5')
voice = assistant.getProperty('voices')
# print(voice)
assistant.setProperty('voices',voice[0].id)
def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()
    print(f"You Say : {audio}")

# speak("Hello sir how can i help")
def recognize():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....................")
        command.pause_threshold=1
        audio = command.listen(source)
    try:
        print("Recognizing.......")
        key_word = command.recognize_google(audio, language='en-US')
        print(f"You say : {key_word}")
    except Exception as Error:
        return "None"
    return key_word.lower()
query = recognize()
# speak("Hello")