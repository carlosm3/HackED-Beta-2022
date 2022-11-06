from threading import Thread
import cv2, time, asyncio
from bulbInterface import lightbulb as lb

lt1 = lb("192.168.137.105",(0, 0, 0), 0)

def calculateAvg(ar,ag,ab,count):
    r = round(ar/count)
    g = round(ag/count)
    b = round(ab/count)
    return (r,g,b)
def RGBt(rgb):
    lt1.changeRGB(rgb)

def main():
    vid = cv2.VideoCapture("trial.mp4")
    if vid.isOpened() == False:
        print("Error opening the video file! / video file not found!")
        exit(0)
    else:
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
                    rgb = calculateAvg(ar,ag,ab,count)
                    ab = ag = ar = count = 0
                    t2 = Thread(target = RGBt(rgb))
                    t2.start()
                    start = time.time()
                time.sleep(1/40)
            else:
                break
            if cv2.waitKey(1) == ord('q'):
                break
        vid.release()
        cv2.destroyAllWindows()
t1 = Thread(target = main())
t1.start()

