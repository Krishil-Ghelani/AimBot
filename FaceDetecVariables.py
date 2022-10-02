import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)


Face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_defult.xml')
upper_body = cv2.CascadeClassifier('upperbody.xml')




while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = Face_cascade.detectMultiScale(gray, 1.1, 4)
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    UPPER_BODY = upper_body.detectMultiScale(gray, 1.1, 4)
    UBRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        print("x=",x,"y=", y)

    cv2.imshow("Image",img)
    cv2.imshow('imageUpperBody', UBRGB)
    cv2.waitKey(1)