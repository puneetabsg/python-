import cv2

# here we are providing image for comparision with cascaded algo. ie for face 
# detection only in this  case.

imagePath ="abba.png"

# this is our algo for face detection in following path.

cascPath = "C:\\Users\\pk112\\Downloads\\opencv\\build\etc\\haarcascades\\haarcascade_frontalface_default.xml"


# here we are just loading our image for detection
# this is face cascade which is having xml  file containing data necessary
# for face detection.
 
faceCascade = cv2.CascadeClassifier(cascPath)

# here we are reading our file and converting our file into GRAY SCALE.
# because our algo works on gray model which is easy for various colors photo.

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# so now this is key code of our program which actually is detecting face in photos.
# detectMultiScale is function that detects objects-----and
# here we are calling it on particular face detection program.
# scale factor is used for objects which are very close to camera
# and make it at reasonable distance from our algo.
# minNeighbors-- is used for detecting more than one object near the 
# current found object ie: our detected face.


face = faceCascade.detectMultiScale(gray, scaleFactor = 1.1,minNeighbors = 5, minSize =(30,30))

# this loop function make rectangles on founded face according to it.
# and continue to search for more faces next to detected face box.
# this loop also provides 4 values ie;
# the x and y location of the rectangle, 
# and the rectangle’s width and height (w , h)
# we use built-in rectangle() function for making rectangle around the faces.

for (x,y,w,h) in face:
    cv2.rectangle(image, (x,y), (x+w,y+h),(0,255,0),2)
cv2.imshow("Faces found", image)
cv2.waitKey(0)