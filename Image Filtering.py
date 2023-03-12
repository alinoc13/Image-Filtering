import cv2
import numpy

#refer myFunctions file
from myFunctions import addNoise
from myFunctions import linearFilter

img = cv2.imread("Resources/carrot.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgNoise = addNoise(imgGray)


imgLinearFilter = linearFilter(imgNoise,3)
imgMedianFilter = cv2.medianBlur(imgNoise,3)
imgAveragingFilter = cv2.blur(imgNoise,(3,3))
imgGaussianFilter = cv2.GaussianBlur(imgNoise,(3,3),0)

imgStack = numpy.hstack((imgNoise,imgLinearFilter,imgMedianFilter,imgAveragingFilter,imgGaussianFilter))

cv2.imshow("output",imgStack)

cv2.waitKey(0)
