from tkinter import *
import os
import requests
from PIL import ImageTk,Image,ImageDraw,ImageFont

#Basic Setup
osPath = os.path.dirname(__file__) 
iconPath = osPath + "/assets/icons/virus2.ico"
root = Tk()
root.geometry("800x600")
root.title("COVID-19 Information")
root.iconbitmap(iconPath)

#set font
font_path = osPath + "/fonts/Sarabun-Regular.ttf"
font_type = ImageFont.truetype(font_path, 70)


#get data from api 
#Github https://github.com/javieraviles/covidAPI?fbclid=IwAR2rYnlwkO4EcZ5kYKQxzj4QBbY13w1ND1rhv01gomWvpmaL7kcx-MpNVow
res_global = requests.get("https://coronavirus-19-api.herokuapp.com/all")
data_global = res_global.json()

#set data to image
deaths = str(data_global['deaths'])



#load image assets
#load background RIP
rip_path = Image.open(osPath + "/assets/img/rip.png")
drawText = ImageDraw.Draw(rip_path)
drawText.text(xy=(200, 400), text=deaths, fill=(0,0,0), font=font_type)
ripImage_resize = rip_path.resize((150, 100), Image.ANTIALIAS)
ripImage_file = ImageTk.PhotoImage(ripImage_resize) 

ripImage = Label(image = ripImage_file)

ripImage.grid(row=0, column = 0)

"""
#fetch data
for idx, item in enumerate(data):
    countryLabel = Label(root, text="ประเทศ: " + str(item['country']),font=18)
    countryLabel.grid(row = idx, column = 0)
    deathsLabel = Label(root, text="เสียชีวิต: " + str(item['deaths']),font=18)
    deathsLabel.grid(row = idx, column = 1)
"""

#mainloop
root.mainloop()