from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyBwHzEdvN63ZO7VfYwrTpY2wVFuDJw18M4")
mToken = "Your App Token"


def sendMessage(now):
    registration_id = mToken

    data_message = {
        "body": '불꽃이 감지됐습니다! : ' + now
    }

    # data payload만 보내야 안드로이드 앱에서 백그라운드/포그라운드 두가지 상황에서 onMessageReceived()가 실행됨
    result = push_service.single_device_data_message(registration_id=registration_id, data_message=data_message)
    print(result)
