import glob
import random
import os
import subprocess
import signal
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def uploadTXT():
    rawtext = ""
    print "got to the function"
    with open(glob.fn, 'r') as f:
    	for line in f:
            print line
            rawtext += line.rstrip() + "  "
    os.remove(glob.fn)
    text = []
    print "before generating colors"
    for chr in rawtext:
       r1 = int(random.random() * 256)
       r2 = int(random.random() * 256)
       r3 = int(random.random() * 256)
       text.append((chr, (r1, r2, r3)))
    print "generated colors"
    font = ImageFont.truetype("/usr/share/fonts/Perfect DOS VGA 437.ttf", 16)
    all_text = ""
    for text_color_pair in text:
        t = text_color_pair[0]
        all_text = all_text + t

    print(all_text)
    width, ignore = font.getsize(all_text)
    print(width)

    im = Image.new("RGB", (width + 10, 16), "black")
    draw = ImageDraw.Draw(im)

    x = 0;
    for text_color_pair in text:
        t = text_color_pair[0]
        c = (0, 153, 204)
        print("t=" + t + " " + str(c) + " " + str(x))
        draw.text((x, 0), t, c, font=font)
        x = x + font.getsize(t)[0]

    im = im.rotate(180)
    im.save("text.ppm")
    glob.fn = "text.ppm"
    uploadPPM()

def uploadPPM():
    stopLEDs()
    str = ("./led-matrix -r 16 -c 3 -D 2 " + glob.fn)
    runLEDs(str)

def uploadImage(image=None):
    stopLEDs()
    if image:
        str = ("./led-image-viewer " + image + " -r 16 -c 3")
    else:
        str = ("./led-image-viewer " + glob.fn + " -r 16 -c 3")
    runLEDs(str)

def stopLEDs():
    if glob.process != None:
        glob.process.stdin.write("\n")
        glob.process.terminate()

def runLEDs(str):
    glob.process = subprocess.Popen("exec " + str, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

