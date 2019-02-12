import cv2
import numpy as np
import json

def middle(num1,num2, cf):
	num = ((num1 + num2) / 2) + cf
	return num

filename = 'img/bp3.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,9,11,0.04)
ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
#for i in range(1, len(corners)):
#    print(corners[i])
img[dst>0.1*dst.max()]=[0,0,255]
#swap place x and y
#print(img[112][225])
#print(img[20][127])
#print(img[114][129])
#print(corners[0][0])

corners_len = len(corners)
lines = []

#corner = corners[1]
#print(corner[1])

for b in range(-3,3):
	for i in range(1, len(corners)):
    		corner = (corners[i])
    		for j in range(i+1, len(corners)):
    			x = int(round(middle(corner[0],corners[j][0],b)))
			y = int(round(middle(corner[1],corners[j][1],b)))
			if(img[y][x][2] != 0):
				x1 = int(round(corner[0]))
				y1 = int(round(corner[1]))
				x2 = int(round(corners[j][0]))
				y2 = int(round(corners[j][1]))
				lines.append([x1,y1,x2,y2])
				#lines.append([corner[0],corner[1],corners[j][0],corners[j][1]])


#uniques = np.unique(lines)
data = json.dumps({'lines' : lines})
print(data)
file = open("data/data.json", "w")
file.write(data) 
file.close()

#for i in range(0, len(lines)):
#    print(lines[i])




#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows
