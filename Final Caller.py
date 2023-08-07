
import glob
import cv2
import os

#vidcap = cv2.VideoCapture('.mp4')
cap = cv2.VideoCapture('input3(jump).mp4')
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
    
    src = cv2.imread(file)
    image = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)
    #cv2.imwrite(file,image)
    cv2.imwrite(file,src)
    
    os.system("python run_image.py --image "+ file)
