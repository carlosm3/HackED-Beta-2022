import cv2
import numpy as np
import time
from bulbInterface import lightbulb as lb
import bulbInterface

lt1 = lb("192.168.137.105",(0, 0, 0),0)

vid = cv2.VideoCapture("trial.mp4")

if vid.isOpened() == False:
    print("Error opening the video file! / video file not found!")
    exit(0)

print("Dimensions:", vid.get(cv2.CAP_PROP_FRAME_WIDTH), vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("FPS:", vid.get(cv2.CAP_PROP_FPS))

start = time.time()
ab = ag = ar = count = 0
while vid.isOpened():
    check, frame = vid.read()
    if check == True:
        cv2.imshow("Frame:", frame)
        b,g,r = frame.mean(axis=(0,1))
        end = time.time()
        if end < start + 2:
            ab += b
            ag += g
            ar += r
            count += 1
        else:
            ar = round(ar/count)
            ag = round(ag/count)
            ab = round(ab/count)
            print(ar,ag,ab)
            lt1.changeRGB((ar, ag, ab))
            ab = ag = ar = count = 0
            start = time.time()
        time.sleep(1/40)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()


