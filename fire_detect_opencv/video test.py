import cv2 as cv
import numpy as np
import datetime

fire = False
fireCascade = cv.CascadeClassifier('/home/pi/2021_cap/fire_detect_opencv/fire.xml')
capture = cv.VideoCapture(-1)
fourcc = cv.VideoWriter_fourcc(*'XVID')



def observe():
    print('불꽃 감시 중..')
    global fire
    while cv.waitKey(33) < 0:
        ret, frame = capture.read()
        fire=fireCascade.detectMultiScale(frame,1.2,5)
        cv.imshow("VideoFrame", frame)
        for(x,y,w,h) in fire:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv.imshow("ObserveFrame", frame)
            fire=True
            break
        if fire==True:
            break

def saveVideo():
    print('불꽃 감지!! / 녹화 시작')
    global fire
    start_time = datetime.datetime.now()
    while(capture.isOpened()):
        now = datetime.datetime.now()
        ret, frame=capture.read()
        out.write(frame)
        cv.imshow('RecordFrame',frame)
        if start_time + datetime.timedelta(seconds=5) <= now:
            fire=False
            break
        
while True:
    #print(fire)
    if fire==False:
        observe()
    else:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        out = cv.VideoWriter(str(now)+'.avi',fourcc,20.0,(640,480))
        saveVideo()


capture.release()
out.release()
cv.destroyAllWindows()

