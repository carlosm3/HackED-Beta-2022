import asyncio
import time
from pywizlight import wizlight, PilotBuilder, discovery

loop = asyncio.get_event_loop()
#class for encapsulating data on a lightbulb and changing said data
#rgb has to be declared like this (red, green, blue), e..g (100,100,100)
#all values go from 0 to 255 except ip which is within ipv4 range
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
        loop.run_until_complete(changeLight(self))
    
    def changeCold(self,newCold):
        self.cold = newCold
        loop.run_until_complete(changeLight(self))
    
    def changeBright(self,newBright):
        self.bright = newBright
        loop.run_until_complete(changeLight(self))
    
    def changeCold(self,newCold):
        self.cold = newCold
        loop.run_until_complete(changeLight(self))

async def changeLight(light):
    await (light.ip).turn_on(PilotBuilder(rgb = light.rgb, brightness = light.bright, warm_white = light.warm, cold_white = light.cold))
async def off(light):
    await (light.ip).turn_off()
