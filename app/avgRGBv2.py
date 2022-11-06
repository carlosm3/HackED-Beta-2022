import cv2, time, pyautogui
import keyboard as k
import numpy as np
from threading import Thread
from bulbInterface import lightbulb as lb

lt1 = lb("192.168.137.105",(0, 0, 0), 0)
#ip_bulb = "192.168.137.105"

'''
def convertHEXtoRGB(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def defineip(ip):
    global ip_bulb
    ip_bulb = ip
'''

def calculateAvg(ar,ag,ab,count):
    r = round(ar/count)
    g = round(ag/count)
    b = round(ab/count)
    return (r,g,b)

def RGBt(rgb):
    lt1.RGBScale(rgb)

def main():
    #x,y = pyautogui.size()
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    start = time.time()
    ab = ag = ar = count = 0
    lum = 0

    while True:
        #cv2.imshow("Unironic Image Name", image)
        b,g,r = image.mean(axis=(0,1))
        end = time.time()
        if end < start + 2:
            ab += b
            ag += g
            ar += r
            count += 1
        else:
            rgb = calculateAvg(ar,ag,ab,count)
            ab = ag = ar = count = 0
            sendRGB = Thread(target = RGBt(rgb))
            sendRGB.start()
            start = time.time()
        time.sleep(1/40)

        if k.is_pressed('b'):
            lum += 10
            if lum >= 255:
                lum = 255
            lt1.changeBright(lum)
        elif k.is_pressed('v'):
            lum -= 10
            if lum <= 0:
                lum = 0
            lt1.changeBright(lum)    
        elif k.is_pressed("q"):
            break

        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.destroyAllWindows()

t1 = Thread(target = main())
t1.start()
