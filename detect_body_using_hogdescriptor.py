import numpy as np
import cv2
import argparse
import imutils
ap = argparse.ArgumentParser()


ap.add_argument("-i", "--image", required = True,
help = "path to where the image file resides")

args= vars(ap.parse_args())
image = cv2.imread(args["image"])

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


#resize image to (1) reduce detection time
# and (2) improve detection accuracy
image = imutils.resize(image, width=min(400, image.shape[1]))


# detect people in the image
(rects, weights) = hog.detectMultiScale(image, winStride=(1,1),
padding=(15,15), scale=1.01)
print(rects)

# draw the original bounding boxes
for (x, y, w, h) in rects:
    pad_w, pad_h = int(0.10*w), int(0.05*h)
    cv2.rectangle(image, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), 2)
    


 




cv2.imshow("body", image)

cv2.waitKey(0)







































