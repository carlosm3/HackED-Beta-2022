from flask import Flask, render_template, request
from pywizlight import wizlight, PilotBuilder, discovery
# import avgRGBv2
import asyncio
import nest_asyncio
import cv2, time, pyautogui
import keyboard as k
import numpy as np
from threading import Thread
# from bulbInterface import lightbulb as lb

app = Flask(__name__, template_folder='templates', static_folder='static')

# loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# bbox = (0, 0, 1920, 1080)
# lt1 = lb("192.168.137.105",(0, 0, 0), 0)
#light = wizlight("192.168.137.105")

#light.turn_on(PilotBuilder(rgb=(0, 0, 0), brightness=255, warm_white=0, cold_white=0))

def calculateAvg(ar,ag,ab,count):
    r = round(ar/count)
    g = round(ag/count)
    b = round(ab/count)
    return (r,g,b)


# def convertHEXtoRGB(value):
#     if (value):
#         value = value.lstrip('#')
#         lv = len(value)
#         return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


@app.route('/', methods=['GET', 'POST'])
@app.route('/playground', methods=['GET', 'POST'])
def playground():
    light1 = lightbulb("192.168.137.105",(request.args.get('r'),request.args.get('g'),request.args.get('b')),request.args.get('bright'),request.args.get('cold'),request.args.get('warmth'))
    #light1.turnOn()
    '''{"r": request.args.get('r'), "g": request.args.get('g'), "b": request.args.get('b'), "a": request.args.get('a'), "cold": request.args.get('cold'), "warmth": request.args.get('warmth')}'''
    
    '''
    if (values["r"] and values["g"] and values["b"]):
        rgb = (int(values["r"]), int(values["g"]), int(values["b"]))
        warmth = int(values['warmth'])
        cold = int(values['cold'])
        brightness = int(float(values['a'])) * 255

        try:
            nest_asyncio.apply(loop.run_until_complete(light.turn_on(PilotBuilder(rgb=rgb, brightness=brightness, warm_white=warmth, cold_white=cold))))
        except Exception as e:
            print(e)'''
        

    return render_template('playground.html', title='Playground')

@app.route('/stream', methods=['GET', 'POST'])
def setup():
    values = {"x1": request.args.get('x1'), "y1": request.args.get('y1'), "x2": request.args.get('x2'), "y2": request.args.get('y2')}
    # if (values["x1"]):
    #     bbox = (int(values["x1"]), int(values["y1"]), int(values["x2"]), int(values["y2"]))
    #     print(bbox)
    #     # image = pyautogui.screenshot(bbox)
    #     image1 = pyautogui.screenshot(region=(bbox))
    #     image = cv2.cvtColor(np.array(image1), cv2.COLOR_RGB2BGR)
    #     start = time.time()
    #     ab = ag = ar = count = 0
    #     lum = 0

    #     while True:
    #         #cv2.imshow("Unironic Image Name", image)
    #         b,g,r = image.mean(axis=(0,1))
    #         end = time.time()
    #         if end < start + 2:
    #             ab += b
    #             ag += g
    #             ar += r
    #             count += 1
    #         else:
    #             rgb = calculateAvg(ar,ag,ab,count)
    #             ab = ag = ar = count = 0
    #             print(rgb)
    #             try:
    #                 loop.run_until_complete(light.turn_on(PilotBuilder(rgb=rgb, brightness=255, warm_white=0, cold_white=0)))
    #             except Exception as e:
    #                 print(e)
    #             start = time.time()
    #         # time.sleep(1/40)

    #         image = pyautogui.screenshot()
    #         image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    #     cv2.destroyAllWindows()
    return render_template('stream.html', title='Stream')

class lightbulb:
    def __init__(self, ip, rgb, bright, cold=0, warm=0):
        self.ip = wizlight(ip)
        self.cold = cold
        self. warm = warm
        self.rgb = rgb
        self.bright = bright
    
    def turnOn(self):
        loop.run_until_complete(changeLight(self))
    
    def turnOff(self):
        loop.run_until_complete(off(self))
    
    def changeRGB(self,newrgb):
        self.rgb = newrgb
    
    def RGBScale(self,newrgb):
        self.rgb = newrgb
        self.cold = round(sum(newrgb)/21)
        self.bright = max(newrgb)
        loop.run_until_complete(changeLight(self))
    
    def changeCold(self,newCold):
        self.cold = newCold
        loop.run_until_complete(changeLight(self))
    
    def changeBright(self,newBright):
        self.bright = newBright
        loop.run_until_complete(changeLight(self))
    
    def changeWarm(self,newWarm):
        self.warm = newWarm
        loop.run_until_complete(changeLight(self))

async def changeLight(light):
    await (light.ip).turn_on(PilotBuilder(rgb = light.rgb, brightness = light.bright, warm_white = light.warm, cold_white = light.cold))

async def off(light):
    await (light.ip).turn_off()

if __name__ == '__main__':
    app.run(debug=True)