#!/usr/bin/env python3

import cv2, sys, json, time
import subprocess as sp
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageSequence
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
#
from libs.Gif_read import GIF, CombinePic


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

def fig2data(fig):
    """
    fig = plt.figure()
    image = fig2data(fig)
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    import PIL.Image as Image
    # draw the renderer
    fig.canvas.draw()
    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis=2)
    image = Image.frombytes("RGBA", (w, h), buf.tostring())
    image = np.asarray(image)
    return image

def TODO_Board():
    '''
    Build a todo list bar chat
    '''
    TODO = open("ToDolist").read().split('\n')[:-1]
    X=[]
    for i in TODO:
      X += [i.split('\t')[0]]

    Y1=[]
    for i in TODO:
      Y1 += [int(i.split('\t')[1])]

    Y2=[]
    for i in TODO:
      Y2 += [int(i.split('\t')[2])]

    my_font = FontProperties(fname='simsun.ttc')
    figure = plt.figure()
    plt.bar(X,Y1,color='r')
    plt.bar(X,Y2,color='g')
    plt.xticks(X, FontProperties = my_font, rotation = 45)
    ##
    image = fig2data(figure)
    return image

Config = json.load(open(sys.path[0]+'/config.json'))
#BGM = sys.path[0] +"/StarBucks_BGN.mp3"

rtmpUrl = "rtmp://bvc.live-send.acg.tv/live-bvc//?streamname=live_393056819_39750720&key=528d4cd0458241ea8976084670a6493c"
camera_path = "/dev/video0"
camera_path2 = "/dev/video1"
cap = cv2.VideoCapture(camera_path)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap2 = cv2.VideoCapture(camera_path2)

# Get video information
fps = 30#int(cap.get(cv2.CAP_PROP_FPS))
ret, frame = cap.read()
h, w, c = frame.shape

BG, height, width = BG_picture(Config['BG_img'])
BG_pic, H_BG2, W_BG2 = BG_picture(sys.path[0]+'/Eco_tank.png')

H = Config['Camera2_height']
W = Config['Camera2_width']
BG_pic = cv2.resize(BG_pic, (W,H), interpolation = cv2.INTER_AREA)

# Gif pika
GIF_pika = img = GIF(sys.path[0]+"/pika.gif")
pika_h = len(GIF_pika[0])
pika_w = len(GIF_pika[0][0])
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
#p = sp.Popen(command, stdin=sp.PIPE)


# read webcamera
Time_1 = time.time()
Num = 0
while(cap.isOpened()):
    Year, Day, Week, Houre = Time_S()
    Config = json.load(open(sys.path[0]+'/config.json'))
    ret, frame = cap.read()

    if not ret:
        print("Opening camera is failed")
        break
    # Lightning
    #frame2 = contrast_img( frame, Config['Lighten_R'], Config['Lighten_B'])
    #frame2 = Zoom_img( frame2, Config["Zoom_X"], Config["Zoom_Y"], Config["Zoom_height"],Config["Zoom_D"])
    #frame2 = cv2.resize(frame2, (width,height), interpolation = cv2.INTER_AREA)
    # Add BG
    BG2 = cv2.resize(BG, (width,height), interpolation = cv2.INTER_AREA)
    BG2[0:h,0:w] = frame

    Y = Config['Camera2_Y']
    X = Config['Camera2_X']
    H = Config['Camera2_height']
    W = Config['Camera2_width']
    BG2[Y:H+Y,X:X+W] = BG_pic
    # Add Date
    BG2 = cv2.putText(BG2, Houre, ( width -250,  50), cv2.FONT_HERSHEY_DUPLEX , 1.3, ( 102, 102, 255), 2)
    BG2 = cv2.putText(BG2, Day, ( width -250,  80), cv2.FONT_HERSHEY_DUPLEX , 0.8, ( 102, 102, 255), 2)
    #BG = cv2.putText(BG2, Week, ( width -150,  80), cv2.FONT_HERSHEY_DUPLEX , 0.5, ( 102, 102, 255), 2)
    BG2 = cv2.putText(BG2, Year, ( width -135,  80), cv2.FONT_HERSHEY_DUPLEX , 0.8, ( 102, 102, 255), 2)
    # Text
    BG2 = cv2.putText(BG2, Config['Text1'], ( Config['Text1_X'],  Config['Text1_Y']), cv2.FONT_HERSHEY_DUPLEX , 0.8, ( 102, 102, 255), 2)
    BG2 = cv2.putText(BG2, Config['Text2'], ( Config['Text2_X'],  Config['Text2_Y']), cv2.FONT_HERSHEY_DUPLEX , 1, ( 0, 0, 0), 2)
    #fram = cv2.resize(BG2, (340,220), interpolation = cv2.INTER_AREA)
    # add the GIF
    ID = Num%(len(GIF_pika))
    Num +=1
    #BG2[0:pika_h,0:pika_w] = GIF_pika[ID]
    BG2 = CombinePic(BG2,GIF_pika[ID])
    cv2.imshow('image',BG2)
    #cv2.imshow('image2',frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
'''
    try:
        p.stdin.write(BG2.tostring())
    except:
        break


'''
