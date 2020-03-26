from tkinter import *
from tkinter import ttk 
import os
import requests
from PIL import ImageTk,Image,ImageDraw,ImageFont
import json 

#Basic Setup
osPath = os.path.dirname(__file__) 
iconPath = osPath + "/assets/icons/virus2.ico"
root = Tk()
root.resizable(width = FALSE, height = FALSE)
root.title("COVID-19 Information || Dev by Pongpon Sinlapa")
root.iconbitmap(iconPath)

canvas = Canvas(root,width = 975, height = 570)
image = ImageTk.PhotoImage(Image.open(osPath + "/assets/img/bg.png"))
canvas.create_image(0, 0, anchor=NW, image = image)
canvas.pack()

#Load country list
f = open("country.txt", "r")
countryList = []
for idx,i in enumerate(f.readlines()):
    countryList.insert(idx,i)

#Dropdown Country 
clicked = StringVar()
clicked.set(countryList[35])
dropdown = ttk.Combobox(root, width = 25, textvariable = clicked)
dropdown['values'] = countryList

dropdown_window = canvas.create_window(775, 20, anchor='nw', window = dropdown)


root.mainloop()