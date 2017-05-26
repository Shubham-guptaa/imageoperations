import cv2

class BodyDetector:
    def __init__(self, bodyCascadePath):
	    
	
        self.bodyCascade = cv2.CascadeClassifier(bodyCascadePath)

    def detect(self, image, scaleFactor = 1.1, minNeighbors = 5,
    minSize = (30,30)):
        rects = self.bodyCascade.detectMultiScale(image,
        scaleFactor = scaleFactor,
        minNeighbors = minNeighbors, minSize = minSize,
        flags = cv2.CASCADE_SCALE_IMAGE)

        return rects