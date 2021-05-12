import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import cv2 as cv
from uuid import uuid4
from fire_detect_opencv import fcm

PROJECT_ID = "cap-aacc4"
cred = credentials.Certificate(
    "/home/pi/2021_cap/fire_detect_opencv/cert_key/cap-aacc4-firebase-adminsdk-qc42b-169c65d5e2.json")
default_app = firebase_admin.initialize_app(cred, {'storageBucket': f"{PROJECT_ID}.appspot.com"})
# 버킷은 바이너리 객체의 상위 컨테이너. 버킷은 Storage에서 데이터를 보관하는 기본 컨테이너.
bucket = storage.bucket()  # 기본 버킷 사용
fireStatus = False
fireCascade = cv.CascadeClassifier('/home/pi/2021_cap/fire_detect_opencv/fire.xml')
# 카메라 정보 받아오기 pi카메라는 -1
capture = cv.VideoCapture(-1)
# 비디오 코덱설정
fourcc = cv.VideoWriter_fourcc(*'XVID')
picture_directory = "/home/pi/2021_cap/fire_detect_opencv/detect_history/pictures/"
video_directory = "/home/pi/2021_cap/fire_detect_opencv/detect_history/videos/"

capture_time = datetime.datetime.now()


def observe():
    print('불꽃 감시 중..')
    global fireStatus, capture_time
    # 키 입력이 없을 시 33ms마다 프레임 받아와서 출력
    while cv.waitKey(33) < 0:
        ret, frame = capture.read()
        fire = fireCascade.detectMultiScale(frame, 1.2, 5)
        cv.imshow("LiveCam", frame)
        for (x, y, w, h) in fire:
            now = datetime.datetime.now()
            str_now=str(now).strftime('%Y-%m-%d %H:%M:%S')
            print('불꽃 감지!! (' + str_now + ')')
            fcm.sendMessage(str_now)
            # 탐지한 불꽃에 사각형으로 표시
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            fireStatus = True
            capture_time = savePhoto(now, frame)
            filename = str(capture_time.strftime('%Y-%m-%d %H:%M:%S')) + '.jpg'
            uploadPhoto(filename)
            break
        if fireStatus == True:
            break


def savePhoto(now, frame):
    cv.imwrite(picture_directory + str(now.strftime('%Y-%m-%d %H:%M:%S')) + ".jpg", frame)
    print('사진 저장 완료 (' + str(now.strftime('%Y-%m-%d %H:%M:%S')) + ".jpg)")
    return now


def saveVideo():
    print('녹화 시작')
    global fireStatus
    start_time = datetime.datetime.now()
    while (capture.isOpened()):
        now = datetime.datetime.now()
        ret, frame = capture.read()
        out.write(frame)
        if start_time + datetime.timedelta(seconds=5) <= now:
            fireStatus = False
            print('녹화 종료')
            print('영상 저장 완료 (' + capture_time.strftime('%Y-%m-%d %H:%M:%S') + ".avi)")
            break


def uploadPhoto(file):
    blob = bucket.blob('detect_history/pictures/' + file)
    # new token, metadata 설정
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token}  # access token 필요
    blob.metadata = metadata

    blob.upload_from_filename(filename='/home/pi/2021_cap/fire_detect_opencv/detect_history/pictures/' + file)
    print("사진 업로드 완료")


def uploadVideo(file):
    blob = bucket.blob('detect_history/videos/' + file)
    # new token, metadata 설정
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token}  # access token 필요
    blob.metadata = metadata

    blob.upload_from_filename(filename='/home/pi/2021_cap/fire_detect_opencv/detect_history/videos/' + file)
    print("영상 업로드 완료")


while True:
    if fireStatus == False:
        observe()
    else:
        out = cv.VideoWriter(video_directory + capture_time.strftime('%Y-%m-%d %H:%M:%S') + '.avi', fourcc, 20.0,
                             (640, 480))
        saveVideo()
        uploadVideo(capture_time.strftime('%Y-%m-%d %H:%M:%S') + '.avi')

capture.release()
out.release()
cv.destroyAllWindows()
