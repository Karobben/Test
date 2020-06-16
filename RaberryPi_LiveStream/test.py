#!/usr/bin/env python3

import cv2, sys, json, time
import numpy as np
import subprocess as sp

def BG_picture(IMG):
    BG = cv2.imread(IMG)
    height, width, c = BG.shape
    R = (height/h)/1.1
    BG = cv2.resize(BG, (int(width/R),int(height/R)), interpolation = cv2.INTER_AREA)
    height, width, c = BG.shape
    return BG, height, width

def Time_S():
    Time = time.ctime().split(" ")
    Houre = Time[3]
    Day = " ".join(Time[1:3])
    Week = Time[0]
    Year = Time[-1]
    return Year, Day, Week, Houre

Config = json.load(open('config.json'))
BGM = sys.path[0] +"/StarBucks_BGN.mp3"

rtmpUrl = "rtmp://bvc.live-send.acg.tv/live-bvc//?streamname=live_393056819_39750720&key=528d4cd0458241ea8976084670a6493c"
camera_path = "/dev/video0"
cap = cv2.VideoCapture(camera_path)



# read webcamera
while(cap.isOpened()):
    #Config = json.load(open('config.json'))
    #BG, height, width = BG_picture(Config['BG_img'])
    ret, frame = cap.read()
    if not ret:
        print("Opening camera is failed")
        break
    frame2 = frame*1.5+10
    frame2[frame2>255]=255
    frame2 = np.array(frame2.astype(int), dtype=np.uint8)
    cv2.imshow('image',frame)
    cv2.imshow('image2',frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break
