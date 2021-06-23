# -*- encoding: utf-8 -*-
import datetime

from pyfcm import FCMNotification

APIKEY="AAAAUTKu0rA:APA91bEa6KQv-LG8mOabTpNim_pNdqdWDa2nma3v27-Wn78VL89DnG9EDrBBBBUQ6JnoU8eVi_RWC82hNBTU1dD8pPJWgH62eu1EbcxwmUW3TiqZquPK8KuDP3IUaK2GupKEMQuY_IdE"
TOKEN="eIJNSlW7T0Sl17zp0YQhbx:APA91bGACNlOXs61FwZ8USbFXO28hMdLqrjJP67MOTK9-kGvQcRU6uljRk7vXUQq2HdUNUoFOkqaYpgDJ_JrCXYfmrZYRGRPSnOhPuODUcYFYGvMHyfQIMq86Tv_71dTwbZ1DqZwRQ2T"

# 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
push_service = FCMNotification(api_key=APIKEY)


def sendMessage(now):  # 메시지 (data 타입)
    data_message = {
        "title": now,
        "body": "불꽃이 감지되었습니다!"
    }

    # 토큰값을 이용해 1명에게 푸시알림을 전송함
    result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)

sendMessage(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


