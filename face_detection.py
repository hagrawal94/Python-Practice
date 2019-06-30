import cv2
img=cv2.imread('one.JPG',1)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(w+x,h+y),(0,255,0),3)
resized=cv2.resize(img,(int(img.shape[1]/7),int(img.shape[0]/7)))
cv2.imshow("Shimla",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()