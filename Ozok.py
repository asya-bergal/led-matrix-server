import urllib
import json
import leds
import time
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def Weather ():
    font = ImageFont.truetype("/usr/share/fonts/pixelmix.ttf", 8)

    widthHello, ignore = font.getsize('Random Hall')
    welcome = Image.new('RGB',(widthHello + 32,16),'black')
    drawWelcome = ImageDraw.Draw(welcome).text((0,0),'Welcome to',(256,126,0),font=font)
    drawWelcome = ImageDraw.Draw(welcome).text((0,8),'Random Hall',(256,126,0),font=font)
    
    ozok = Image.open('ozok2.png')
    welcome.paste(ozok, (widthHello + 1, 0))

    welcome = welcome.rotate(180)
    welcome.save('welcome.ppm') 
    leds.uploadPPM("welcome.ppm")

    raw_input()

if  __name__ =='__main__':
    while(True):
        Weather()
        time.sleep(600)

