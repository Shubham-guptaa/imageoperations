import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("edged", edged)

(_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2
.CHAIN_APPROX_SIMPLE)
print("I count %d contours in this image" % (len(cnts)))

newimage = image.copy()
cv2.drawContours(newimage, cnts, -1, (0, 255, 0), 2)
cv2.imshow("image with contour drawn", newimage)
cv2.waitKey(0)