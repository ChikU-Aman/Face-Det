import cv2
import winsound
import random
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face_cascading
Video = cv2.VideoCapture(0)
while True:
    frames, img = Video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #detecting faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
    #beem sound whenever face detected
    if len(faces) > 0:
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    random1 = random.randint(1,100)  # generating random no for image
    cv2.imshow('img',img)
    cv2.imwrite('image/{}.jpg'.format(random1),img)  #saving a image
    if cv2.waitKey(1) == ord("q"):
        break
Video.release()
cv2.destroyAllWindows()
