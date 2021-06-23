import time
import threading
import serial_commute
import fire_detect

thread1=threading.Thread(target=serial_commute.data_commute)
thread2=threading.Thread(target=fire_detect.observe)
if __name__=="__main__":
#   thread1=Thread(target=t.printhello)
#   thread2=Thread(target=t1.printhello1)

    thread1.start()
    thread2.start()
