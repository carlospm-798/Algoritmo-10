#Algoritmo 10
#Paredes Márquez Carlos
#30 09 2021

import cv2
from time import sleep

im_fondo = cv2.imread('fiesta.jpg')

cap = cv2.VideoCapture('doge.mp4')

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

im_fondo = cv2.resize(im_fondo, (w,h))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('output.mp4', fourcc, 30, (w,h))

while cap.isOpened():
    ret, im = cap.read()    
    if ret == False:
        break
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    mask0 = cv2.inRange(hsv, (54, 0, 0), (63, 255, 255)) #117, 58.5
    mask = cv2.bitwise_not(mask0)
    im2 = cv2.bitwise_and(im, im, mask=mask)

    im3 = cv2.bitwise_and(im_fondo, im_fondo, mask=mask0)
    im4 = cv2.bitwise_or(im3, im2)

    cv2.imshow('imagen', im4)
    out.write(im4)
    
    if cv2.waitKey(1) == 27:
        break
    sleep(1/30)