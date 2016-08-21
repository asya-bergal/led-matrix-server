import datetime
import urllib
import json
import leds
import time
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

eventMessage = ""
eventMessage2 = ""
eventMessage3 = ""

def CPW (day,hour,minute):
	intro = "Next Event In Random Hall:"
	intro2 =""

	global eventMessage
	global eventMessage2
	global eventMessage3

	eventMessage = ""
	eventMessage2 = ""
	eventMessage3 = ""

	if(day == 16):
		if(hour < 16 or (hour == 16 and minute <=17)):
			eventMessage = "Knitting Circle Taqueria 14:17 - 16:17 BMF "
			print('hoi;')
		elif(hour <19 or (hour == 19 and minute <=17)):
			eventMessage = "Clam Olympics 18:17 - 19:17 Clam "
			print('dfs')
		elif (hour <20 or (hour == 20 and minute <=17)):
			eventMessage = "Chemistry and Cake w/ LN2 ice cream continued 19:17 - 20:17 Pecker "
		elif(hour <23 or (hour == 23 and minute <=59)):
			eventMessage =  "BBQ and Spinning on the Roofdeck w/ Giga Curry 21:47 - 24:47 Black Hole+Roofdeck "
			eventMessage2 = "Five SCPs at Freddy's 22:47 - 24:47 Destiny "
			eventMessage3 = "Crazy Cat Lady Make-A-Thon 23:47 - 24:47 Loop "

	if(day == 17):
		if (hour == 0 and minute <=47):
			eventMessage = "BBQ and Spinning on the Roofdeck w/ Giga Curry 21:47 - 24:47 Black Hole+Roofdeck"
			eventMessage2 = "Five SCPs at Freddy's 22:47 - 24:47 Destiny"
			eventMessage3 = "Crazy Cat Lady Make-A-Thon 23:47 - 24:47 Loop"
		elif (hour<12 or (hour == 12 and minute <=17)):
			eventMessage = "Nerf Chess 11:17 - 12:17 Foo"
		elif (hour<14 or (hour == 14 and minute <=47)):
			eventMessage = "Physics and Coffee 2:17 PM - 16:17 Pecker"
			eventMessage2 = "Dumpling Hylomorphisms	12:17 PM - 2:47 PM Black Hole"
		elif (hour<14 or (hour == 14 and minute <=17)):
			eventMessage = "Physics and Coffee 2:17 PM - 16:17 Pecker"
			eventMessage2 = "Rocky Horrible's Nerdy Singalong Blog w/ LN2 ice cream	3:47 PM - 17:47	AIW "
		elif (hour<17 or (hour == 17 and minute <=47)):
			eventMessage = "Rocky Horrible's Nerdy Singalong Blog w/ LN2 ice cream	3:47 PM - 17:47	AIW "
			eventMessage2 = "mitBEEF 17:00 - 18:00 Foo	"
		elif (hour<18 or (hour == 18 and minute <=1)):	
			eventMessage = "mitBEEF	17:00 - 18:00 Foo"
			eventMessage2 = "Math and Tea 17:47 - 20:47 Pecker "
		elif (hour<20 or (hour == 20 and minute <=47)):
			eventMessage = "Math and Tea 17:47 - 20:47 Pecker	"
		elif (hour<22 or (hour == 22 and minute <=17)):
			eventMessage = "Star Trek on Infinite Loop 20:47 - 22:47 Loop"
			eventMessage2 = "Duct Tape Construction w/ Cookies by Committee 21:47 - 11:47 PM	Black Hole"
		elif (hour<23 or (hour == 23 and minute <=47)):
			eventMessage = "Duct Tape Construction w/ Cookies by Committee 21:47 - 11:47 PM	Black Hole"
			eventMessage2 = "PowerPoint Karaoke + Latte Art 10:47 PM - 12:47 PM	Foo	"
		elif (hour<23 or (hour == 23 and minute <=59)):
			eventMessage = "PowerPoint Karaoke + Latte Art 22:47 - 24:47	Foo	"

	if(day == 18):
		if (hour == 0 and minute <= 47):
			eventMessage = "PowerPoint Karaoke + Latte Art 10:47 - 24:47 Foo"
		elif (hour< 11 or (hour == 11 and minute <= 47)):
			eventMessage = "Saturday Morning Breakfast Cartoons w/ Ceiling Tile Painting	9:47 AM - 11:47 AM	Loop"
		elif (hour< 13 or (hour == 13 and minute <= 17)):
			eventMessage = "Epic Mealtime of Destiny	11:47 - 13:17 Destiny"
		elif (hour< 15 or (hour == 15 and minute <= 47)):
			eventMessage = "Carbonated Fruit!	13:47 - 15:47 Black Hole"
		elif (hour< 17 or (hour == 17 and minute <= 17)):
			eventMessage = "Storytime with Cruft w/ Liquid Nitrogen Ice Cream and Truffles	15:17 - 17:17 Foo	"
			eventMessage2 = "Random Plays Randomly + Smash!	16:17 - 17:47 AIW"
		elif (hour< 17 or (hour == 17 and minute <= 47)):
			eventMessage = "Random Plays Randomly + Smash!	16:17 - 17:47 AIW"
		elif (hour< 21 or (hour == 21 and minute <= 47)):
			eventMessage = "InterDorm Potluck Event	19:30 - 21:47	Foo	"
			eventMessage2 = "Chainmail w/ Experimental Smoothies	20:47 - 21:47 Destiny"
		elif (hour< 23 or (hour == 23 and minute <= 59)):
			eventMessage = "Pecker Board Game Night + Teach You Tichu 21:47 - 24:47	Pecker	"
			eventMessage2 = "(Almost) Life-Sized Settlers of Catan 21:47 - 24:47	Foo	"

	if (day == 19):
		if (hour == 0 and minute <= 47):
			eventMessage = "Pecker Board Game Night + Teach You Tichu	21:47 - 24:47 Pecker"
			eventMessage2 = "(Almost) Life-Sized Settlers of Catan	21:47 - 24:47 Foo"
		else:
			eventMessage = "Tea Time with Teddy	11:47 - 12:47 BMF"

	print("1" + eventMessage + "\n 2" + eventMessage2 + "\n 3" + eventMessage3)  

	font = ImageFont.truetype("/usr/share/fonts/pixelmix.ttf", 8)
	widthIntro, ignore = font.getsize(intro)
	widthMessage, ignore = font.getsize(intro2 + eventMessage+eventMessage2+eventMessage3)
	currentEvents = Image.new("RGB", (widthMessage + 10, 16), "black")
	introText = [("Next event in   ",(127,63,0)), (eventMessage, (118,13,13)) ]
	text = [("R",(127,0,0)), ("a",(127,63,0)),("n",(127,127,0)),("d",(14,86,60)),("o",(10,81,102)),("m",(79,0,127)), (" Hall: ",(127,63,0)), (eventMessage2,(53,45,103)),(eventMessage3,(0,101,44))]
	x = 0
	for element in introText:
		drawIntro = ImageDraw.Draw(currentEvents).text((x,0),element[0], element[1], font=font)
		x = x + font.getsize(element[0])[0]
	x = 0
	count = 0
	for element in text:
		count += 1
		drawCurrentEvents = ImageDraw.Draw(currentEvents).text((x,8),element[0],element[1],font=font)
		x = x + font.getsize(element[0])[0]
		if count == 7:
			x = x + font.getsize("Next event in   ")[0] - font.getsize("Random Hall: ")[0]
	currentEvents = currentEvents.rotate(180)
	currentEvents.save("currentEvents.ppm")
	leds.uploadPPM("currentEvents.ppm")

