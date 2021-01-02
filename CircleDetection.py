# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:12:17 2019

@author: Haroon Nawaz
"""

import cv2
import numpy as np
import serial
import time

cam = cv2.VideoCapture(1)

threshold = 0.05
freq = 1

c2 = [0,0,0]

ser = serial.Serial('COM4', 9600)
time.sleep(3)

def check_trajectory():
    try:
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist=100,
                                   param1=75,param2=75,minRadius= 100,maxRadius=130)
        c1 = np.around(circles)[0][0]
    except AttributeError:
        pass
    
def move_motor():
    
    ser.write(b'-1 ')
    
try:

    while(True):

        s, img = cam.read()
        cimg = img
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = cv2.medianBlur(img,5)
        
#        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        
        t = time.clock()
        if ((t % freq) <= threshold) or (c2 == [0,0,0]):
            check_trajectory()
            
        try:
            circles2 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist=1000,
                                        param1=50,param2=14,minRadius=6,maxRadius=8)
            c2 = np.around(circles2)[0][0]  
        except AttributeError:
            pass

        cv2.circle(cimg,(c2[0],c2[1]),c2[2],(0,255,0),2) 
        cv2.circle(cimg,(c2[0],c2[1]),2,(0,0,255),3)    
#    
#        cv2.circle(cimg,(c1[0],c1[1]),c1[2],(0,255,0),2)  
#        cv2.circle(cimg,(c1[0],c1[1]),2,(0,0,255),3)   

        cv2.imshow("Circle Detection",cimg)
        
        if c2[1] >= c1[1]:
            move_motor()
            time.sleep(0.001)
            
        cv2.waitKey(5)

except KeyboardInterrupt:
    cv2.destroyAllWindows()

cv2.destroyAllWindows()
time.sleep(0.1)
ser.close()