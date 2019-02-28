import cv2
import numpy as np

img = cv2.imread('img/fig2.png')
cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blueprint = cv2.imread('img/fig2.png', cv2.COLOR_BGR2HSV)
cv2.imshow("blueprint", blueprint) 	
cv2.waitKey()
cv2.destroyAllWindows()
lower_red = np.array([0,0,50])
upper_red = np.array([10,10,255])
only_blueprint = cv2.inRange(blueprint, lower_red, upper_red)
cv2.imshow("Only blueprint", only_blueprint) 	
cv2.waitKey()
cv2.destroyAllWindows()

gray = np.float32(only_blueprint)
dst = cv2.cornerHarris(gray,15,17,0.04)
ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
print(corners)
dest = abs(int(corners[1][0]) - int(corners[2][0]))
print(dest)
coef = 10 / float(dest)
print(coef)


#img[dst>0.1*dst.max()]=[0,0,105]
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows
