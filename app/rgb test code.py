import cv2
import numpy as np
#import pyautogui
#cap = cv2.VideoCapture(0)
from PIL import ImageGrab
from time import time

def rgb_every_second(): # t_time defines how long the loop runs

    #loop_time = time()
    
    #ret,frame = cap.read()
    #cv2.imshow('frame',frame)
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    
    #anypxl = screenshot[100,100]
    #print(anypxl)

    avg_color_per_row = np.average(screenshot, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    return avg_color

    #cv2.imshow('outputfile',screenshot)
    #fps =1/(time()-loop_time)
    #print(f'FPS: {fps}')
    #loop_time = time()

#time.sleep(2)
#print("1",rgb_every_second())

def color_every_n_seconds(t_time):
    counter = 1
    r = 0
    g = 0
    b = 0
    initial_loop_time = time()
    loop_time = time()
    #print(loop_time)
    while loop_time <= t_time+initial_loop_time:

        loop_time = time()

        #ret,frame = cap.read()
        #cv2.imshow('frame',frame)
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        #anypxl = screenshot[100,100]
        #print(anypxl)

        avg_color_per_row = np.average(screenshot, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        b = b + avg_color[0]
        g = b + avg_color[1]
        r = r + avg_color[2]
        counter = counter + 1
        #return avg_color

        #cv2.imshow('outputfile',screenshot)
        #fps =1/(time()-loop_time)
        #print(f'FPS: {fps}')
        #loop_time = time()
        loop_time = time()
    avg_b = b/counter
    avg_g = g/counter
    avg_r = r/counter
    return [avg_r,avg_g,avg_b]

#while True:
#    print(color_every_n_seconds(3))