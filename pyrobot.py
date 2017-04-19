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
import mouse
import win32api, win32con #à virer car déjà appelé dans mouse.py
import ImageOps # plus besoin
from PIL import ImageChops
import cv2
#import player
import sniffer
import Queue
from threading import Thread
import watcher
# x_pad and y_pad are the position of the window on your screen (no problem if full screen)
x_pad = 0
y_pad = 0 
screen_width = 670
screen_height = 550
debug = False
teleport_key = "F5"



# Dev under Python 2.7  
#cap = cv2.VideoCapture(0)
# Requirement : GRF edition to show up the monsters we want to target into color specific squares
# Requirement 2  : Disable lightmaps ( Ragnarök settings )
# pip install pydivert (for packet sniffing)

# We'll loop screenshotting the client window
# On these screenshots, we'll find the color specific squares and locate them using the "CONTOURS" technology of OpenCV
# Need to plug a winpcap listener on the client in order to analyze the incoming trafic (the incoming only) : It will allow us to watch HP / SP, 

# Issue 1 :
# The cursor go on a location next to the target, but not on it.
# You sould configure your Python.exe to accept high resolution DPI => Go to your Python FOlder => right click => compatibilities .. and you're done



def watchScreen(mainQueue):
    watcher.watch(mainQueue)

def program():
    global mainQueue
    mainQueue = Queue.LifoQueue()
    t1 = Thread(target = watchScreen,args=(mainQueue,)) # target is the above function
    t1.start() # start the thread

    while(1):
        if mainQueue.qsize() > 0:
            print("There are "+str(mainQueue.qsize())+" items in queue")
            element = mainQueue.get()
            if element["type"]=="monster":
                print("monster found on "+str(element["coord"][0])+","+str(element["coord"][1]))
                
        else:
            time.sleep(1)


if __name__ == '__main__':
    program()
"""         
mouse.mousePos(x_pad,y_pad,coord)
		#time.sleep(.2)
mouse.leftClick()
		#time.sleep(7)
"""
	# Display Window ... 
	#cv2.imshow('frame',frame)
	
	#k = cv2.waitKey(2) & 0xFF

	#if k == 27:
	#	break

"""
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    """
    # wait
	

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