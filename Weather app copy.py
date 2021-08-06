#WEATHER DESCRIPTIONS clear sky  few clouds scattered clouds broken clouds shower rain rain thunderstorm snow mist

#This is a simple python project that uses Open weather API for weather forcast

#variables
button1= None
button2= None
button3= None
button4= None
button5= None
button6= None
button7= None
button8= None
button9= None
button_text1= None
button_text2= None
button_text3= None
button_text4= None
button_text5= None
button_text6= None
button_text7= None
button_text8= None
button_text9= None
button_texts=[button_text1,button_text2,button_text3,button_text4, button_text5, button_text6,button_text7,button_text8,button_text9]
weather_object1=None
weather_object2=None
weather_object3=None
weather_object4=None
weather_object5=None
weather_object6=None
weather_object7=None
weather_object8=None
weather_object9=None
weather_objects=[weather_object1, weather_object2, weather_object3, weather_object4, weather_object5, weather_object6, weather_object7, weather_object8, weather_object9,]
GUI_address=None
weather_info1=None
weather_info2=None
weather_info3=None
weather_info4=None
weather_info5=None
weather_info6=None
weather_info7=None
weather_info8=None
weather_info9=None
weather_infos=[weather_info1, weather_info2, weather_info3, weather_info4, weather_info5, weather_info6, weather_info7, weather_info8, weather_info9, ]
weather_data=["weather_info1","weather_info2","weather_info3","weather_info4","weather_info5","weather_info6","weather_info7","weather_info8","weather_info9",]
weather_status=[" "," "," "," "," "," "," "," "," "]
button_list=[button1, button2, button3, button4, button5, button6, button7, button8, button9]
description=""

#weather descriptions 
thunderstorm=["thunderstorm with light rain","thunderstorm with rain","thunderstorm with heavy rain","light thunderstorm","thunderstorm","heavy thunderstorm","ragged thunderstorm","thunderstorm with light drizzle","thunderstorm with drizzle","thunderstorm with heavy drizzle"]
drizzle=["light intensity drizzle","drizzle","heavy intensity drizzle","light intensity drizzle rain","drizzle rain","heavy intensity drizzle rain","shower rain and drizzle","heavy shower rain and drizzle","shower drizzle"]
rain=["light rain","moderate rain","heavy intensity rain","very heavy rain","extreme rain","freezing rain","light intensity shower rain","shower rain","heavy intensity shower rain","ragged shower rain"]
snow=["light snow","Snow","Heavy snow","Sleet","Light shower sleet","Shower sleet","Light rain and snow","Rain and snow","Light shower snow","Shower snow","Heavy shower snow"]
atmosphere=["mist","Smoke","Haze","sand/ dust whirls","fog","sand","dust","volcanic ash", "squalls", "tornado"]
clear_sky=["clear sky"]
clouds=["few clouds","scattered clouds","broken clouds","overcast clouds"]


#Import libraries

#BackEnd imports
import requests #import request #to pass a get request to the api
import json
from geopy.geocoders import ArcGIS  #for geocoding

#Frontend Imports
from tkinter import *
import tkinter.simpledialog as dialog
import tkinter.messagebox as message
from PIL import Image, ImageTk



my_api_key="e09789dc0702eba3041eea856433ffc2"  # A global variable that allow access to the api
my_api_key2="1fa54ccba1edb660f5ed9e45f63340d7"


