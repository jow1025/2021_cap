import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import cv2 as cv
from uuid import uuid4
import push_message as fcm
import time

PROJECT_ID = "cap-aacc4"
cred = credentials.Certificate(
    "/home/pi/2021_cap/fire_detect_opencv/cert_key/cap-aacc4-firebase-adminsdk-qc42b-169c65d5e2.json")
default_app = firebase_admin.initialize_app(cred, {'storageBucket': f"{PROJECT_ID}.appspot.com"})
# 버킷은 바이너리 객체의 상위 컨테이너. 버킷은 Storage에서 데이터를 보관하는 기본 컨테이너.
bucket = storage.bucket()  # 기본 버킷 사용
fireStatus = False

capture_time = datetime.datetime.now()


def observe():
    print('불꽃 감시 중..')
    global fireStatus, capture_time
    now = datetime.datetime.now()
    str_now=str(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('불꽃 감지!! (' + str_now + ')')
    fcm.sendMessage(str_now)
    fireStatus=True;


while True:
    if fireStatus==False:
        observe()
    else:
        time.sleep(1)
        fireStatus=False;
