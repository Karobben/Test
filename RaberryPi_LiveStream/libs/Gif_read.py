#!/usr/bin/env python3
import time, cv2
from PIL import Image
import numpy as np

def GIF(file):
    List = []
    im = Image.open(file)
    im.seek(1)#skip to the second frame
    try:
        while 1:
            List += [cv2.cvtColor(np.asarray(im.convert()),cv2.COLOR_RGB2BGR)]
            im.seek(im.tell()+1)
    except EOFError:#the sequence ends
        pass
    return List
'''
def CombinePic(pathPic1,pathPic2):
    #https://www.jianshu.com/p/0b0c2e3bd1a6
    img1 = cv2.resize(pathPic1, (512,512), interpolation=cv2.INTER_CUBIC) #底图 _pathPic1 为底图位置
    img2 = cv2.resize(pathPic2, (512,512), interpolation=cv2.INTER_CUBIC) #素材 _pathPic2 为素材位置
    img_mix = cv2.addWeighted(img1, 1, img2,1, 1) #合并，其中参数1表示透明度，第一个1表示img1不透明，第二个1表示img1不透明，如果改成0.5表示合并的时候已多少透明度覆盖。
    return img_mix #合并完毕，_pathPic1底图被修改成合并后的图片
'''
def CombinePic(img1,img2,Y=0,X=400):
    rows,cols,channels = img2.shape
    roi = img1[X:X+rows, Y:Y+cols ] #先创建了抠图区域
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) #转为灰度图片
    img2[img2gray==0] = np.array([255,255,255], dtype='uint8')
    #cv2.imshow('img2gray',img2gray)
    ret, mask = cv2.threshold(img2gray, 227, 255, cv2.THRESH_BINARY) #通过灰度设置阈值对比，建立mask区域
    mask_inv = cv2.bitwise_not(mask)
    #cv2.imshow('mask',mask)
    #cv2.imshow('mask_inv',mask_inv)
    # Now black-out the area of logo in ROI
    # 取 roi 中与 mask 中不为零的值对应的像素的值，其他值为 0
    # 注意这里必须有 mask=mask 或者 mask=mask_inv, 其中的 mask= 不能忽略
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask) #抠图区进行掩膜保护，留下需要的图片
    #cv2.imshow('img1_bg',img1_bg)
    # 取 roi 中与 mask_inv 中不为零的值对应的像素的值，其他值为 0。
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv) #对贴图进行掩膜保护，留下需要的图片
    #cv2.imshow('img2_fg',img2_fg)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg) #抠图区和贴图合并
    img1[X:X+rows, Y:Y+cols ] = dst #合并后再合并替换掉原来的大图区域
    return img1
