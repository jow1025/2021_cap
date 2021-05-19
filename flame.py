
# 시리얼, 시간 객체 가져오기
from twilio.rest import Client
from time import time,sleep
import serial
from twilio.rest import Client
#USB 0번 포트를 9600bps 속도로 ser 객체 선언, 만약 에러가 난다면 USB0을 USB1로 변경 요망
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
account_sid = 'ACb71ce0db02c9c4dabc8df0cf3bbb4d52'
auth_token = 'e3d18d0a0836724c7049d99363343c59'
client = Client(account_sid, auth_token)
#0.1초 대기
#time.sleep(0.1)

twilio_client=client
try:
    #time.sleep(0.1)
    fire = 0
    time_sent=0
    while 1:
        # serial 포트로 들어온 데이터를 \n까지 읽은 뒤 string형으로 캐스팅 
        response = str(ser.read_until())
        # 문자열로 전송되는 데이터에서 원하는 값만 추출, 문자열 슬라이싱
        pos_start = response.find('a')
        if pos_start != -1:
            pos_end = response.find('r')
            fire = response[pos_start+1:pos_end-1]
            if fire=='1':
                message_interval=round(time()-time_sent)
                if message_interval > 30:#30초 주기 
                    #twilio_client=client
                    message = client.messages.create(
                        body='\n화재가 발생했습니다!!!!',
                        from_='+12066733748',
                        to='+8201099650391'
                        )
                else:
                    pass
                time_sent=round(time())
                #time.sleep(1)

#예외처리
except KeyboardInterrupt:
    ser.close()