class Places:
    get_url="api.openweathermap.org/data/2.5/weather?"
    get_url2="http://api.positionstack.com/v1/forward?"
    api_key=my_api_key
    api_key2=my_api_key2
    
    def __init__(self, address, city, state, country):
        self.Address= address+","+city+","+state+","+country
        self.city=city
        self.state=state
        self.country=country
        
    def get_location(self):
        #get the location coordinate
        location = ArcGIS() #create an instance of ArcGIS
        self.locate=location.geocode(self.Address)
        self.latitude=str(self.locate.latitude)
        self.longitude=str(self.locate.longitude)
        
    def get_location2(self):
        self.url_sub=Places.get_url2+"access_key="+Places.api_key2+"&query="+self.Address
        self.coordinate_info=requests.get(self.url_sub)
        print(self.coordinate_info)
        self.latitude=self.coordinate_info.json()["data"][0]["latitude"]
        self.longitude=self.coordinate_info.json()["data"][0]["longitude"]
        self.postal_code=self.coordinate_info.json()["data"][0]["postal_code"]
        
    def connection_error(self):
        message.showerror("Connection time out", "Please check your internet connection. \nCan't reach the server")
        
        
    def get_weather(self,):
        try:
            self.get_location()
        except:
            try:
                self.get_location2()
            except:
                self.connection_error()
        try:
            self.url=Places.get_url+"lat="+ str(self.latitude)+"&lon="+ str(self.longitude)+"&appid="+ Places.api_key    #complete api call url using api key
        except:
            #self.connection_error()
            pass
            
        #get the weather information
        self.wea=requests.get("https://"+ self.url)
        self.condition=self.wea.json()["weather"][0]["description"]
        self.temperature=self.wea.json()["main"]["temp"]
        self.feels_like=self.wea.json()["main"]["feels_like"]
        self.temp_min=self.wea.json()["main"]["temp_min"]
        self.temp_max=self.wea.json()["main"]["temp_max"]
        self.pressure=self.wea.json()["main"]["pressure"]
        self.humidity=self.wea.json()["main"]["humidity"]
        self.sea_level=self.wea.json()["main"]["sea_level"]
        self.ground_level=self.wea.json()["main"]["grnd_level"]
        self.visibility=self.wea.json()["visibility"]
        self.wind_speed=self.wea.json()["wind"]["speed"]
        self.wind_temp=self.wea.json()["wind"]["deg"]
        self.cloudiness=self.wea.json()["clouds"]["all"]
        
class Buttons:
    def __init__ (self, number, row, column):
        self.row =row
        self.column =column
        self.number =number
        self.count=number-1
        self.button_photo=ImageTk.PhotoImage(Image.open("pics\\icons8-plus-50.png"))
        self.button= Button(frame1, image=self.button_photo, width="145",height="170", command = lambda button= 1+self.count: com(button))
        self.button.grid(column=column, row=row)
        #self.label= Label(frame1, text=button_texts[self.count])
        #self.label.grid(column=column, row=row)
        
    #def text(self, text1):
        #self.label.configure(text= text1)
    
    def image(self, photo):
        self.button.configure(image=photo)
        
        
        
        
        
    

        
#Frontend





#first window
#root=Tk()
#root.title("ATMOSAPP")
#root.geometry("700x700")
#Welcome_image= ImageTk.PhotoImage(Image.open("C:\\Users\\USER\\Downloads\\light-1282314_1920.jpg"))
#Image_label= Label(root, image=Welcome_image)
#Image_label.place()

#second window
start=Tk()
start.title("ATMOSAPP")
start.iconbitmap("C:\\Users\\USER\Desktop\\python softwares\\WEATHER APP\\pics\\cloud_weather.ico")
start.geometry("700x700")
start.resizable(False, False)

background_photo=ImageTk.PhotoImage(Image.open("pics\\thunderstorm.jpg"))


#Import weather icons
thunder_pic=ImageTk.PhotoImage(Image.open("pics\\thunderstorm.png"))        
cloudy_pic=ImageTk.PhotoImage(Image.open("pics\\cloudy.png"))        
clear_pic=ImageTk.PhotoImage(Image.open("pics\\clear sky.png"))        
drizzle_pic=ImageTk.PhotoImage(Image.open("pics\\drizzle.png"))        
rainy_pic=ImageTk.PhotoImage(Image.open("pics\\rainy.png"))        
misty_pic=ImageTk.PhotoImage(Image.open("pics\\misty.png"))        
snow_pic=ImageTk.PhotoImage(Image.open("pics\\snow.png"))        
default=ImageTk.PhotoImage(Image.open("pics\\default.png"))        


image_label= Label(start, image=background_photo)
image_label.pack()     #First pack the image before placing the frame on the window

frame1= Frame(start, )
frame1.place(x=125, y=80)
    
def check():
    global description
    global thunderstorm
    global clouds
    global atmosphere
    global drizzle 
    global rain
    global clear_sky
    global snow
    global thunder_pic
    global cloudy_pic
    global clear_pic
    global drizzle_pic
    global rainy_pic
    global misty_pic
    global snow_pic
      
    
    if description in thunderstorm:
        pic=thunder_pic
    elif description in clouds:
        pic=cloudy_pic
    elif description in atmosphere:
        pic=misty_pic
    elif description in drizzle:
        pic=drizzle_pic
    elif description in rain:
        pic=rainy_pic
    elif description in clear_sky:
        pic=clear_pic
    elif description in snow:
        pic=snow_pic
    else:
        pic=default
    
    return pic
        
 
    
    
    
    
    
    
