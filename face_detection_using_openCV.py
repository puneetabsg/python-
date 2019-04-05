import cv2
imagePath ="abba.png"
cascPath = "C:\\Users\\pk112\\Downloads\\opencv\\build\etc\\haarcascades\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face = faceCascade.detectMultiScale(gray, scaleFactor = 1.1,minNeighbors = 5, minSize =(30,30))
for (x,y,w,h) in face:
    cv2.rectangle(image, (x,y), (x+w,y+h),(0,255,0),2)
cv2.imshow("Faces found", image)
cv2.waitKey(0)