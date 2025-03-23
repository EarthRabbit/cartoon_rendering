import cv2 as cv
import numpy as np

img = cv.imread('data/kyosu.jpg')
 
img = img if (img.shape[0] > 600) else cv.resize(img, None, fx=1.5, fy=1.5, interpolation=cv.INTER_LINEAR)
 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 
gray = cv.medianBlur(gray, 3)

edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3)

color = cv.bilateralFilter(img, 9, 300, 300)

cartoon = cv.bitwise_and(color, color, mask=edges)

cv.imshow("Original", img)
cv.imshow("Cartoon", cartoon)

cv.waitKey(0)
cv.destroyAllWindows()