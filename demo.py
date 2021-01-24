from tkinter import *
from PIL import ImageTk,Image
import requests
import json
from tkinter import messagebox
from tkinter import ttk
import os

#from tkinter import *

from tkinter.ttk import *
def loadSplash():
    root = Tk()
    # show no frame
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(
        "%dx%d+%d+%d" % (width * 0.5, height * 0.5,
                         width * 0.25, height * 0.25)
    )
    # take a .jpg picture you like, add text with a program like PhotoFiltre
    # (free from http://www.photofiltre.com) and save as a .gif image file
    image_file = os.getcwd() + "//bg1.jpeg"
    # assert os.path.exists(image_file
    # use Tkinter's PhotoImage for .gif files

    image = ImageTk.PhotoImage(Image.open('bg1.jpeg'))
    canvas = Canvas(root, height=height * 0.5,
                       width=width * 0.5, bg="brown")
    canvas.create_image(width * 0.5 / 2, height * 0.5 / 2, image=image)
    canvas.pack()
    # show the splash screen for 5000 milliseconds then destroy
    root.after(2000, root.destroy)
    root.mainloop()

loadSplash()
root=Tk()
root.title("weather")
root.iconbitmap("m.ico")
root.geometry("600x400")
back = ImageTk.PhotoImage(Image.open('rootbg600.jpg'))
c = Canvas(root, bg ="white", height = 300, width = 300 )

background_label = Label(root,image = back)
background_label.place( x= 0, y=0,relwidth = 1, relheight = 1)

c.pack()
'''
back = ImageTk.PhotoImage(Image.open('rootbg.jpg'))
w = back.width()
h = back.height()
root.geometry("%dx%d"%(w,h))
root.configure(background = back)


ttk.Style().configure("Tbutton",padding = 6, relief = "sunken",background="red")

def ziplookup():

    try:
        #we create a variable api_request to request and get data
        api_request =  requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip.get()+"&distance=5&API_KEY=987A095D-B3A7-41CD-B6CB-C8FA16EEE6D6")
        api = json.loads(api_request.content)#try it
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category=="Good":
            weather_color = "#0C0"

        elif category=="Moderate":
            weather_color = "#FFFF00"

        elif category==" Unhealthy for Sensitive Groups":
            weather_color="ff9900"

        elif category==" Unhealthy":
            weather_color="FF0000"

        elif category=="Very Unhealthy":
            weather_color="#990066"

        elif category=="Hazardous ":
            weather_color="#660000"

        weather_update=city+ " Air Quality "+ str(quality)+" "+category
        myLabel = Label(root, text=weather_update, font=("Helvectica",20),background=weather_color)
        myLabel.grid(row=1,column=0)
         #to change the font of the label we do: font=(" fontstyle",fontsize)
        root.configure(background=weather_color)
    except Exception as e :#if any error
        api = "Error......"
        #response=messagebox.showinfo("Error","Zipcode Doesn't Exist. Try Again!")
        #me.popup()


zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton= Button(root, text="Lookup Zipcode",command=ziplookup)
zipButton.grid(row=0,column=1, sticky=W+E+N+S)


style = ttk.Style()
style.configure("BW.TLabel",foreground = "Black",background="White",borderwidth = 3)

l1 = ttk.Label(text="Test", style="BW.TLabel").grid(row = 1,column = 0)
l2 = ttk.Label(text="Test", style="BW.TLabel").grid(row = 2,column=0)

l3 = Label(root, text = "Normal Label",foreground = "Blue",background = "Red")
l3.grid(row = 3, column = 0)

b1 = ttk.Button(text = "Smple").grid( row = 3, column =1 )
'''
root.mainloop()
