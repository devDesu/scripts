# -*- coding: cp1251 -*-
import cv2
import sys
import fcntl, os
from v4l2 import *
import numpy as np


width = 640
height = 480

cascPath = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
print 'loaded haar face cascade'
if len(sys.argv)>1:
	name = sys.argv[1]
else:
	name = "hotline.png"
s_img = cv2.imread(name, -1)
cv2.namedWindow('Video')
video_capture = cv2.VideoCapture(0)
video_capture.set(3, width)
video_capture.set(4, height)
video_capture.set(5, 15)
cv2.createTrackbar('ofstY', 'Video', 50, 130, lambda x: x)
cv2.createTrackbar('ofstX', 'Video', 50, 100, lambda x: x)
cv2.createTrackbar('deltaX', 'Video', 0, 80, lambda x: x)
cv2.createTrackbar('deltaY', 'Video', 0, 80, lambda x: x)
device = open("/dev/video1", "wb", 0)


def config_device(device):
    print 'configuring device: ', device
    capability = v4l2_capability()
    print "get capabilities result", (fcntl.ioctl(device, VIDIOC_QUERYCAP, capability))
    print "capabilities", hex(capability.capabilities)
    #fmt = V4L2_PIX_FMT_YUYV
    #fmt = V4L2_PIX_FMT_YUV420M
    fmt = V4L2_PIX_FMT_YUYV
    #fmt=V4L2_PIX_FMT_SGBRG8 
    print("v4l2 driver: " + capability.driver)
    format = v4l2_format()
    format.type = V4L2_BUF_TYPE_VIDEO_OUTPUT
    format.fmt.pix.pixelformat = fmt
    format.fmt.pix.width = width
    format.fmt.pix.height = height
    format.fmt.pix.field = V4L2_FIELD_NONE
    format.fmt.pix.bytesperline = width * 2
    format.fmt.pix.sizeimage = width * height * 2
    format.fmt.pix.colorspace = V4L2_COLORSPACE_JPEG
    print "set format result", (fcntl.ioctl(device, VIDIOC_S_FMT, format))
    return format

def ConvertToYUYV(image):
    imsize = image.shape[0] * image.shape[1] * 2
    buff = np.zeros((imsize), dtype=np.uint8)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2YUV).ravel()
    Ys = np.arange(0, img.shape[0], 3)
    Vs = np.arange(1, img.shape[0], 6)
    Us = np.arange(2, img.shape[0], 6)
    BYs = np.arange(0, buff.shape[0], 2)
    BUs = np.arange(1, buff.shape[0], 4)
    BVs = np.arange(3, buff.shape[0], 4)

    buff[BYs] = img[Ys]
    buff[BUs] = img[Us]
    buff[BVs] = img[Vs]

    return buff

def drawIm(x, y, s_img, frame, w, h):
    try:
        s_img = cv2.resize(s_img, (w, h+80))
        for c in range(0, 3):
            frame[y:y+s_img.shape[0], x:x+s_img.shape[1],
            c] = s_img[:, :, c] * (s_img[:, :, 3]/255.0
            ) + frame[y:y+s_img.shape[0], x:x+s_img.shape[1], c
            ] * (1.0 - s_img[:, :, 3]/255.0)
    except ValueError:
        pass

format = config_device(device)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
                                        gray,
                                        scaleFactor=1.1,
                                        minNeighbors=5,
                                        minSize=(30, 30),
                                        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
                                        )
    # frame = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=3)
    # frame = cv2.Laplacian(frame,cv2.CV_32F)
    # frame[:,:,:]=255-frame[:,:,:] #- negative
    # frame[:,:,1:3] = np.logical_xor(frame[:,:,1:3],1)
    # frame = cv2.blur(frame,(cv2.getTrackbarPos('ofst','Video')+1,
    # cv2.getTrackbarPos('ofst','Video')+1)) #- размытие
    # frame = cv2.boxFilter(frame, -1, (100,1)) #- размытие???
    # frame = cv2.erode(frame, (100,5)) #- nothing
    # frame = cv2.GaussianBlur(frame, (11,11), 2) #- гауссово размытие
    # frame = cv2.bilateralFilter(frame,9,75,75)
    for (x, y, w, h) in faces:
        y -= cv2.getTrackbarPos('ofstY', 'Video')
	x += 50 - cv2.getTrackbarPos('ofstX', 'Video')
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        drawIm(x, y, s_img, frame, w+cv2.getTrackbarPos('deltaX', 'Video'), h+cv2.getTrackbarPos('deltaY', 'Video'))
    cv2.imshow('Video', frame)
    device.write(ConvertToYUYV(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
