# OpenCV Python program to detect cars in video frame 
# import libraries of python OpenCV  
import cv2 
import os

''' 
# capture frames from a video 
cap = cv2.VideoCapture('video1.mp4')




  
# Trained XML classifiers describes some features of some object we want to detect 
car_cascade = cv2.CascadeClassifier('cars.xml')

try:
  count = 0
  
  
  # loop runs if capturing has been initialized. 
  while True: 
      # reads frames from a video 
      ret, frames = cap.read()
      cv2.imwrite("./Cars/frame%d.jpg" % count, frames)     # save frame as JPEG file 
      #print(frames)
      count += 1  
      # convert to gray scale of each frames 
      gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
        
    
      # Detects cars of different sizes in the input image 
      cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
        
      # To draw a rectangle in each cars 
      for (x,y,w,h) in cars: 
          cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
      cv2.imshow('video2', frames)
      if cv2.waitKey(33) == 27:
          break


except:
  print("Video processing is done")
'''

import glob

#vidcap = cv2.VideoCapture('.mp4')
cap = cv2.VideoCapture('video1.mp4')
success,image = cap.read()
count = 0
print(success)
while success:
  print("./Frames/frame.jpg")
  cv2.imwrite("./Frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = cap.read()
  print('Read a new frame: ', success)
  count += 1

files = glob.glob('Frames/*')
for file in files:
    os.system("python yolo_opencv.py --image "+ file+" --config yolov3.cfg --weights yolov3.weights --classes yolov3.txt")


cap.release()
# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
