import numpy as np
import cv2
import os
import shutil
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_face_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5, minSize=(30,30))

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (230,100,80), 2)
    
    return frame

try:
    if not os.path.exists('images'):
        os.makedirs('images')
except OSError:
    print("THERE IS AN ERROR")    

cap = cv2.VideoCapture(0) #uses cam0
image_count = 0

while image_count < 5:
    ret, frame = cap.read() #returns the frame (image in form of num py array), ret tells us if it worked

    frame_and_face = detect_face_emotion(frame)

    cv2.imshow("frame", frame_and_face) #title = frame, displays frame    
    cv2.imwrite('images/frame' + str(image_count + 1) + '.jpg', frame_and_face)
    image_count += 1
    time.sleep(3)

    if cv2.waitKey(1) == ord('q'): #if key pressed is the end frame, exit
        break

cap.release # release the camera resource
cv2.destroyAllWindows()
emotion = "happy"