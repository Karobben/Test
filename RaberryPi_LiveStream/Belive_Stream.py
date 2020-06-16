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

def Zoom_img(frame, Zoom_X1, Zoom_Y1, height, Zoom):
    if Zoom == "Yes":
        h, w, c = frame.shape
        hw_R = w/h
        Zoom_Y1 = Zoom_Y1
        Zoom_Y2 = Zoom_Y1 + height
        Zoom_X1 = Zoom_X1
        Zoom_X2 = int(Zoom_X1 + height*hw_R)
        frame = frame[Zoom_Y1:Zoom_Y2,Zoom_X1:Zoom_X2]
        frame = cv2.resize(frame, (w,h), interpolation = cv2.INTER_AREA)
    else:
        frame = frame
    return frame

Config = json.load(open('config.json'))
BGM = sys.path[0] +"/StarBucks_BGN.mp3"

rtmpUrl = "rtmp://bvc.live-send.acg.tv/live-bvc//?streamname=live_393056819_39750720&key=528d4cd0458241ea8976084670a6493c"
camera_path = "/dev/video0"
camera_path2 = "/dev/video1"
cap = cv2.VideoCapture(camera_path)
cap2 = cv2.VideoCapture(camera_path2)

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
    Config = json.load(open('config.json'))
    #BG, height, width = BG_picture(Config['BG_img'])
    if Config['Sitch_Camare'] == "No":
        ret, frame = cap.read()
        ret, img_egg = cap2.read()
    elif Config['Sitch_Camare'] == "Yes":
        ret, img_egg = cap.read()
        ret, frame   = cap2.read()
        img_egg = Zoom_img( img_egg, Config["Zoom_X"], Config["Zoom_Y"], Config["Zoom_height"],Config["Zoom_D"])
    img_egg2 = cv2.resize(img_egg, (Config['Camera2_width'],Config['Camera2_height']), interpolation = cv2.INTER_AREA)
    # save egg img
    if time.time() - Time_1>60:
        Time_1 = time.time()
        ret, egg_tmp = cap2.read()
        egg_tmp = cv2.putText(egg_tmp, "/".join([Year,Day,Houre]), ( 440,  470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 102, 102, 255), 2)
        cv2.imwrite(sys.path[0]+"/Egg/"+str(time.time())+".png",egg_tmp)
    if not ret:
        print("Opening camera is failed")
        break
    # Lightning
    #frame2=contrast_img( frame, Config['Lighten_R'], Config['Lighten_B'])
    #index = np.where(frame2 > 220)
    #frame2[index[0],index[1]] = frame[index[0],index[1]]

    # Add BG
    BG2 = cv2.resize(BG, (width,height), interpolation = cv2.INTER_AREA)
    BG2[0:h,0:w] = frame#2

    # Add Camare2
    Y = Config['Camera2_Y']
    X = Config['Camera2_X']
    H = Config['Camera2_height']
    W = Config['Camera2_width']
    BG2[Y:H+Y,X:X+W] = img_egg2
    # Add Date
    BG2 = cv2.putText(BG2, Houre, ( width -250,  50), cv2.FONT_HERSHEY_DUPLEX , 1.3, ( 102, 102, 255), 2)
    BG2 = cv2.putText(BG2, Day, ( width -250,  80), cv2.FONT_HERSHEY_DUPLEX , 0.8, ( 102, 102, 255), 2)
    #BG = cv2.putText(BG2, Week, ( width -150,  80), cv2.FONT_HERSHEY_DUPLEX , 0.5, ( 102, 102, 255), 2)
    BG2 = cv2.putText(BG2, Year, ( width -135,  80), cv2.FONT_HERSHEY_DUPLEX , 0.8, ( 102, 102, 255), 2)
    # Text
    BG2 = cv2.putText(BG2, Config['Text1'], ( Config['Text1_X'],  Config['Text1_Y']), cv2.FONT_HERSHEY_DUPLEX , 0.8, ( 102, 102, 255), 2)

    try:
        p.stdin.write(BG2.tostring())
    except:
        break
