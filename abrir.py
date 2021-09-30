#Abrir video
#Paredes Márquez Carlos
#29 09 2021

import cv2
from time import sleep

cap = cv2.VideoCapture('prueba.mkv')

while cap.isOpened():
    ret, im = cap.read()    
    if ret == False:
        break
    cv2.imshow('imagen', im)
    
    if cv2.waitKey(1) == 27:
        break
    sleep(1/30)