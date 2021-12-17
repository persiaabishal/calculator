# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:41:51 2021

@author: Abishal
"""

from tkinter import *
window=Tk()
window.geometry("350x350")
e=Entry(window,width=56,borderwidth=5)
e.place(x=0,y=0)
def btclick(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
    

b=Button(window,text='1',width=12,command=lambda:btclick(1))
b.place(x=10,y=60)

b=Button(window,text='2',width=12,command=lambda:btclick(2))
b.place(x=80,y=60)

b=Button(window,text='3',width=12,command=lambda:btclick(3))
b.place(x=170,y=60)

b=Button(window,text='4',width=12,command=lambda:btclick(4))
b.place(x=10,y=120)

b=Button(window,text='5',width=12,command=lambda:btclick(5))
b.place(x=80,y=120)

b=Button(window,text='6',width=12,command=lambda:btclick(6))
b.place(x=170,y=120)

b=Button(window,text='7',width=12,command=lambda:btclick(7))
b.place(x=10,y=180)

b=Button(window,text='8',width=12,command=lambda:btclick(8))
b.place(x=80,y=180)

b=Button(window,text='9',width=12,command=lambda:btclick(9))
b.place(x=170,y=180)

b=Button(window,text='0',width=12,command=lambda:btclick(0))
b.place(x=10,y=240)

def add():
    firstno=e.get()
    global math
    math='addition'
    global f
    f=int(firstno)
    e.delete(0,END)

b=Button(window,text='+',width=12,command=add)
b.place(x=80,y=240)

def sub():
    firstno=e.get()
    global math
    math='subtraction'
    global f
    f=int(firstno)
    e.delete(0,END)

    
b=Button(window,text='-',width=12,command=sub)
b.place(x=170,y=240)

def mul():
    firstno=e.get()
    global math
    math='multiplication'
    global f
    f=int(firstno)
    e.delete(0,END)

    
b=Button(window,text='*',width=12,command=mul)
b.place(x=10,y=300)

def div():
    firstno=e.get()
    global math
    math='division'
    global f
    f=int(firstno)
    e.delete(0,END)

b=Button(window,text='/',width=12,command=div)
b.place(x=80,y=300)
def eq():
    secondno=e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,f+int(secondno))
    elif math=='subtraction':
        e.insert(0,f-int(secondno))
    elif math=='multiplication':
        e.insert(0,f*int(secondno))
    elif math=='division':
        e.insert(0,f/int(secondno))
        
        
b=Button(window,text='=',width=12,command=eq)
b.place(x=170,y=300)

def clear():
    e.delete(0,END)
b=Button(window,text='clear',width=12,command=clear)
b.place(x=10,y=350)



window.mainloop()
