import webbrowser as web
import time
import keyboard
import pyautogui

def whatsapp(number,message):
    numb = '+91' + number
    open_chat = "https://web.whatsapp.com/send?photo=" + numb + "&text=" + message
    web.open(open_chat)
    time.sleep(15)
    keyboard.press('enter')

def Whatspp_Grp(group_id , message):
    open_chat = "https://web.whatsapp.com/accept?code=" + group_id
    web.open(open_chat)
    time.sleep(15)
    pyautogui.click(x=754 , y =696)
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')

