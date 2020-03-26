from tkinter import *
import os
import requests
from PIL import ImageTk,Image,ImageDraw,ImageFont

#Basic Setup
osPath = os.path.dirname(__file__) 
iconPath = osPath + "/assets/icons/virus2.ico"
root = Tk()
root.geometry("975x570")
root.title("COVID-19 Information || Dev by Pongpon Sinlapa")
#root.configure(background='white')
root.iconbitmap(iconPath)

#set font
font_path = osPath + "/fonts/Sarabun-Regular.ttf"
font_type = ImageFont.truetype(font_path, 35)


#get data from api 
#Github https://github.com/javieraviles/covidAPI?fbclid=IwAR2rYnlwkO4EcZ5kYKQxzj4QBbY13w1ND1rhv01gomWvpmaL7kcx-MpNVow
res_global = requests.get("https://coronavirus-19-api.herokuapp.com/all")
#res_countries = requests.get(" https://coronavirus-19-api.herokuapp.com/countries")
data_global = res_global.json()

#set data to image
cases = str(data_global['cases'])
deaths = str(data_global['deaths'])
recover = str(data_global['recovered'])


#load image assets
#load background RIP
bg_path = Image.open(osPath + "/assets/img/bg.png")
drawText = ImageDraw.Draw(bg_path).text(xy=(65, 75),
                                         text=cases,
                                         font=font_type,
                                         fill="#ffff")
drawText = ImageDraw.Draw(bg_path).text(xy=(70, 275),
                                         text=deaths,
                                         font=font_type,
                                         fill="#ffff")
drawText = ImageDraw.Draw(bg_path).text(xy=(65, 455),
                                         text=recover,
                                         font=font_type,
                                         fill="#ffff")
bg_file = ImageTk.PhotoImage(bg_path) 
bg = Label(root, image=bg_file)

bg.pack()
#mainloop
root.mainloop()