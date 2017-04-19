import cv2
import numpy
import time
def detectMonsters(frame):
	debug = False
	beginDetection = time.time()

	hsv = 	cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # Convert RGB image into HSV image (Hue Saturation Value) => requiered for 
	green = numpy.uint8([[[66,0,132 ]]]) 
	hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV) #Convert the RGB Color to track into HSV Color
	#print hsv_green 
	#cv2.imshow("frame",frame)
	color = numpy.array([165,255,132]) 
	endConversions = time.time()
	if debug == True:
		print("Image Conversions processed in : " + str(endConversions - beginDetection) + " s")
	beginMasking = time.time()
	mask = cv2.inRange(hsv, color, color) #The inRange function takes 2 colors. Upper and Lower. Everything between will be targeted. here, we only want one color.
	endMasking = time.time()
	if debug == True:
		print("Masking processed within : "+ str(endMasking-beginMasking)+" s")

	beginNegation = time.time()
	res = cv2.bitwise_and(frame,frame, mask= mask) #The result of the match. it negates every single pixel but the ones with our color inside.
	endNegation = time.time()
	if debug == True:
		print("Pixel Negation proccessed in : "+str(endNegation-beginNegation)+" s")

	beginContoursSearch = time.time()
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] #Found contours on mask
	endContoursSearch = time.time()
	if debug == True:
		print("Search Contours processed in : "+ str(endContoursSearch-beginContoursSearch)+" s")
	if len(cnts) < 1:
		endDetection = time.time()
		if debug == True:
			print("Global Detection processed within "+ str(endDetection-beginDetection)+" s")
		return frame,False
	else:

		beginContourDrawing = time.time()
		cv2.drawContours(frame, cnts, 0, (127, 255, 0), 3)# Draw the contours on the base frame (the screenshot)
		endContourDrawing = time.time()

		beginCircleCreation = time.time()
		(x,y),radius = cv2.minEnclosingCircle(cnts[0])

		print("x: "+str(x)+" y: "+str(y)) # Here are the coordinates of the center of the object
		coord=[0,0]
		coord[0] = int(x)
		coord[1] = int(y)
		center = (int(x),int(y))
		radius = int(radius)
		cv2.circle(frame, center, radius, (255, 0, 0), 3)

		endCircleCreation = time.time()
		if debug == True:
			print("Contour Drawing :"+ str(endContourDrawing - beginContourDrawing)+" s" )
		if debug == True:
			print("Circle Creation processed in :"+str(endCircleCreation - beginCircleCreation) +" s")
		endDetection = time.time()
		if debug == True:
			print("Detection processed within "+ str(endDetection-beginDetection)+" s")
		return frame,coord