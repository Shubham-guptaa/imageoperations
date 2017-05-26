import numpy as np
import argparse
import cv2
import imutils


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

rotated = imutils.rotate(image, 180, scale=0.5)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)