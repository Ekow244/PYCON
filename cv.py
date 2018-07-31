import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image=cv2.imread("photo.jpg",0)




resized_image=cv2.resize(image,(1000,500))
cv2.imshow("Grey",resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()