#Guardar video
#Paredes Márquez Carlos
#30 09 2021

import cv2
from time import sleep

cap = cv2.VideoCapture('prueba.mkv')

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#out = cv2.VideoWriter('output.mp4', fourcc, 30, (w,h))

while cap.isOpened():
    ret, im = cap.read()    
    if ret == False:
        break
    #cv2.rectangle(im, (200,100), (600,500), (0,0,255), 3)
    cv2.imshow('imagen', im)
    #out.write(im)
    
    if cv2.waitKey(1) == 27:
        break
    sleep(1/30)