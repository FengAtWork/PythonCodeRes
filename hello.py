# Learn Python Coding 2023
# Feng Lin 
# Using Git on Git Bash
########################################
# clear the terminal
from tkinter import *
import os
os.system('clear')

##################
# TKinter GUI
##################

root = Tk()
root.title('Feng - first GUI in Python')
root.geometry("400x600")

def hello():
	hello_label = Label(root, text = "Hello " + myTextbox.get())
	hello_label.pack()

myLabel = Label(root, text = "Enter your first name:")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text = "Submit", command = hello)
myButton.pack()

root.mainloop()