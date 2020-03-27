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

#Function Get Data follow select at Combobox
def getCountryData(event):
    url = "https://coronavirus-19-api.herokuapp.com/countries/" + dropdown.get()
    data_country = requests.get(url).json()
    canvas.itemconfigure(deaths, text=str(data_country['deaths']))
    canvas.itemconfigure(todayCases, text=str(data_country['todayCases']))
    canvas.itemconfigure(todayDeaths, text=str(data_country['todayDeaths']))
    canvas.itemconfigure(cases, text=str(data_country['cases']))
    canvas.itemconfigure(critical, text=str(data_country['critical']))
    canvas.itemconfigure(recovered, text=str(data_country['recovered']))


#setCountry
countryList = ["Australia","Austria","Belgium","Brazil","Canada","Chile","China",
               "Czechia","Denmark","Ecuador","Finland","France","Germany","Greece","Iceland",
               "Indonesia","Iran","Ireland", "Israel", "Italy", "Japan", "Luxembourg", "Malaysia",
               "Netherlands","Norway", "Pakistan","Poland", "Portugal" ,"Romania", "Russia", "S. Korea",
               "Saudi","Arabia","Spain","Sweden","Switzerland","Thailand","Turkey","UK","USA"]

#Get Global data from Api
data_global = requests.get("https://coronavirus-19-api.herokuapp.com/all").json()


#data
cases = str(data_global['cases'])
deaths = str(data_global['deaths'])
recover = str(data_global['recovered'])

#Dropdown Country 
clicked = StringVar()
clicked.set(countryList[36])
dropdown = ttk.Combobox(root, width = 25, textvariable = clicked, state = "readonly")
dropdown['values'] = countryList
dropdown.bind('<<ComboboxSelected>>', getCountryData) 
dropdown_window = canvas.create_window(775, 20, anchor='nw', window = dropdown)

#set data text position
#Global data text
casesGlobal = canvas.create_text(120, 110, text=cases, font = ('Arial', 30), fill = "white")
deathGlobal = canvas.create_text(120, 310, text=deaths, font = ('Arial', 30), fill = "white")
recoverGlobal = canvas.create_text(120, 480, text=recover, font = ('Arial', 30), fill = "white")

#Country data text
deaths = canvas.create_text(370, 200, text='', font = ('Arial', 30), fill = "white")
todayCases = canvas.create_text(610, 200, text='', font = ('Arial', 30), fill = "white")
todayDeaths = canvas.create_text(845, 200, text='', font = ('Arial', 30), fill = "white")
cases = canvas.create_text(370, 370, text='', font = ('Arial', 30), fill = "white")
critical = canvas.create_text(610, 370, text='', font = ('Arial', 30), fill = "white")
recovered = canvas.create_text(845, 370, text="", font = ('Arial', 30), fill = "white")


#first run
getCountryData("run")



root.mainloop()