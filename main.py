from tkinter import *
import os
import requests

#Root config
osPath = os.path.dirname(__file__) 
iconPath = osPath + "/assets/icons/virus2.ico"

root = Tk()
root.geometry("800x600")
root.title("COVID-19 Information")
root.iconbitmap(iconPath)

#Get data from api url
res = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
data = res.json()

#fetch data
for idx, item in enumerate(data):
    countryLabel = Label(root, text="ประเทศ: " + str(item['country']),font=18)
    countryLabel.grid(row = idx, column = 0)
    deathsLabel = Label(root, text="เสียชีวิต: " + str(item['deaths']),font=18)
    deathsLabel.grid(row = idx, column = 1)


#mainloop
root.mainloop()