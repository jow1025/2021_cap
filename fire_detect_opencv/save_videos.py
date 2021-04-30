import cv2 as cv
import numpy as np
import datetime

fire = False
fireCascade = cv.CascadeClassifier('/home/pi/2021_cap/fire_detect_opencv/fire.xml')
#카메라 정보 받아오기 pi카메라는 -1
capture = cv.VideoCapture(-1)
#비디오 코덱설정
fourcc = cv.VideoWriter_fourcc(*'XVID')
directory="/home/pi/2021_cap/fire_detect_opencv/detected_record/videos/"


def observe():
    print('불꽃 감시 중..')
    global fire
    #키 입력이 없을 시 33ms마다 프레임 받아와서 출력
    while cv.waitKey(33) < 0:
        ret, frame = capture.read()
        fire=fireCascade.detectMultiScale(frame,1.2,5)
        cv.imshow("VideoFrame", frame)
        for(x,y,w,h) in fire:
            #탐지한 불꽃에 사각형으로 표시
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
        cv.imshow('RecordFrame',frame)
        out.write(frame)
        if start_time + datetime.timedelta(seconds=5) <= now:
            fire=False
            break
        
while True:
    #print(fire)
    if fire==False:
        observe()
    else:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        out = cv.VideoWriter(directory+str(now)+'.avi',fourcc,20.0,(640,480))
        saveVideo()


capture.release()
out.release()
cv.destroyAllWindows()


