#-*- encoding: utf-8 -*-
from pyfcm import FCMNotification
APIKEY="AAAAalMeKts:APA91bEiB12GcGeo5W0MmzOjjmcDiR9LwrVgUxmspbWpI4eZz0LjuFIuTVxnfCbqd_IoeMjVkqJt5BGe9V77gvzFLmfSj5utQtj_0C0B0Y3LYM9nFytYpgDA_RV4HouwU-Qp7t8RwWMd"
TOKEN="egej7XPRReWXTPHnoUkZGY:APA91bHE1EKFp3dKpADWteaqyxb0eQW2JCYhWFLjRfdJ42e9whr4F3XQy2MFO03It3VjrrnUlwSYHTH9C7ByQiSo5S3d-VJ_d9ndnKiQuwxCHMmdVpj_xZQsFbmhdgWKkZ70k8lp8HrH"

# 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
push_service = FCMNotification(api_key=APIKEY)
 
'''
def sendMessage(body, title):
    # 메시지 (data 타입)
    message_title=title
    message_body=body
 
    # 토큰값을 이용해 1명에게 푸시알림을 전송함
    result = push_service.notify_single_device(registration_id=TOKEN, message_title=message_title,message_body=message_body)
 
    # 전송 결과 출력
    print(result)
 
sendMessage("title", "body")
'''
def sendMessage(body, title): # 메시지 (data 타입)
    data_message = {
        "title": title,
        "body": body
    }
 
    # 토큰값을 이용해 1명에게 푸시알림을 전송함
    result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)
 
    # 전송 결과 출력
    print(result)
 
sendMessage("title", "body")
   

