import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import time
import wikipedia #pip install wikipedia
import webbrowser
import os
import random


assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
# print(voices[1].id)
assistant.setProperty('voice', voices[1].id)


def speak(audio):
    """[summary]
                The audio is that which you are speak take as string[str] and then speak 
    Args:
        audio ([str]]): [none]
    """    
    assistant.say(audio)
    assistant.runAndWait()

def takeCommand():  
    command = sr.Recognizer()
    # with sr.Microphone(device_index=1) as source:
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


def startup():
    """[startup] this function will start when the sophia is run every time."""    
    speak("Initializing Sophia")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Checking the internet connection")
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
    speak("I am sophia. Online and ready sir. Please tell me how may I help you")

if __name__ == "__main__":
    # startup()
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

            elif "time" in query:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                speak(f"Currently it is {strTime}")
            
            elif 'wikipedia' in query:
                try:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
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
            
            elif 'make you' in query or 'created you' in query or 'develop you' in query:
                ans_m = " For your information Yogesh, Krishna and Gulsher Develop me!."
                print(ans_m)
                speak(ans_m)
            elif "who are you" in query or "about you" in query or "your details" in query:
                about = "I am Sophia. I am computer based program but i can help you lot like a your close friend. Simple try me to give simple command ! I also play video and song from web or online. ok Lets Start "
                speak(about)
                print(about)

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
            
            elif 'open code' in query:
                code_path = "C:\\Users\\Yogesh Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("Openning VSCODE")
                os.startfile(code_path)
            
            elif 'play song' in query:
                music_folder = "E:\\audios"
                song = os.listdir(music_folder)
                all_song=len(song)
                import random
                rand_song = random.randint(0, all_song-1)
                os.startfile(os.path.join(music_folder,song[rand_song]))

 
            elif "search on youtube" in query:
                link = takeCommand()
                link = link.replace("search",'')
                link = link.replace("on","")
                link = link.replace("youtube","")
                from gyw import YouTubeSearch
                YouTubeSearch(link)
                speak("Enjoy!")

            elif "google sesrch" in query:
                pass

            elif 'remember that' in query:
                rememberMsg = query.replace("sophia",'')
                rememberMsg = query.replace('remember that','')
                speak("You tell me to remind you that" + rememberMsg)
                remeber = open("C:\\Users\\Yogesh Singh\\Desktop\\miniproject\\Database\\data.txt")
                remeber.write(rememberMsg)
                remeber.close()


            elif 'what you remember' in query:
                remeber = open("C:\\Users\\Yogesh Singh\\Desktop\\miniproject\\Database\\data.txt")
                speak(f"You tell me to remember is that {remeber.read()}")


            elif 'temperature' in query:
                import temperature
                speak("city name please")
                place = ("Temperature in ").takeCommand()
                temperature(place)
            

            

        except Exception as e:
            print(e)
            speak("I cannot recognize ")