def Weather ():
    try:
        weatherURL = urllib.URLopener().retrieve("http://api.wunderground.com/api/efb7f164a8ddf6f5/conditions/forecast/q/pws:KMACAMBR9.json","weather.json")
        with open("weather.json",'r') as weatherData:
            weather = json.load(weatherData)
    except:
        return None
    current = "Currently: " + str(weather["current_observation"]["temp_c"]) + u'\N{DEGREE SIGN}' + "C | " + str(weather["current_observation"]["weather"])
    current1 = current.split("|")[0] + "|"
    current2 = current.split("|")[1]
    forecastFor = "Forecast for " + str(weather["forecast"]["simpleforecast"]["forecastday"][0]["date"]["weekday_short"]) + ": "
    forecastHi = "Hi:" + str(weather["forecast"]["simpleforecast"]["forecastday"][0]["high"]["celsius"]) + u'\N{DEGREE SIGN}' + "C "
    forecastLo = "Lo:" + str(weather["forecast"]["simpleforecast"]["forecastday"][0]["low"]["celsius"]) + u'\N{DEGREE SIGN}' + "C "
    forecastConditions = str(weather["forecast"]["simpleforecast"]["forecastday"][0]["conditions"])
    text = [(forecastFor ,(127,63,0)),(forecastHi,(100,4,10)),(forecastLo,(35,82,90)),(forecastConditions,(101,80,80))]
    forecast = forecastFor + forecastHi + forecastLo + forecastConditions
    font = ImageFont.truetype("/usr/share/fonts/pixelmix.ttf", 8)
    widthCurrent, ignore = font.getsize(current)
    widthForecast, ignore = font.getsize(forecast)

    currentWeather = Image.new("RGB", (widthForecast + 10, 16), "black")
    drawCurrentWeather = ImageDraw.Draw(currentWeather).text((0,0),current1, (127,63,0), font=font)
    drawCurrentWeather = ImageDraw.Draw(currentWeather).text((font.getsize(current1)[0],0),current2, (101,80,80), font=font)

    x = 0
    for element in text:
        drawCurrentForecast = ImageDraw.Draw(currentWeather).text((x,8),element[0],element[1],font=font)
        x = x + font.getsize(element[0])[0]
    currentWeather = currentWeather.rotate(180)
    currentWeather.save("currentWeather.ppm")

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

def updateWeather():
    leds.uploadPPM("currentWeather.ppm")

if  __name__ =='__main__':
	while (True):
	    Weather()
            for i in range(50):
                now = datetime.datetime.now()
                CPW(now.day,now.hour + 1,now.minute)
                sleepTime = (len("Random Hall:     ") + len(eventMessage2) + len(eventMessage3))/5 +6
		time.sleep(sleepTime)
		updateWeather()
		time.sleep(10)
