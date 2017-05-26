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


	
	
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

	
	
	
	

