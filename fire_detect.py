import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import cv2 as cv
from uuid import uuid4
from pyfcm import FCMNotification

APIKEY="AAAAalMeKts:APA91bEiB12GcGeo5W0MmzOjjmcDiR9LwrVgUxmspbWpI4eZz0LjuFIuTVxnfCbqd_IoeMjVkqJt5BGe9V77gvzFLmfSj5utQtj_0C0B0Y3LYM9nFytYpgDA_RV4HouwU-Qp7t8RwWMd"
TOKEN="eIDty5mEQveNdIeVUUisu3:APA91bHgCKec2OnflVTgS7a5bCacJZjX18js8BvNoCfYR0_3N6nPAp6KWCrfL-PzG3AjTfCBDqYnzr0oB_fV62fjcFFrw5OTJFkt6t04NKhzEWjGuYHoooGDlBG6JF8uq2avny8sLByL"

push_service = FCMNotification(api_key=APIKEY)
PROJECT_ID = "project-8965d"
cred = credentials.Certificate(
    "/home/pi/Downloads/project-8965d-firebase-adminsdk-bkl6z-29507732d7.json")
default_app = firebase_admin.initialize_app(cred, {'storageBucket': f"{PROJECT_ID}.appspot.com"})
# 버킷은 바이너리 객체의 상위 컨테이너. 버킷은 Storage에서 데이터를 보관하는 기본 컨테이너.
bucket = storage.bucket()  # 기본 버킷 사용
fireStatus = False
fireCascade = cv.CascadeClassifier('/home/pi/fire.xml')
# 카메라 정보 받아오기 pi카메라는 -1
capture = cv.VideoCapture(-1)
# 비디오 코덱설정
fourcc = cv.VideoWriter_fourcc(*'XVID')
picture_directory = "/home/pi/image_store/"
video_directory = "/home/pi/video_store/"

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
            
            print('불꽃 감지!! (' + now.strftime('%Y-%m-%d %H:%M:%S') + ')')
            sendMessage(str(now.strftime('%Y-%m-%d %H:%M:%S')))
            
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

    blob.upload_from_filename(filename='/home/pi/image_store/' + file)
    print("사진 업로드 완료")


def uploadVideo(file):
    blob = bucket.blob('detect_history/videos/' + file)
    # new token, metadata 설정
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token}  # access token 필요
    blob.metadata = metadata

    blob.upload_from_filename(filename='/home/pi/video_store/' + file)
    print("영상 업로드 완료")
    
def sendMessage(now):  # 메시지 (data 타입)
    data_message = {
        "title": now,
        "body": "불꽃이 감지되었습니다!"
    }

    # 토큰값을 이용해 1명에게 푸시알림을 전송함
    result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)

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
