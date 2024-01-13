import numpy as np
import cv2
import os
import shutil
import time

try:
    if not os.path.exists('images'):
        os.makedirs('images')
except OSError:
    print("THERE IS AN ERROR")    

cap = cv2.VideoCapture(0) #uses cam0
imageCount = 0
lastTime = time.time()
frameInterval = 3

while (True):
    ret, frame = cap.read() #returns the frame (image in form of num py array), ret tells us if it worked
    cv2.imshow("frame",frame) #title = frame, displays frame  

    if cv2.waitKey(1) == ord('q'): #if key pressed is the end frame, exit
        break
    
    currentTime = time.time()
    
    if float(currentTime - lastTime) >= frameInterval and imageCount < 5:
        cv2.imwrite('images/frame' + str(imageCount + 1) + '.jpg', frame)
        imageCount += 1
        lastTime = currentTime
    
    if (imageCount >= 5):
        break

cap.release() # release the camera resource
cv2.destroyAllWindows()

if os.path.isdir('images'):
    shutil.rmtree('images')
