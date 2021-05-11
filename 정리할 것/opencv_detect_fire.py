import cv2
import numpy as np

fireCascade=cv2.CascadeClassifier('/home/pi/fire.xml')
image=cv2.imread('/home/pi/fire2.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
fire=fireCascade.detectMultiScale(image,1.2,5)

for(x,y,w,h) in fire:
	#cv2.rectangle(img,(x+y),(x+w,y+h),(0,255,0),2)
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
	print('Fire is detected..!')

cv2.imshow('Fire',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#	if cv2.waitkey(5) ==27:
 
#		break

#cv2.destroyAllWindows()

