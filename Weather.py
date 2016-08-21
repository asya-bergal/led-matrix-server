
import urllib
import json
import leds
import time
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from time import strftime

brightness = 0.8

def Weather ():
    try:
        weatherURL = urllib.URLopener().retrieve("http://api.wunderground.com/api/efb7f164a8ddf6f5/conditions/forecast/q/pws:KMACAMBR9.json","weather.json")
        with open("weather.json",'r') as weatherData:
            weather = json.load(weatherData)
    except:
        return None
    current = "Currently: " + str(weather["current_observation"]["temp_c"]) + u'\N{DEGREE SIGN}' + "C | " + str(weather["current_observation"]["weather"])
    forecastFor = "Forecast for " + str(weather["forecast"]["simpleforecast"]["forecastday"][0]["date"]["weekday_short"]) + ": "
    forecastHi = "Hi:" + str(weather["forecast"]["simpleforecast"]["forecastday"][0]["high"]["celsius"]) + u'\N{DEGREE SIGN}' + "C "
    forecastLo = "Lo:" + str(weather["forecast"]["simpleforecast"]["forecastday"][0]["low"]["celsius"]) + u'\N{DEGREE SIGN}' + "C "
    forecastConditions = "| " + str(weather["forecast"]["simpleforecast"]["forecastday"][0]["conditions"])
    text = [(forecastFor ,(int(128*brightness),int(64*brightness),0)),(forecastHi,(int(100*brightness),int(4*brightness),int(10*brightness))),(forecastLo,(int(35*brightness),int(82*brightness),int(90*brightness))),(forecastConditions,(int(101*brightness),int(80*brightness),int(80*brightness)))]
    forecast = forecastFor + forecastHi + forecastLo + forecastConditions
    font = ImageFont.truetype("/usr/share/fonts/pixelmix.ttf", 8)
    widthCurrent, ignore = font.getsize(current)
    widthForecast, ignore = font.getsize(forecast)

    currentWeather = Image.new("RGB", (widthForecast + 10, 16), "black")
    drawCurrentWeather = ImageDraw.Draw(currentWeather).text((0,0),current, (int(127*brightness),int(63*brightness),0), font=font)
    currentForecast = Image.new("RGB",(widthForecast + 10, 16),"black")
    x = 0
    for element in text:
        drawCurrentForecast = ImageDraw.Draw(currentWeather).text((x,8),element[0],element[1],font=font)
        x = x + font.getsize(element[0])[0]
    currentWeather = currentWeather.rotate(180)    
    currentWeather.save("currentWeather.ppm")
    currentForecast = currentForecast.rotate(180)
    currentForecast.save("currentForecast.ppm")
    '''
    widthHello, ignore = font.getsize('Welcome to Random Hall')
    welcome = Image.new('RGB',(widthHello + 32,16),'black')
    drawWelcome = ImageDraw.Draw(welcome).text((0,0),'Welcome to Random Hall',(256,126,0),font=font)
    welcome = welcome.rotate(180)
    welcome.save('welcome.ppm') 
    leds.uploadPPM("welcome.ppm")
    '''
    leds.uploadPPM("currentWeather.ppm")
    print(current + "\n" + forecastFor + forecastHi + forecastLo + forecastConditions )

def Time ():
    for i in range(10):
        date = strftime("%H:%M:%S")

        font = ImageFont.truetype("/usr/share/fonts/pixelmix.ttf",10)
        widthTime, ignore = font.getsize(date)

        currentTime = Image.new("RGB", (widthTime + 100, 16), "black")
        drawCurrentTime = ImageDraw.Draw(currentTime).text((0,0),date,(int(35*brightness),int(83*brightness),int(90*brightness)),font=font)
        currentTime = currentTime.rotate(180)
        currentTime.save("currentTime.ppm")

        leds.uploadPPM("currentTime.ppm")

        print(date)

        time.sleep(10)

if  __name__ =='__main__':
    while(True):
        #Time()
        Weather()
        time.sleep(600)

