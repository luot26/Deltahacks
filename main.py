import numpy as np
import cv2

cap = cv2.VideoCapture(0) #number of webcam being used, 0 = first cam (only one we have)

while True:
    ret, frame = cap.read() #returns the frame (image in form of num py array), ret tells us if it worked


    cv2.imshow("frame",frame) #title = frame, displays frame
    if cv2.waitKey(1) == ord('q'): #if key pressed is the end frame, exit
        break


cap.release # release the camera resource
cv2.destroyAllWindows()