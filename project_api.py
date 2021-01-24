from tkinter import *
from PIL import ImageTk,Image
import requests
import json
from tkinter import messagebox

def loadSplash():
    root = Tk()
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d+%d+%d" % (width * 0.5, height * 0.5,width * 0.25, height * 0.25))

    image = ImageTk.PhotoImage(Image.open('bg1.jpeg'))
    canvas = Canvas(root, height=height * 0.5, width=width * 0.5, bg="brown")
    canvas.create_image(width * 0.5 / 2, height * 0.5 / 2, image=image)
    canvas.pack()
    # show the splash screen for 2000 milliseconds then destroy
    root.after(2000, root.destroy)
    root.mainloop()

loadSplash()
#import timezone
root = Tk()
root.title("Weather Now")
root.iconbitmap("m.ico")
root.geometry("700x300")
bg_root = "#14161a"
root.configure(background=bg_root)

def weather_lookup():
    try:
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid=15c0971cb976b3bda8755b411fe07094&units=metric".format(city.get().capitalize()))
        api = json.loads(api_request.content)
        #api = api_request.json()
        #print(1)
        clouds=api['clouds']['all']
        latitude = api['coord']['lat']
        longitude = api['coord']['lon']
        feel = api['main']['feels_like']
        humidity  = api['main']['humidity']
        pressure = api['main']['pressure']
        temp = api['main']['temp']
        country = api['sys']['country']
        time = api['timezone']
        visibility = api['visibility']
        description = api['weather'][0]['description']
        wind_speed = api['wind']['speed']
        wind_d = api['wind']['deg']
        #print(2)
        #DIRECTION OF WIND
        if (wind_d>=0 and wind_d<=11.25) or (wind_d<=360 and wind_d>=348.75):
            direction = "N" #wind direction north
        elif wind_d>=11.25 and wind_d<=33.75:
            direction = "NNE" #wind direction north east
        elif wind_d>=33.75 and wind_d<=56.25:
            direction = "NE"
        elif wind_d>=56.25 and wind_d<=78.75:
            direction = "ENE"
        elif wind_d>=78.75 and wind_d<=101.25:
            direction = "E"
        elif wind_d>=101.25 and wind_d<=123.75:
            direction = "ESE"
        elif wind_d>=123.75 and wind_d<=146.25:
            direction = "SE"
        elif wind_d>=146.25 and wind_d<=168.75:
            direction = "SSE"
        elif wind_d>=168.75 and wind_d<=191.25:
            direction = "S"
        elif wind_d>=191.25 and wind_d<=213.75:
            direction = "SSW"
        elif wind_d>=213.75 and wind_d<=236.25:
            direction = "SW"
        elif wind_d>=236.25 and wind_d<=258.75:
            direction = "WSW"
        elif wind_d>=258.75 and wind_d<=281.25:
            direction = "W"
        elif wind_d>=281.25 and wind_d<=303.75:
            direction = "WNW"
        elif wind_d>=303.75 and wind_d<=326.25:
            direction = "NW"
        elif wind_d>=326.25 and wind_d<=348.75:
            direction = "NNW"
        else:
            direction = "N"
        #print(3)
        #cloud interpretation
        if clouds >=0 and clouds <=10:
            cloud = "Sunny Day"
            day = "sunny.png"
        elif clouds>10 and clouds<=30:
            cloud ="Mostly Sunny Day"
            day = "mostly sunny.png"
        elif clouds>30 and clouds<=60:
            cloud ="Partly Sunny Day"
            day = "partly sunny.png"
        elif clouds>60 and clouds<=90:
            cloud="Mostly Cloudy"
            day = "mostly cloudy.png"
        else:
            cloud="Cloudy"
            day = "cloudy.png"

        #print(4)
        #wind type"
        winds = wind_speed*3.6

        if winds>=0 and winds<1:
            wind_type = "Calm"
        elif winds>=1 and winds<=3:
            wind_type ="Light Air"
        elif winds>3 and winds<=7:
            wind_type = "Light Breeze"
        elif winds>7 and winds<=12:
            wind_type = "Gentle Breeze"
        elif winds>12 and winds<=18:
            wind_type = "Moderate Breeze"
        elif winds>18 and winds<=24:
            wind_type = "Fresh Breeze"
        elif winds>24 and winds<=31:
            wind_type = "Strong Breeze"
        elif winds>31 and winds<=38:
            wind_type = "Near Gale"
        elif winds>38 and winds<=46:
            wind_type = "Gale"
        elif winds>46 and winds<=54:
            wind_type = "Strong Gale"
        elif winds>54 and winds<=63:
            wind_type = "Whole Gale"
        elif winds>63 and winds<=75:
            wind_type = "Storm Force"
        else :
            wind_type = "Hurricane Force"

        #print(api)
        #time details
        time_request = requests.get(' http://api.timezonedb.com/v2.1/get-time-zone?key=KM0U3KGCH95P&format=json&by=position&lat='+str(latitude)+'&lng='+str(longitude))
        time_api = json.loads(time_request.content)

        date_time = time_api['formatted']
        zone = time_api['zoneName']
        abb = time_api['abbreviation']

        #print(time_api)
        #new Toplevel
        result = Toplevel()
        result.title("Weather Updates")
        result.iconbitmap("m.ico")
        result.geometry("850x600")
        bg_result ="#2cd4f5"
        result.configure(background=bg_result)

        city_l = Label(result,text = city.get().capitalize()+ ", "+ country , font= ("Helvectica",20), bg  = bg_result,fg ="white")
        city_l.grid(row = 1,column = 0,ipadx=200,pady=30)
        #°C
        cloud_img = ImageTk.PhotoImage(Image.open(day))
        result.photo = cloud_img

        day_label = Label(result,image = cloud_img,bg= bg_result).grid(row = 2,column=0)

        time_l= Label(result,text =date_time+" "+abb+" \n Timezone: "+zone,font = ("Helvectica",15),bg  = bg_result,fg ="white")
        time_l.grid(row = 3,column = 0,ipadx=200)

        land = Label(result,text = "Latitude:"+str(latitude)+" | "+"Longitude:"+str(longitude), font= ("Helvectica",20), bg  = bg_result,fg ="white")
        land.grid(row=4,column=0,ipadx=200,ipady=10)

        temp_l = Label(result,text = str(temp)+"°C", font = ("Helvectica",20),bg  = bg_result,fg ="white" )
        temp_l.grid(row = 5,column = 0,ipadx = 200)

        #need to make a line
        canvas = Canvas(result,width = 500,height = 2)
        canvas.create_line(6,0,6,500,width= 500,fill ="white")
        canvas.grid(row = 6,column = 0)

        wind_l = Label(result,text ="Wind "+str(wind_speed)+" m/s , "+direction,font = ("Helvectica",20),bg  = bg_result,fg ="white")
        wind_l.grid(row = 7, column =0,ipadx = 150,ipady =5)

        cloud_l = Label(result,text = "Cloudiness: "+str(clouds)+"% | "+cloud, font = ("Helvectica",20),bg  = bg_result,fg ="white")
        cloud_l.grid(row = 8,column = 0,ipadx=200,ipady=5)

        pressure_l= Label(result,text ="Pressure: " +str(pressure)+" hPa | Humidity: "+str(humidity)+"%",font = ("Helvectica",15),bg  = bg_result,fg ="white")
        pressure_l.grid(row = 9,column = 0,ipadx=200,ipady=5)

        visible = Label(result, text= "Visibility: "+str(visibility/1000)+" km", font = ("Helvectica",15),bg  = bg_result,fg ="white")
        visible.grid(row = 10,column = 0,ipadx=200,ipady=5)

        canvas_2 = Canvas(result,width = 500,height = 2) #canvas object
        canvas_2.create_line(10,0,10,200,width= 500,fill ="white")
        canvas_2.grid(row = 11,column = 0)

        feels_like = Label(result, text= "Feels Like "+str(feel)+"°C", font = ("Helvectica",15),bg  = bg_result,fg ="white")
        feels_like.grid(row = 12,column = 0,ipadx=200,ipady=5)

        description_l = Label(result, text=description.capitalize() + " , " + wind_type, font = ("Helvectica",15),bg  = bg_result,fg ="white")
        description_l.grid(row = 13,column = 0,ipadx=200,ipady=5)

    except Exception as e:
        api = "Error......."
        response=messagebox.showinfo("Error","City Doesn't Exist/City not available . Try Again!")

Label_main = Label(root,text="Weather Updates",font=("Helvectica",20),background = "#2cd4f5",padx = 20,pady = 20,borderwidth = 5,relief = "groove")
Label_main.grid(row=0,column=0, padx = 200,pady = 20.)

Label_1 = Label(root,text = "Enter city name to find the weather",font=("Helvectica",12),padx = 10,pady =5,background = "#495252",fg = "white",relief = "groove")
Label_1.grid(row=1 ,column =0,pady=10)

city = Entry(root)
city.grid(row=2,column=0,sticky=W+E+N+S,padx=200,ipady =10)

search = ImageTk.PhotoImage(Image.open("find40.png"))
select_btn = Button(root,text="Weather in your city? ",image = search,compound = "left",font=("Helvectica",10),background ="#495252",fg = "white",padx = 5,command = weather_lookup )
select_btn.grid(row=3,column =0,pady = 10)

root.mainloop()
