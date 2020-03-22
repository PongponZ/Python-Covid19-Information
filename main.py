from tkinter import *
import os
import requests
from PIL import ImageTk,Image,ImageDraw,ImageFont

#Basic Setup
osPath = os.path.dirname(__file__) 
iconPath = osPath + "/assets/icons/virus2.ico"
root = Tk()
root.geometry("980x700")
root.title("COVID-19 Information || Dev by Pongpon Sinlapa")
#root.configure(background='white')
root.iconbitmap(iconPath)

#set font
font_path = osPath + "/fonts/Sarabun-Regular.ttf"
font_type = ImageFont.truetype(font_path, 30)


#get data from api 
#Github https://github.com/javieraviles/covidAPI?fbclid=IwAR2rYnlwkO4EcZ5kYKQxzj4QBbY13w1ND1rhv01gomWvpmaL7kcx-MpNVow
res_global = requests.get("https://coronavirus-19-api.herokuapp.com/all")
#res_countries = requests.get(" https://coronavirus-19-api.herokuapp.com/countries")
data_global = res_global.json()

#set data to image
deaths = str(data_global['deaths'])
recover = str(data_global['recovered'])


#load image assets
#load background RIP
deathsBG_path = Image.open(osPath + "/assets/img/deaths.png")
drawText = ImageDraw.Draw(deathsBG_path).text(xy=(65, 60),
                                         text=deaths,
                                         font=font_type,
                                         fill="#ffff")
                                            
deathsBG_resize = deathsBG_path.resize((250, 250), Image.ANTIALIAS)
deathsBG_file = ImageTk.PhotoImage(deathsBG_resize) 
deathsBG = Label(root, image=deathsBG_file)

#load background recover 
recoverBG_path = Image.open(osPath + "/assets/img/recover.png")
drawText = ImageDraw.Draw(recoverBG_path).text(xy=(65, 60),
                                               text=recover,
                                               font=font_type,
                                               fill="#ffff")
                                            
recoverBG_resize = recoverBG_path.resize((250, 250), Image.ANTIALIAS)
recoverBG_file = ImageTk.PhotoImage(recoverBG_resize) 
recoverBG = Label(root, image=recoverBG_file)


#set Grid
deathsBG.grid(row=0, column = 0)
recoverBG.grid(row=1, column = 0)

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