def startup():
    global button_list
    count=0
    for row in range(1,4):
        for col in range (1,4):
            button_list[count]= Buttons(count+1, row, col)
            count=count+1
            print(str(row) + str(col))
        
        
def icons():    #A simple function that is used to place appropraite image icons on each button based on the description attached to that button and read from a file
    global button_list
    global description
    icon=""
    with open ("data\\weather_description.txt","r") as data:
        icon=data.read()
    count=0
    for x in icon.split("\n"):
        if x=="":
            continue
        if x=="nothing":
            pass
        else:
            description=x
            button_list[count].image(check())
        print(x)
        count=count+1
startup()
icons()
            
            
            

def clear():
    global button_text1
    global button_text2
    global button_text3
    global button_text4
    global button_text5
    global button_text6
    global button_text7
    global button_text8
    global button_text9
    global weather_object1
    global weather_object2
    global weather_object3
    global weather_object4
    global weather_object5
    global weather_object6
    global weather_object7
    global weather_object8
    global weather_object9
    global weather_info1
    global weather_info2
    global weather_info3
    global weather_info4
    global weather_info5
    global weather_info6
    global weather_info8
    global weather_info9
    global weather_status
    descriptions="nothing\nnothing\nnothing\nnothing\nnothing\nnothing\nnothing\nnothing\nnothing\n"
    
    button_text1= None
    button_text2= None
    button_text3= None
    button_text4= None
    button_text5= None
    button_text6= None
    button_text7= None
    button_text8= None
    button_text9= None
    weather_object1=None
    weather_object2=None
    weather_object3=None
    weather_object4=None
    weather_object5=None
    weather_object6=None
    weather_object7=None
    weather_object8=None
    weather_object9=None
    weather_info1=None
    weather_info2=None
    weather_info3=None
    weather_info4=None
    weather_info5=None
    weather_info6=None
    weather_info7=None
    weather_info8=None
    weather_info9=None
    weather_status=[" "," "," "," "," "," "," "," "," "]
    global weather_data

    startup()
    for obj in weather_data:
        with open ("data\\"+obj+".txt", "r+") as data:
            data.truncate(0)
    with open ("data\\weather_status.txt", "w") as data:
        data.write("False\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\n")
    
    with open ("data\\weather_description.txt", "w+") as data:
        data.write(descriptions)
        
    
    
    
        
def refresh():
    global weather_data
    global description
    global button_list
    
    
    for obj in weather_data:
        with open ("data\\"+obj+".txt", "r") as data:
            address=data.readline()
            print(address)
            address_list= [x for x in address.split("-")]
        print(address_list)
        
        if address==["None"] or address=="":
            continue 
        weather= Places(address_list[0], address_list[1], address_list[2], address_list[3])
        print(weather)
        weather.get_weather()
        print(weather.Address+"\n"+str(weather.pressure))
        weather_infos= StringVar()
        weather_infos.set(("{}\n\n\n\n Here's what the weather looks like today\n\
            \nWeather description: {}\
            \nActual temperature:  {}\
            \nTemp. Feels like:    {}\
            \nMinimum Temperature: {}\
            \nMaximum Temperature: {}\
            \nAir Pressure:        {}\
            \nHumidity:            {}\
            \nSea level:           {}\
            \nGround level:        {}\
            \nVisibility:          {}\
            \nWind Speed:          {}\
            \nWind temperature:    {}\
            \nLevel of Cloudiness: {}").format(address, weather.condition,weather.temperature,weather.feels_like,weather.temp_min,weather.temp_max,weather.pressure,weather.humidity,weather.sea_level,weather.ground_level,weather.visibility,weather.wind_speed,weather.wind_temp,weather.cloudiness))
    
        with open ("data\\"+obj+".txt", "w+") as data:
            data.write(weather_infos.get())
            
        description=weather.condition
        button_list[button-1].image(check())
        with open ("data\\weather_description.txt", "r") as data:
            data2=data.read()
            print(data2)
        lister=[]
        for x in data2.split("\n"):
            if not x=="":
                lister.append(x)
        with open ("data\\weather_description.txt", "w+") as data:
            lister[button-1]=description
            data2=""
            for item in lister:
                data2+=item+"\n"
            data.write(data2)
    
            
        
    
        
            
        
    
