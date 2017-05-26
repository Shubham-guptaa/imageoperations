import blur
import argparse
import numpy as np
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image=imutils.resize(image, 400)

cv2.imshow("Original", image)

#for average blur
blurred=blur.average(image)

#for gaussian blur
gblurred=blur.gaussian(image)

#for median blur
mblurred=blur.median(image)

#for bilateral blur
bblurred=blur.bilateral(image)

cv2.imshow("averaged", blurred)
cv2.imshow("gaussian", gblurred)
cv2.imshow("median", mblurred)
cv2.imshow("bilateral", bblurred)
cv2.waitKey(0)













