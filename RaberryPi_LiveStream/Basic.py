import cv2 as cv
import subprocess as sp

rtmpUrl = "rtmp://bvc.live-send.acg.tv/live-bvc//?streamname=live_393056819_39750720&key=528d4cd0458241ea8976084670a6493c"
camera_path = "/dev/video0"
cap = cv.VideoCapture(camera_path)

# Get video information
fps = int(cap.get(cv.CAP_PROP_FPS))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# ffmpeg command
command = ['ffmpeg',
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
    ret, frame = cap.read()
    if not ret:
        print("Opening camera is failed")
        break

    # process frame
    # your code
    # process frame

    # write to pipe
    p.stdin.write(frame.tostring())

