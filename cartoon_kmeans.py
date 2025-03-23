import cv2 as cv
import numpy as np

img = cv.imread('data/poke.jpg')

img = img if (img.shape[0] > 400) else cv.resize(img, None, fx=1.5, fy=1.5, interpolation=cv.INTER_LINEAR)
    
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = cv.medianBlur(gray, 5)

edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3)

img = cv.bilateralFilter(img, d=1, sigmaColor=300, sigmaSpace=300)

data = np.float32(img).reshape(-1, 3)
criteria = (cv.TermCriteria_EPS + cv.TermCriteria_MAX_ITER, 20, 0.1)
_, labels, centers = cv.kmeans(data, 12, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
clustered_img = centers[labels.flatten()].reshape(img.shape)

cartoon = cv.bitwise_and(clustered_img, clustered_img, mask=edges)

cv.imshow("Original", img)
cv.imshow("K-means cartoon image", cartoon)

cv.waitKey(0)
cv.destroyAllWindows()