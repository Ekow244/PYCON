import cv2
import time


first_frame= None

video=cv2.VideoCapture(0)

a=0


while True:      #check frame for different objects
    a=a+1
    check, frame = video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)  #Apply a gaussian blur to image to smooth, it remove noise and increase accuracy for processing

    if first_frame is None:
       first_frame=gray
       continue


    delta_frame=cv2.absdiff(first_frame,gray)

    threshhold=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]

    threshhold=cv2.dilate(threshhold,None,iterations=2)


#
    (_,cnts,_)=cv2.findContours(threshhold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    #cv2.imshow("Capturing", gray)  #frame variable replaces gray if we wanna keep it in color
    #cv2.imshow("Delta Frame",delta_frame)
    #cv2.imshow("Threshold",threshhold)
    cv2.imshow("Color Frame",frame)


    key=cv2.waitKey(1)

    print(gray)#remove/replace with frame
    print(delta_frame)

    if key==ord('q'):
        break

print(a)

video.release()

cv2.destroyAllWindows
