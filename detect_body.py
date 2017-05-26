from facedetector import FaceDetector
import cv2
import argparse
ap = argparse.ArgumentParser()

ap.add_argument("-b", "--body", required = True,
help = "path to where the face cascade resides")
ap.add_argument("-i", "--image", required = True,
help = "path to where the image file resides")

args= vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)




fd = FaceDetector(args["body"])
faceRects = fd.detect(gray, scaleFactor=1.01, minNeighbors =1 , minSize =(10,10))
print(faceRects)
for (x, y, w, h) in faceRects:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
  
	
	
	
	
	
	
	
	
cv2.imshow("body", image)
cv2.waitKey(0)