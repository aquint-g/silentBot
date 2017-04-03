
#-*- coding: utf-8 -*-
import ImageGrab
import os
import time
import PIL
#Global variables


def screenGrab(x_pad,y_pad,screen_width,screen_height):
    box = ()
    im = ImageGrab.grab([x_pad+1,y_pad+1,x_pad+screen_width,x_pad+screen_height])
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    return im
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()