#!/usr/bin/env python3
import numpy as np
import cv2
from mss import mss


cords = {'top':0 , 'left': 1920 , 'width': 1920, 'height': 1080 }
#cap = cv2.VideoCapture(0)

while(True):
    with mss() as sct :
        img = np.array(sct.grab(cords)) #sct.grab(cords/monitor)
    #cimg = cv2.cvtColor(img , cv2.COLOR_BGRA2GRAY)
    #ret, frame = cap.read()
    img = cv2.medianBlur(img,5)
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        #cap.release()
        break
