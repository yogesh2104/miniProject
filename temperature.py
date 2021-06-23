import sophia as spk
import requests
from bs4 import BeautifulSoup
def temp(place):
    """
    Args:
        place ([str]): [take the place name as string]
    """    
    url = ("https://www.google.com/search?/q=" + place)
    req = requests.get(url)
    data = BeautifulSoup(req.txt, "html.parser")
    temerature = data.find("div",class_="Neawe").text
    spk.speak("the temperature outside is " + temerature + "celcius")
    