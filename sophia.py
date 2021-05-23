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
assistant.setProperty('voice', voices[1].id)


def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # print(sr.Mircrophone.list_microphone_name()) # also pass device_index=1,2,3,0 etc
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


    
def startup():
    speak("Initializing Sophia")
    # speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Checking the internet connection")
    # speak("All drivers are up and running")
    # speak("All systems have been activated")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    strTime  =datetime.datetime.now().strftime('%H:%M:%S')
    speak(f"Currently it is {strTime}")
    speak("I am sophia. Online and ready sir. Please tell me how may I help you")


if __name__ == "__main__":
    startup()
    while True:
        try:
            query = takeCommand().lower()
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
                try:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    # print(results)
                    speak(results)
                except Exception as e:
                    print("Can not find result")
                    speak("Can not find result")
            
            elif 'open youtube' in query:
                speak("opening youtube")
                webbrowser.open("youtube.com")
            
            elif 'open github' in query:
                speak("opening github")  
                webbrowser.open("https://www.github.com")
           
            elif 'open facebook' in query:
                speak("opening facebook")      
                webbrowser.open("https://www.facebook.com")
            
            elif 'open instagram' in query:
                speak("opening instagram")    
                webbrowser.open("https://www.instagram.com")
            
            elif 'open google' in query:
                speak("opening google")
                webbrowser.open("https://www.google.com")
            
            elif 'open yahoo' in query:
                speak("opening yahoo")
                webbrowser.open("https://www.yahoo.com")
            
            elif 'open gmail' in query:
                speak("opening google mail") 
                webbrowser.open("https://mail.google.com")
                
            elif 'open snapdeal' in query:
                webbrowser.open("https://www.snapdeal.com") 
                speak("opening snapdeal")  
                
            elif 'open amazon' in query or 'shop online' in query:
                webbrowser.open("https://www.amazon.com")
                speak("opening amazon")
            
            elif 'open flipkart' in query:
                webbrowser.open("https://www.flipkart.com")
                speak("opening flipkart")   
            
            elif 'open ebay' in query:
                webbrowser.open("https://www.ebay.com")
                speak("opening ebay")
            
            elif "shutdown" in query:
                speak("shutting down")
                os.system('shutdown -s') 
            
            elif "what\'s up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
                ans_q = random.choice(stMsgs)
                speak(ans_q)  
                ans_take = takeCommand()
                
                if 'fine' in ans_take or 'happy' in ans_take or 'okey' in ans_take:
                    speak('okey..')  
                
                elif 'not' in ans_take or 'sad' in ans_take or 'upset' in ans_take:
                    speak('oh sorry..')  
            
            elif 'make you' in query or 'created you' in query or 'develop you' in query:
                ans_m = " For your information Yogesh, Krishna and Gulsher !."
                print(ans_m)
                speak(ans_m)
            elif "who are you" in query or "about you" in query or "your details" in query:
                about = "I am Sophia. I am computer based program but i can help you lot like a your close friend. Simple try me to give simple command ! I also play video and song from web or online. ok Lets Start "
                speak(about)

            elif "your name" in query or "sweat name" in query:
                na_me = "Thanks for Asking my name my self ! Sophia."  
                print(na_me)
                speak(na_me)

            elif query == 'none':
                continue 
            
            elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
                ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
                speak(ex_exit)
                exit()    
            else:
                temp = query.replace(' ','+')
                g_url="https://www.google.com/search?q="    
                res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
                print(res_g)
                speak(res_g)
                webbrowser.open(g_url+temp)
        
        except Exception as e:
            print(e)
            speak("I cannot recognize ")