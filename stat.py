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
import signal   
from tkinter import * 

import multiprocessing as mp
def Check():
    


    
    
    s = requests.Session()
    r = s.post('http://stat.ukrsat.mk.ua/login.php', data = {'user':'globus12', 'password':'fAzvawZ5g'})
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
    

def on_closing():
    pid=os.getpid()
    os.kill(pid, signal.CTRL_C_EVENT)

if __name__ == '__main__':
    
    Check()
    result=Check()
    root=Tk()
    root.title("Stat")
    root.configure(background='gray')
    
    p1=mp.Process(target=alert)
    p1.start()
    
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
    
    
    if result < 10:
        
        label2.config(bg="red")
        
    else: 
        label2.config(bg="green")
        
    root.protocol("WM_DELETE_WINDOW",on_closing )
    root.mainloop()

    
