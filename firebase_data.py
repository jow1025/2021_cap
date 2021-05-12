#import firebase_admin
#from firebase_admin import credentials
import pyrebase
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
gas = 11
GPIO.setup(gas,GPIO.IN)
config={
    "apiKey":"kk4ks2sHVBKCA5TExxZPjEiqlNmJOdUywZN4At5g",
    "authDomain": "project-8965d.firebaseapp.com",
    "databaseURL": "https://project-8965d-default-rtdb.firebaseio.com",
    "storageBucket": "gs://project-8965d.appspot.com"
}
firebase=pyrebase.initialize_app(config)
db=firebase.database()
print("start")
print("------------")
print()

while True:
    val=GPIO.input(gas)
    print(val)

    data={
        "val":val
    }
    db.child("8965d").child("1-set").set(val)
    db.child("8965d").child("2-push").push(val)
    time.sleep(2)