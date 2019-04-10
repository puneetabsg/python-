import cv2
import numpy as np
# here we using numpy for converting image frames as array. 
# Create a VideoCapture object
# here 0 is for webcam camera usage or this is device camera index.
# if we are feeding any video then be replaced by 0 inside VideoCapture function.

cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
# isOpened() is for opening camera.

if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# fourcc-- is special video codec which detects or give default codec rate for your device video mode.
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# here codec is MJPG which is best and can be used as default codec for devices.
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
while(True):
  ret, frame = cap.read()
 
  if ret == True: 
    # this is for converting imageframes into video.
    # Write the frame into the file 'output.avi'
    out.write(frame)
 
    # Display the resulting frame- video is result of this imshow() frames collection.   
    cv2.imshow('frame',frame)
    
    # waitkey=1 will automatically adjust the frame rate of your device's camera.
    # here waitkey=0 will pause frame for infinite time which is not accepted in case for video recording.
    # Press Q on keyboard to stop recording--here waitkey()=1 for video and for images it should be 0.
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows()