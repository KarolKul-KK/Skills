from tkinter import *
from PIL import ImageTk, ImageTk
import requests
import json

root = Tk()
root.title('Code at home')
root.geometry("600x100")

#Create Zipcode lookup Function
def ziplookup():
    zip.get()
    zipLabel = Label(root, text=zip.get())
    zipLabel.grid(row=1, column=0, columnspan=2)

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=B847548A-BF82-4809-B9AD-A1D978B4581E



    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=B847548A-BF82-4809-B9AD-A1D978B4581E")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        print(category)

        if category == 'Good':
            weather_color = "#0C0"
        elif category == 'Moderate':
            weather_color = "#FFFF00"
        elif category == 'Unheathly for Sensitive Groups':
            weather_color = "#ff9900"
        elif category == 'Unheathly':
            weather_color = "#FF0000"
        elif category == 'Very Unheathly':
            weather_color = "#990066"
        elif category == 'Hazardous':
            weather_color = "#660000"

        print(weather_color)

        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1, column=1)
        root.configure(background=weather_color)

    except Exception as e:
        api = "Error..."

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command=ziplookup)
zipButton.grid(row=1, column=0, columnspan=2, stick=W+E+N+S)

root.mainloop()