refresh_image=ImageTk.PhotoImage(Image.open("pics\\refresh.png"))        
refresh_button=Button(frame1,image=refresh_image, command= refresh)
refresh_button.grid(column=2, row=7)
clear_all= Button(frame1, text="CLEAR ALL DATA", command= clear)
clear_all.grid(column=3, row=7)
        




        
        

    

def fill_form(button):
    global weather_status
    global GUI_address
    global weather_objects
    global weather_infos
    global button_list
    global description
    GUI_address= StringVar()
    GUI_address.set(dialog.askstring("Type in location", "To add a new weather location, type in your locations complete address in the following format \nLocal Address-city-state-country\n\nMake sure you address is valid to avoid errors"))
    address_list= [x for x in GUI_address.get().split("-")]
    print(address_list)
    print(button)
    if address_list==["None"]:
        return 
    weather_objects[button-1]= Places(address_list[0], address_list[1], address_list[2], address_list[3])
    print(weather_objects[button-1])
    weather_objects[button-1].get_weather()
    print(weather_objects[button-1].Address+"\n"+str(weather_objects[button-1].pressure))
    weather_infos[button-1]= StringVar()
    weather_infos[button-1].set(("{}\n\n\n\n Here's what the weather looks like today\n\
            \nWeather description: {}\
            \nActual temperature:  {}\
            \nTemp. Feels like:    {}\
            \nMinimum Temperature: {}\
            \nMaximum Temperature: {}\
            \nAir Pressure:        {}\
            \nHumidity:            {}\
            \nSea level:           {}\
            \nGround level:        {}\
            \nVisibility:          {}\
            \nWind Speed:          {}\
            \nWind temperature:    {}\
            \nLevel of Cloudiness: {}").format(GUI_address.get().capitalize(), weather_objects[button-1].condition,weather_objects[button-1].temperature,weather_objects[button-1].feels_like,weather_objects[button-1].temp_min,weather_objects[button-1].temp_max,weather_objects[button-1].pressure,weather_objects[button-1].humidity,weather_objects[button-1].sea_level,weather_objects[button-1].ground_level,weather_objects[button-1].visibility,weather_objects[button-1].wind_speed,weather_objects[button-1].wind_temp,weather_objects[button-1].cloudiness))
    
    with open ("data\\"+weather_data[button-1]+".txt", "w+") as data:
        data.write(weather_infos[button-1].get())
    weather_status[button-1]="True"
    print(weather_status)
    status=""
    for y in weather_status:
            status+=y+"\n"
    print("This is status "+status)
    with open ("data\\weather_status.txt", "w+") as data:
        data.write(status)
    description=weather_objects[button-1].condition
    print(description)
    
    button_list[button-1].image(check())
    
    with open ("data\\weather_description.txt", "r") as data:
        data2=data.read()
        print(data2)
        lister=[]
        for x in data2.split("\n"):
            if not x=="":
                lister.append(x)
    with open ("data\\weather_description.txt", "w+") as data:
        lister[button-1]=description
        data2=""
        for item in lister:
            data2+=item+"\n"
        data.write(data2)

    print(weather_infos[button-1].get())
    
    

def show_form(button):
    data2=""
    global weather_infos
    global weather_data
    weather_infos[button-1]=StringVar()
    with open("data\\"+weather_data[button-1]+".txt",) as data:
        data2=data.read()
    weather_infos[button-1].set(data2)
    note=str(weather_infos[button-1].get())
    message.showinfo(title="Today's weather",message=note )
    
    
    
    
def com(button):
    global weather_infos
    global weather_status
    
    data2=[]
    
    with open ("data\\weather_status.txt") as data:
        data2=[x for x in data.read().split("\n")]
        data2.pop()
    weather_status=data2
    print(weather_status)
    if weather_status[button-1]=="True":
        show_form(button)
    else:
        fill_form(button)
        
        
        
        
        ""
        
        
        
        
        
        
        
start.mainloop()