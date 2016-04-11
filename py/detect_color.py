import cv2
import numpy as np

cv2.namedWindow('Video')
video_capture = cv2.VideoCapture(0)
video_capture.set(3, 750)
video_capture.set(4, 750)
video_capture.set(5, 15)
while True:
    ret, frame = video_capture.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    frame = cv2.GaussianBlur(frame, (3,3), 2)
    fr,fr1,fr2 = cv2.split(frame)
    fr3=np.copy(fr)
    cv2.bitwise_and(fr,fr1,fr3)
    cv2.bitwise_and(fr3,fr2,fr3)
    cv2.imshow('Video',fr3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
