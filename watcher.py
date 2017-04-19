from screenGrab import *
import numpy
from detection import *
import pyrobot
debug = True

def watch(mainQueue):
    while(1):
        printscreen = ImageGrab.grab()
        frame =   numpy.array(printscreen.getdata(),dtype='uint8')\
        .reshape((printscreen.size[1],printscreen.size[0],3)) 

        frame,coord = detectMonsters(frame)
        if coord == False:
            if debug == True:
                print("No monster Found")
    		  #Player.teleport

    	else:
            element = {}
            element["type"] = "monster"
            element["coord"] = coord
            mainQueue.put(element)
            #print("watchThread having mainQueue : "+str(mainQueue.qsize())+" items")
