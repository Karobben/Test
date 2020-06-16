#!/usr/bin/env python3

import cv2, sys, json, time
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

# Get video information
fps = 32#int(cap.get(cv2.CAP_PROP_FPS))
ret, frame = cap.read()
h, w, c = frame.shape

BG, height, width = BG_picture(Config['BG_img'])
# ffmpeg command
command = ['ffmpeg',
        #'-re', '-stream_loop', '-1',
        #'-i', '/home/pi/scrpt/Blive/StarBucks_BGN.mp3',
        '-y',
        '-f', 'rawvideo',
        '-vcodec','rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', "{}x{}".format(width, height),
        '-r', str(fps),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-f', 'flv',
        rtmpUrl]

# 管道配置
p = sp.Popen(command, stdin=sp.PIPE)


# read webcamera
while(cap.isOpened()):
    Config = json.load(open('config.json'))
    #BG, height, width = BG_picture(Config['BG_img'])  # This proccess will slow the script
    ret, frame = cap.read()
    if not ret:
        print("Opening camera is failed")
        break

    # write to pipe
    BG[0:h,0:w] = frame
    Year, Day, Week, Houre = Time_S()
    BG2 = cv2.putText(BG, Houre, ( width -250,  50), cv2.FONT_HERSHEY_DUPLEX , 1.3, ( 102, 102, 255), 2)
    BG2 = cv2.putText(BG2, Day, ( width -250,  80), cv2.FONT_HERSHEY_DUPLEX , 0.8, ( 102, 102, 255), 2)
    #BG2 = cv2.putText(BG2, Week, ( width -150,  80), cv2.FONT_HERSHEY_DUPLEX , 0.5, ( 102, 102, 255), 2)
    BG2 = cv2.putText(BG2, Year, ( width -135,  80), cv2.FONT_HERSHEY_DUPLEX , 0.8, ( 102, 102, 255), 2)

    p.stdin.write(BG2.tostring())
