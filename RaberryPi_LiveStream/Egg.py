#!/usr/bin/env python3

import cv2, sys, json, time
import subprocess as sp
import numpy as np

def BG_picture(IMG):
    BG = cv2.imread(IMG)
    height, width, c = BG.shape
    R = (height/h)/1.1
    BG = cv2.resize(BG, (int(width/R),int(height/R)), interpolation = cv2.INTER_AREA)
    height, width, c = BG.shape
    return BG, height, width

def Time_S():
    Time = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()).split(" ")
    Houre = Time[3]
    Day = " ".join(Time[1:3])
    Week = Time[0]
    Year = Time[-1]
    return Year, Day, Week, Houre

def contrast_img(img1, c, b):
    # 亮度就是每个像素所有通道都加上b https://blog.csdn.net/wsp_1138886114/article/details/82624534
    rows, cols, channels = img1.shape
    # 新建全零(黑色)图片数组:np.zeros(img1.shape, dtype=uint8)
    blank = np.zeros([rows, cols, channels], img1.dtype)
    dst = cv2.addWeighted(img1, c, blank, 1-c, b)
    return dst

Config = json.load(open('config.json'))
BGM = sys.path[0] +"/StarBucks_BGN.mp3"

rtmpUrl = "rtmp://bvc.live-send.acg.tv/live-bvc//?streamname=live_393056819_39750720&key=528d4cd0458241ea8976084670a6493c"
#camera_path = "/dev/video0"
camera_path2 = "/dev/video1"
#cap = cv2.VideoCapture(camera_path)
cap = cv2.VideoCapture(camera_path2)

# Get video information
fps = 9.5#int(cap.get(cv2.CAP_PROP_FPS))
ret, frame = cap.read()
h, w, c = frame.shape

BG, height, width = BG_picture(Config['BG_img'])
# ffmpeg command
command = ['ffmpeg',
        #'-re', '-stream_loop', '-1',
        #'-acodec', 'aac', '-ar', '44100',
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
Time_1 = time.time()
while(cap.isOpened()):
    Year, Day, Week, Houre = Time_S()
    ret, frame = cap.read()
    if time.time() - Time_1>1:
        Time_1 = time.time()
        #ret, egg_tmp = cap.read()
        egg_tmp = cv2.putText(frame, "/".join([Year,Day,Houre]), ( 440,  470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 102, 102, 255), 2)
        cv2.imwrite(sys.path[0]+"/Egg_2/"+str(time.time())+".png",egg_tmp)
    if not ret:
        print("Opening camera is failed")
        break
    # Lightning

    try:
        p.stdin.write(BG2.tostring())
    except:
        print("WARBING")
