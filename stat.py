import bs4
import requests
import urllib
import lxml
from bs4 import BeautifulSoup
from playsound import playsound
import threading
import os
import sys
import time
import ctypes   
from tkinter import * 

from multiprocessing import Process
def Check():
    


    
    
    s = requests.Session()
    r = s.post('http://stat.ukrsat.mk.ua/login.php', data = {'user':'Input login here', 'password':'and password'})
    r = s.get('http://stat.ukrsat.mk.ua/index.php')

    b=bs4.BeautifulSoup(r.text,'lxml')
    par=b.center.b.text

    result=round(float(par))
        
    
    return result 

def alert():
    Check()
    result=Check()
    if result < 10:
        while True:
            playsound('alarm.mp3')
    
def UI():
    Check()
    result=Check()
    root=Tk()
    root.title("Stat")
    root.configure(background='gray')

    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))

    root.geometry("300x300")
    label1=Label(root,text="На счету:",fg="#eee", bg="#333")
    label2=Label(root,text=result)
    label3=Label(root,text="Интернет счет",fg="#eee", bg="#333")

    label1.config(font=("Ariel", 12))
    label2.config(fon=("Ariel",12))
    label1.place(relx=0.3, rely=0.5)
    label2.place(relx=0.55, rely=0.5)
    label3.place(relx=0.3,rely=0.1)
    button = Button(root, text="Выйти", fg="#eee",bg="#333",command=sys.exit)
    root.overrideredirect(1)
    button.place(relx=0.3,rely=0.8) 
    
    if result < 10:
        
        label2.config(bg="red")
        
    else: 
        label2.config(bg="green")
        
    
    root.mainloop()

if __name__ == '__main__':
    p1=Process(target=alert)
    p1.start()
    p2=Process(target=UI)
    p2.start()

