import sophia as spk
# from sophia import *
import pywhatkit
import webbrowser as web
import wikipedia


def YouTubeSearch(link):
    """
    link: This is the link which we want to search on youtube 
    @param name: Name of the property to fetch
    @type name: str
    @param: Value to set for the property

    """
    result = "https://www.youtube.com/result?search_query=" + link
    web.open(result)
    spk.speak("This is what i found!")
    pywhatkit.playonyt(link)

def GoogleSearch(link): 
    """
    link: this would be a word or sentence which is searched on google 
    @param name: Name of the property to fetch
    @type name: str
    @param: Value to set for the property
    
    """
    link = link.replace('sophia','')
    link = link.replace('how to','')
    link = link.replace('what is','')
    link = link.replace('what do you mean by','')
    Query = str(link)
    pywhatkit.search(Query)
    if 'how to' in Query:
        max_result = 1
        # how_to = search_wikihow
        pass


def whatsappmsg():
    spk.speak("Tell me the name of Person")
    name = spk.takeCommand()
    if 'yogesh' in name:
        spk.speak("Please Tell me the message")
        msg = spk.takeCommand()
        spk.speak("tell me the time. time in hour.")
        hour = int(spk.takeCommand())
        spk.speak("tell me the time. time in minutes.")
        min = int(spk.takeCommand())
        pywhatkit.sendwhatmsg("+918850281705",msg,hour,min,20)
        spk.speak("ok,sir sending message on whatsapp")
    elif 'krishna' in name:
        spk.speak("Please Tell me the message")
        msg = spk.takeCommand()
        spk.speak("tell me the time. time in hour.")
        hour = int(spk.takeCommand())
        spk.speak("tell me the time. time in minutes.")
        min = int(spk.takeCommand())
        pywhatkit.sendwhatmsg("+918850281705",msg,hour,min,20)
        spk.speak("ok,sir sending message on whatsapp")
    elif 'gulser' in name:
        spk.speak("Please Tell me the message")
        msg = spk.takeCommand()
        spk.speak("tell me the time. time in hour.")
        hour = int(spk.takeCommand())
        spk.speak("tell me the time. time in minutes.")
        min = int(spk.takeCommand())
        pywhatkit.sendwhatmsg("+918850281705",msg,hour,min,20)
        spk.speak("ok,sir sending message on whatsapp")
    else:
        spk.speak("Tell me th number")
        num = int(spk.takeCommand())
        phone_num = '+91' + num
        spk.speak("Please Tell me the message")
        msg = spk.takeCommand()
        spk.speak("tell me the time. time in hour.")
        hour = int(spk.takeCommand())
        spk.speak("tell me the time. time in minutes.")
        min = int(spk.takeCommand())
        pywhatkit.sendwhatmsg(phone_num,msg,hour,min,20)
        spk.speak("ok,sir sending message on whatsapp")
        




