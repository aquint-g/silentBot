import cv2
import numpy
def detectMonsters(frame):
	hsv = 	cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # Convert RGB image into HSV image (Hue Saturation Value) => requiered for 
	green = numpy.uint8([[[163,73,164 ]]]) 
	hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV) #Convert the RGB Color to track into HSV Color
	print hsv_green 
	cv2.imshow("frame",frame)
	color = numpy.array([150,141,164]) 

	mask = cv2.inRange(hsv, color, color) #The inRange function takes 2 colors. Upper and Lower. Everything between will be targeted. here, we only want one color.
	res = cv2.bitwise_and(frame,frame, mask= mask) #The result of the match. it negates every single pixel but the ones with our color inside.

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] #Found contours on mask

	if len(cnts) < 1:
		return frame,False
	else:
		cv2.drawContours(frame, cnts, 0, (127, 255, 0), 3)# Draw the contours on the base frame (the screenshot)

		(x,y),radius = cv2.minEnclosingCircle(cnts[0])

		print("x: "+str(x)+" y: "+str(y)) # Here are the coordinates of the center of the object
		coord=[0,0]
		coord[0] = int(x)
		coord[1] = int(y)
		center = (int(x),int(y))
		radius = int(radius)
		cv2.circle(frame, center, radius, (255, 0, 0), 3)
		return frame,coord