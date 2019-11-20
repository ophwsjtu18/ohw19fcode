import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

def recognize_faceneye(img):
    face_cascade = cv2.CascadeClassifier('C:\\Program Files\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('C:\\Program Files\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('jhy',img)
#cv2.waitKey(0)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        coordinate = [(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x-w,y+h),(x-w,y),(x-w,y-h),(x,y-h),(x+w,y-h)]
        for (eks,why) in coordinate:
            cv2.rectangle(frame,(eks,why),(eks+w,why+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return img


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = recognize_faceneye(frame)
    # Display the resulting frame
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #time.sleep(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


