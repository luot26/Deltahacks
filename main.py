import numpy as np
import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt

def emotion_capture(frame): #will return dominant emotion type

    # identify face from image, prep for deepface model
    face_model= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face= face_model.detectMultiScale(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),1.1,5)
    # loop through each detected face, draw a rect and display dominant emotion
    for x,y,width,height in face:
        emotion = DeepFace.analyze(frame,actions=["emotion"],enforce_detection=False)
        # dictionary
        cv2.putText(frame, (emotion[0].get('dominant_emotion')),(x,y+height),
        cv2.FONT_HERSHEY_COMPLEX, 0.9, (255,255,0),2 )
        cv2.rectangle(frame, (x,y) , (x + width, y+ height), ( 255,255,0),2 )
    # Check the response
        
    cv2.imshow("Computer Vision",frame) #title = frame, displays frame
    

cap = cv2.VideoCapture(0) #number of webcam being used, 0 = first cam (only one we have)
while True:
    
    ret, frame = cap.read() #returns the frame (image in form of num py array), ret tells us if it worked
    emotion_capture(frame) # capture the emotion displayed in the frame
    if cv2.waitKey(1) == ord('q'): #if key pressed is the end frame, exit
        break


cap.release # release the camera resource
cv2.destroyAllWindows()

