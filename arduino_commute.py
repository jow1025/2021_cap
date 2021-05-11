{\rtf1\ansi\ansicpg949\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset129 AppleSDGothicNeo-Regular;\f2\fnil\fcharset0 HelveticaNeue;
}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
#
\f1  \'bd\'c3\'b8\'ae\'be\'f3, \'bd\'c3\'b0\'a3, \'c6\'c4\'c0\'cc\'be\'ee\'ba\'a3\'c0\'cc\'bd\'ba \'b0\'b4\'c3\'bc \'b0\'a1\'c1\'ae\'bf\'c0\'b1\'e2
\f0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f2\fs26 \cf0 import serial, time\
from firebase import firebase\
\
#
\f1 \'c6\'c4\'c0\'cc\'be\'ee\'ba\'a3\'c0\'cc\'bd\'ba DB\'c1\'d6\'bc\'d2\'b8\'a6 \'b0\'a1\'c1\'f6\'b0\'ed \'bf\'cd\'bc\'ad \'c3\'ca\'b1\'e2\'c8\'ad
\f2 \
firebase = firebase.FirebaseApplication("https://co2sensor-500bb-default-rtdb.firebaseio.com/",None)\
#USB 0
\f1 \'b9\'f8
\f2  
\f1 \'c6\'f7\'c6\'ae\'b8\'a6 9600bps \'bc\'d3\'b5\'b5\'b7\'ce ser \'b0\'b4\'c3\'bc \'bc\'b1\'be\'f0, \'b8\'b8\'be\'e0 \'bf\'a1\'b7\'af\'b0\'a1 \'b3\'ad\'b4\'d9\'b8\'e9 USB0\'c0\'bb USB1\'b7\'ce \'ba\'af\'b0\'e6 \'bf\'e4\'b8\'c1
\f2 \
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)\
#0.1
\f1 \'c3\'ca
\f2  
\f1 \'b4\'eb\'b1\'e2
\f2 \
time.sleep(0.1)\
\
try:\
    time.sleep(0.1)\
    while 1:\
	# serial 
\f1 \'c6\'f7\'c6\'ae\'b7\'ce
\f2  
\f1 \'b5\'e9\'be\'ee\'bf\'c2
\f2  
\f1 \'b5\'a5\'c0\'cc\'c5\'cd\'b8\'a6
\f2  \\
\f1 n\'b1\'ee\'c1\'f6 \'c0\'d0\'c0\'ba \'b5\'da string\'c7\'fc\'c0\'b8\'b7\'ce \'c4\'b3\'bd\'ba\'c6\'c3 
\f2 \
        response = str(ser.read_until())\
	# 
\f1 \'b9\'ae\'c0\'da\'bf\'ad\'b7\'ce
\f2  
\f1 \'c0\'fc\'bc\'db\'b5\'c7\'b4\'c2
\f2  
\f1 \'b5\'a5\'c0\'cc\'c5\'cd\'bf\'a1\'bc\'ad \'bf\'f8\'c7\'cf\'b4\'c2 \'b0\'aa\'b8\'b8 \'c3\'df\'c3\'e2, \'b9\'ae\'c0\'da\'bf\'ad \'bd\'bd\'b6\'f3\'c0\'cc\'bd\'cc
\f2 \
        pos_start = response.find('a')\
        pos_end = response.find('r')\
        response = response[pos_start+1:pos_end-1]\
	# 
\f1 \'b0\'aa
\f2  
\f1 \'c3\'e2\'b7\'c2
\f2 \
        print(response)\
	# 
\f1 \'b5\'a5\'c0\'cc\'c5\'cd\'ba\'a3\'c0\'cc\'bd\'ba\'bf\'a1 \'be\'f7\'b7\'ce\'b5\'e5
\f2 \
        result = firebase.put('Rpi', 'CO2', str(response)+"ppm") \
        # 10
\f1 \'c3\'ca
\f2  
\f1 \'b4\'eb\'b1\'e2
\f2 \
	time.sleep(10)\
\
#
\f1 \'bf\'b9\'bf\'dc\'c3\'b3\'b8\'ae
\f2 \
except KeyboardInterrupt:\
    ser.close()\
}