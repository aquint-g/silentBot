#-*- coding: utf-8 -*-
"""
Toutes les coordonnées sont basées sur un écran de résolution 1920x1080
x_pad = 0
y_pad = 0

game area = x_pad+1, y_pad+1, x_pad+screen_width, y_pad+screen_height
"""
import config
import os
import time
from screenGrab import *
import mouse
import win32api, win32con
import numpy
import ImageOps
from PIL import ImageChops
import cv2
x_pad = 0
y_pad = 0
screen_width = 1920
screen_height = 1080




#cap = cv2.VideoCapture(0)
# Requirement : GRF edition to show up the monsters we want to target into color specific squares
# We'll loop screenshotting the client window
# On these screenshots, we'll find the color specific squares and locate them using the "CONTOURS" technology of OpenCV
# Need to plug a winpcap listener on the client in order to analyze the incoming trafic (the incoming only) : It will allow us 


while(1):
    frame = cv2.imread('full_snap__1490996017.png') #  Here is the screenshot, it'll be automated then (the function exists below)
    hsv = 	cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # Convert RGB image into HSV image (Hue Saturation Value) 
    green = numpy.uint8([[[163,73,164 ]]]) 
    hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV) #Convert the RGB Color to track into HSV Color
    print hsv_green 
    cv2.imshow("frame",frame)
    color = numpy.array([150,141,164]) 

    mask = cv2.inRange(hsv, color, color) #The inRange function takes 2 colors. Upper and Lower. Everything between will be targeted. here, we only want one color.
    res = cv2.bitwise_and(frame,frame, mask= mask) #The result of the match. it negates every single pixel but the ones with our color inside.

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] #Found contours on mask
    cv2.drawContours(frame, cnts, 0, (127, 255, 0), 3)# Draw the contours on the base frame (the screenshot)

    (x,y),radius = cv2.minEnclosingCircle(cnts[0])

    print("x: "+x+" y: "+y) # Here are the coordinates of the center of the object
    # These coordinates need a light modification. Indeed, here, we're counting as y,x = 0 = bottom left of the image, wherehas, according to win32api, y,x = 0 = top left of  the screen 

    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(frame, center, radius, (255, 0, 0), 3)
    # Display Windows ... 
    cv2.imshow('frame',frame)
    """
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    """
    # wait
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


"""
while(True):
    printscreen_pil =  ImageGrab.grab()

    printscreen_numpy =   numpy.array(printscreen_pil.getdata(),dtype='uint8')\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3)) 
    printscreen = printscreen_numpy.astype(numpy.float32)

    template = cv2.imread('template.bmp',cv2.IMREAD_COLOR) # chargement du template .jpg en image OpenCV
    method = 'cv2.TM_CCOEFF'
    w, h, z = template.shape[::-1]

    meth = eval(method) #la méthode de recherche du template
    res = cv2.matchTemplate(printscreen_numpy,template,meth) # la fonction de recherche
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(printscreen,top_left, bottom_right, 255, 2)
    cv2.imshow('window',printscreen_numpy)
    time.sleep(5)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


"""
"""
im1 = screenGrab(x_pad,y_pad,screen_width,screen_height) #prise du screenshot
screenshot = numpy.array(im1) #transformation en image OpenCV

im1.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')

screen = cv2.imread('full_snap__1490995023.png')

template = cv2.imread('mobs/template.jpg',0) # chargement du template .jpg en image OpenCV
w, h = template.shape[::-1]

method=0 #la méthode de recherche du template

res = cv2.matchTemplate(screen,template,method) # la fonction de recherche

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
cv2.rectangle(screen,top_left, bottom_right, 255, 2)


time.sleep(1)
im2 = screenGrab(x_pad,y_pad,screen_width,screen_height)

diff = PIL.ImageChops.difference(im1, im2)
mouse.get_cords(x_pad,y_pad)"""