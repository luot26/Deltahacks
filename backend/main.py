import numpy as np
import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt
import time


tallys ={'angry': 0,
        'disgust': 0,
        'fear': 0,
        'happy': 0,
        'sad': 0,
        'surprise': 0,
        'neutral': 0}  


def emotion_capture(frame): #will return dominant emotion type
    emotions=[]
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
        emotions.append(emotion[0].get('dominant_emotion'))

    cv2.imshow("Computer Vision",frame) #title = frame, displays frame
    return emotions

def compute_dominant_emotion():
    max=0
    dominant_emote=''
    keys=tallys.keys() # array of all keys
    for key in keys:
        if tallys[key] > max: # see if value > max
            max=tallys[key]
            dominant_emote=key
    return dominant_emote
    

            
 
def CVLoop():
    cap = cv2.VideoCapture(0) #number of webcam being used, 0 = first cam (only one we have)
    old_time=time.time()
    new_time=time.time()
    while new_time-old_time<20:
        ret, frame = cap.read() #returns the frame (image in form of num py array), ret tells us if it worked
        emotes= emotion_capture(frame) # capture the emotion displayed in the frame

        for emote in emotes:
            tallys[emote]+=1
        
        if cv2.waitKey(1) == ord('q'): #if key pressed is the end frame, exit
            break
        new_time=time.time()
        

    cap.release # release the camera resource
    cv2.destroyAllWindows()
