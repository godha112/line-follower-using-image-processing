import numpy as np
import cv2
cap = cv2.VideoCapture(0)
def nothing(x):
    pass
cv2.namedWindow('show')
cv2.createTrackbar('h','show',0,180,nothing)
cv2.createTrackbar('s','show',0,255,nothing)
cv2.createTrackbar('v','show',0,255,nothing)
while(True):
    ret, frame = cap.read()
    fil = cv2.GaussianBlur(frame,(5,5),0)
    hsv = cv2.cvtColor(fil,cv2.COLOR_BGR2HSV)
    h = cv2.getTrackbarPos('h','show')
    s = cv2.getTrackbarPos('s','show')
    v = cv2.getTrackbarPos('v','show')
    lb = np.array([h,s,v])
    hb = np.array([120,255,255])
    mask = cv2.inRange(hsv,lb,hb)
    _, contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    res1 = cv2.drawContours(frame,contours,-1,(0,0,255),3)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow('img',res1)
    cv2.imshow('img1',mask)
    cv2.imshow('show',res)
    if(cv2.waitKey(1)&0xFF==ord(' ')):
        break
cap.release()
cv2.destroyAllWindows()
