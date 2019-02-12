import cv2
import numpy as np
blueprint = cv2.imread('img/bp.png')

edges = cv2.Canny(blueprint,1,2,apertureSize = 7)
cv2.imshow('edges',edges)
cv2.waitKey(0)

minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength,maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(blueprint,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('hough',blueprint)
cv2.waitKey(0)
