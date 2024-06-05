import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound as p

def a(event):
    print(event)
    p.playsound("a.mp3")
 
def b(event):
    print(event)
    p.playsound("b.mp3")

def c(event):
    print(event)
    p.playsound("c.mp3")

def d(event):
    print(event)
    p.playsound("d.mp3")
 
def e(event):
    print(event)
    p.playsound("e.mp3")

def f(event):
    print(event)
    p.playsound("f.mp3")

win = tk.Tk()
win.title()

l1 = tk.Label(win,text="Press any button to play a sound")
l2 = tk.Button(win, text="Alien life-form", width=20)
l2.bind("<Button>",a)
l3 = tk.Button(win, text="Best Singer",width=20)
l3.bind("<Button>", b)
l4 = tk.Button(win, text="Actor",width=20)
l4.bind("<Button>", c)
l5 = tk.Button(win, text="Actually",width=20)
l5.bind("<Button>", d)
l6 = tk.Button(win, text="The life left in Beijing",width=20)
l6.bind("<Button>", e)
l7 = tk.Button(win, text="Vagrancy",width=20)
l7.bind("<Button>", f)

l1.grid(row=1, column=2)
l2.grid(row=2, column=1)
l3.grid(row=2, column=2)
l4.grid(row=2, column=3)
l5.grid(row=3, column=1)
l6.grid(row=3, column=2)
l7.grid(row=3, column=3)


win.mainloop()