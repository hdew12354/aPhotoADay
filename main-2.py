print("go")
#[Claire]: i know i can import multiple on one line, i just wanna see which mod takes the longest, probs gonna be cv2 tho
print("importing numpy")
import numpy as np
print("importing cv2")
import cv2
print("importing sys")
import sys
print("importing time")
import time
print("importing datetime from datetime")
from datetime import datetime
print("importing timedelta from datetime")
from datetime import timedelta as deltatime
print("importing keyboard")
import keyboard
print("finished importing")
alreadyDoneTodaysPic = False
roboName = Claire
###<DEFS>###

def savePic(alreadyDoneTodaysPic, frame, faceCount):
    # Display the resulting frame
    print("about to cv2.imshow")
    cv2.imshow('Video', frame)
    print("about to cv2.imwrite")
    cv2.imwrite('DailyPhotos//Day ' +
                str(datetime.now().day) + "-" +
                str(datetime.now().month) + "-" +
                str(datetime.now().year) + "---" +
                str(datetime.now().hour) + "-" +
                str(datetime.now().minute) + "-" +
                str(datetime.now().second) + "-fc:" +
                str(faceCount) + '.png',frame)
    print("about to set already ykwim to true")
    alreadyDoneTodaysPic = True
    return alreadyDoneTodaysPic
    
def checkTime(timeLookStart, timeLookEnd):
    
    now = datetime.now()
    #this took so fucking long to get working
    if(timeLookStart < now.hour < timeLookEnd):
        print("time in range " + str(timeLookStart) + " to " + str(timeLookEnd))
        return True
    else:
        print("time NOT in range " + str(timeLookStart) + " to " + str(timeLookEnd))
        return False
    
def setup():    
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    try:
        video_capture = cv2.VideoCapture(sys.argv[1])
        return video_capture
    except:
        print("going to try to use webcam")
        video_capture = cv2.VideoCapture(0)
        print(str(video_capture))
        return video_capture, faceCascade

###</DEFS>###
        

while True:
    if (checkTime(0, 1)):
        alreadyDoneTodaysPic = False
        print("set already done todays pic to false")
    else:
        #do nothing
        pass
    if(checkTime(0, 23)): #normally it's 7, 11 but it's what it is atm for testing
        
        if(alreadyDoneTodaysPic == False): 
            
            video_capture, faceCascade = setup()
            
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            #print(str(frame))
            try:
                print("about to cv2.cvtColor")
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                print("about to faces = faceCascade.detetMultiScale")
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.15,
                    minNeighbors=2,
                    minSize=(30, 30)
                )
                
                print("about to for (x,y,h,w) in faces")
                # Draw a rectangle around the faces
                for (x, y, w, h) in faces:
                    print("about to cv2.rectangle(vars, fuck you)")
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                try:
                    print(type(faces))
                    print(type(faces[0]))
                    print("~~~~~~")
                    print("Number of faces detected: " + str(faces.shape[0]))
                    print("[" + roboName + "]: Hello!")
                    video_capture.release()
                    alreadyDoneTodaysPic = savePic(alreadyDoneTodaysPic, frame, faces.shape[0])
                except IndexError:
                    print("index error, assuming this means no face detected, if you're certain there was a face in shot that it should've found, mess with the minNeighbors variable, it's kinda like the sensitivity option for the face recognition")
                    video_capture.release()
                except SyntaxError:
                    print ("faces.shape[0] AttributeError: 'tuple' object has no attribute 'shape', release vc to be safe")
                    video_capture.release()
                






            except cv2.error:
                print("eof")
                video_capture.release()
                break
        else:
            print("[" + roboName + "]: I'm sure you look amazing, but I've already taken today's pic!")
            now = datetime.now()
            tomorrow = datetime.now() + deltatime(1)
            targetTime = datetime(year=tomorrow.year, month = tomorrow.month, day = tomorrow.day, hour = 6, minute = 0, second = 0)
            waitTime = (targetTime - now).seconds
            print("[" + roboName + "]: darn, i'm tired, i'm gonna nap for " + str(waitTime) + " seconds, goodnight. [-, -]...zzzZZZ")
            
            while(waitTime != 0):
                if (keyboard.read_key() != None):
                    #wake up
                    waitTime = 0
                    print("[" + roboName + "]: [*^*] yes? oh you want me to go again? ok!")
                    alreadyDoneTodaysPic = False
                else:                        
                    time.sleep(1)
                    waitTime = waitTime - 1
            
    else:
        print("returned false in checkTime()")
        time.sleep(5)
# When everything is done, release the capture
print("releasign capture and destroying windows")
video_capture.release()
cv2.destroyAllWindows()

print("reached end")
