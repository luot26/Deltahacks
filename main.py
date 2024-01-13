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

while (imageCount < 5):
    ret, frame = cap.read() #returns the frame (image in form of num py array), ret tells us if it worked

    cv2.imshow("frame",frame) #title = frame, displays frame    
    cv2.imwrite('images/frame' + str(imageCount + 1) + '.jpg', frame)
    imageCount += 1
    time.sleep(3)

    if cv2.waitKey(1) == ord('q'): #if key pressed is the end frame, exit
        break

cap.release # release the camera resource
cv2.destroyAllWindows()

if os.path.isdir('images'):
    shutil.rmtree('images')