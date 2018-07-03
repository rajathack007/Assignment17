# Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import tkinter
from tkinter import *
root=Tk()
label=Label(root,text="Hello World1!",bg='red',fg='white')
label.pack()
b=Button(root,text="exit",width=30,bg='blue',fg='black',command=exit)
b.pack()
root.mainloop()
# Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
import tkinter
from tkinter import *
def display():
    label=Label(root,text="hii i am there")
    label.pack()
root=Tk()
label=Label(root,text="Hello World1!",bg='red',fg='white')
label.pack()
b=Button(root,text="exit",width=30,bg='blue',fg='black',command=exit)
b.pack()
b1=Button(root,text="click",width=25,bg='red',command=display)
b1.pack()
root.mainloop()
#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
import tkinter
from tkinter import *
def display():
    label.config(text="hello python")
root=Tk()
f1=Frame(root)
f1.pack()
label=Label(f1,text="hello world",width=20)
label.pack()
b1=Button(f1,text="exit",width=30,command=exit)
b1.pack()
b2=Button(f1,text="change",width=25,command=display)
b2.pack()
root.mainloop()

#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
import tkinter
from tkinter import *
def show():
    print(entry.get())
root=Tk()
entry=Entry(root,width=40)
entry.pack()
b=Button(root,text="click",width=20,command=show)
b.pack()
root.mainloop()
