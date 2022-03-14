import cv2
import numpy as np


width=1280
height=720
fps=120

fourcc=cv2.VideoWriter_fourcc(*'MJPG')
outvid1 = cv2.VideoWriter('output2.avi',fourcc,fps,(width,height),isColor=True)


frame=np.zeros((height,width,3),dtype=np.uint8)


b,g,r=0,0,0
for k in range(120):
    b+=2
    g+=2
    r+=2
    frame[0:height,0:width,0]=b
    frame[0:height,0:width,1]=g
    frame[0:height,0:width,2]=r
    outvid1.write(frame)


u=0
q=width/200
for k in range(205):
    #frame=np.zeros((height, width, 3),dtype=np.uint8)
    b=240
    g=240
    r=240
    frame[0:round(height/3),0:round(u),0]=b
    frame[0:round(height/3),0:round(u),1]=0
    frame[0:round(height/3),0:round(u),2]=0

    frame[round(height/3):round(2*height/3),0:round(u),0]=0
    frame[round(height/3):round(2*height/3),0:round(u),1]=g
    frame[round(height/3):round(2*height/3),0:round(u),2]=0

    frame[round(2*height/3):height,0:round(u),0]=0
    frame[round(2*height/3):height,0:round(u),1]=0
    frame[round(2*height/3):height,0:round(u),2]=r

    outvid1.write(frame) #write frame
    u+=q

    
for k in range(200):
    frame[0:round(height/3),0:width,0]-=2
    frame[round(height/3):round(2*height/3),0:width,1]-=2
    frame[round(2*height/3):round(height),0:width,2]-=2
    outvid1.write(frame)

outvid1.release()


















    

