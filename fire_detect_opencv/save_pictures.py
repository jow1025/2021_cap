import cv2 as cv
import numpy as np
import datetime

fireCascade=cv.CascadeClassifier('/home/pi/2021_cap/fire_detect_opencv/fire.xml')
#카메라 정보 받아오기 pi카메라는 -1
capture = cv.VideoCapture(-1)
#카메라 설정(너비,폭)
#capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
#capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
directory="/home/pi/2021_cap/fire_detect_opencv/detected_record/pictures/"
start_time=datetime.datetime.now()
capture_time=start_time-datetime.timedelta(seconds=1)

def savePhoto(now):
    print('Fire is detected : '+str(now))
    cv.imshow('Fire',frame)
    cv.imwrite(directory+str(now.strftime('%Y-%m-%d %H:%M:%S'))+".jpg",frame)
    return now

#키 입력이 없을 시 33ms마다 프레임 받아와서 출력
while cv.waitKey(33) < 0:
    ret, frame = capture.read()
    fire=fireCascade.detectMultiScale(frame,1.2,5)
    cv.imshow("VideoFrame", frame)
    for(x,y,w,h) in fire:
        #탐지한 불꽃에 사각형으로 표시
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        now = datetime.datetime.now()
        #1초마다 저장(이상하게 2-3초마다 저장됨?!)
        if capture_time+datetime.timedelta(seconds=1) <= now:
            capture_time=savePhoto(now)
        else:
            continue
            
        

capture.release()
cv.destroyAllWindows()