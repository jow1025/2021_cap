import cv2 as cv
import numpy as np
import datetime

#
fireCascade=cv.CascadeClassifier('/home/pi/code/fire.xml')

#카메라 정보 받아오기
capture = cv.VideoCapture(0)
#카메라 설정(너비,폭)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

#키 입력이 없을 시 33마다 프레임 받아와서 출력
while cv.waitKey(33) < 0:
    ret, frame = capture.read()
    fire=fireCascade.detectMultiScale(frame,1.2,5)
    cv.imshow("VideoFrame", frame)
    for(x,y,w,h) in fire:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        print('Fire is detected..!')
        cv.imshow('Fire',frame)
        #now = datetime.datetime.now()
        #time=str(now)
        #cv.imwrite(time,frame)

capture.release()
cv.destroyAllWindows()