import cv2
import numpy as np
import json

def middle(num1,num2, cf):
	num = ((num1 + num2) / 2) + cf
	return num

def fourth(num1,num2, cf):
	num = ((num1 + num2) / 4) + cf
	return num

filename = 'img/bp_fig2.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,9,11,0.05)
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

for b in range(-5,5):
	for i in range(1, len(corners)):
    		corner = (corners[i])
    		for j in range(i+1, len(corners)):
    			x = int(round(middle(corner[0],corners[j][0],b)))
			y = int(round(middle(corner[1],corners[j][1],b)))
			x1 = int(round(middle(corner[0],x,b)))
			y1 = int(round(middle(corner[1],y,b)))
			x2 = int(round(middle(x,corners[j][0],b)))
			y2 = int(round(middle(y,corners[j][1],b)))
			if(img[y][x][2] != 0 and img[y1][x1][2] != 0 and img[y2][x2][2] != 0):
				x1 = int(round(corner[0]))
				y1 = int(round(corner[1]))
				x2 = int(round(corners[j][0]))
				y2 = int(round(corners[j][1]))
				lines.append([x1,y1,x2,y2])

lines_f = []
for b in range(-3,3):
	for i in range(1, len(corners)):
    		corner = (corners[i])
    		for j in range(i+1, len(corners)):
			x = int(round(middle(corner[0],corners[j][0],b)))
			y = int(round(middle(corner[1],corners[j][1],b)))
			x1 = int(round(middle(x,corners[j][0],b)))
			y1 = int(round(middle(y,corners[j][1],b)))
			if(img[y][x][2] != 0 and img[y1][x1][2] != 0):
				x1 = int(round(corner[0]))
				y1 = int(round(corner[1]))
				x2 = int(round(corners[j][0]))
				y2 = int(round(corners[j][1]))
				lines_f.append([x1,y1,x2,y2])

#uniques = np.unique(lines)
#print(len(lines))
#del lines[]
#np.delete(lines, 2, axis=1)
#print(len(lines))

#print(lines[0],lines[4])
#if(lines[0] == lines[4]):
#	print('azazaz')


def tuples(A):
    try: return tuple(tuples(a) for a in A)
    except TypeError: return A
b = set(tuples(lines))
c = set(tuples(lines_f))
print(len(b))
print(len(c))


l = []
for z in range(0, len(b)):
	l.append(b.pop())

data = json.dumps({'lines' : l})
print(data)
file = open("data/data.json", "w")
file.write(data) 
file.close()


#print(len(lines))
#for i in range(0, len(lines):
#	indexes = []
#	for j in range(i + 1, len(lines)):
#		if(lines[i] == lines[j]):
#			indexes.append(j)

#for b in range(0, len(indexes)):
#	print(indexes[b])
#	del lines[indexes[b]]		

#new_array = [tuple(row) for row in lines]
#uniques = np.unique(new_array)
#print(uniques)

#print(lines)
		
	


#data = json.dumps({'lines' : lines})
#print(data)
#file = open("data/data.json", "w")
#file.write(data) 
#file.close()

#for i in range(0, len(lines)):
#    print(lines[i])




cv2.imshow('image', img)
cv2.waitKey(0)
#cv2.destroyAllWindows
