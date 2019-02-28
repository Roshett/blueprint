def middle(num1,num2, cf):
	num = ((num1 + num2) / 2) + cf
	return num

def tuples(A):
    try: return tuple(tuples(a) for a in A)
    except TypeError: return A

#import libraries
import cv2
import numpy as np
import json

#Server or desktop
print('Server or desktop (s/d)')
sd = raw_input()

#read image
print('Input image name in "image" folder')
nameImg = raw_input()
blueprint = cv2.imread('img/' + nameImg, cv2.COLOR_BGR2GRAY)
print('Image read succesfully')
if (sd == 'd'):
	cv2.imshow("Blueprint", blueprint)
	cv2.waitKey()
	cv2.destroyAllWindows()

	
nameImg = 'bp_' + nameImg
answer = 'n'
while (answer != 'y'):
	print('Input intensity blackcolor (0 - 255)')
	intensity = int(raw_input())

	#filter on intensity RGB channels
	low_black = (0,0,0)
	high_black = (intensity,intensity,intensity)
	only_blueprint = cv2.inRange(blueprint, low_black, high_black)

	if (sd == 'd'):
		cv2.imshow("Only blueprint", only_blueprint) 	
		cv2.waitKey()
		cv2.destroyAllWindows()
	else:
		cv2.imwrite('img/' + nameImg,only_blueprint)
	print('That is suitable for us?(y/n)')
	answer = raw_input()
	
cv2.imwrite('img/' + nameImg,only_blueprint)
print('Image was writed "img/' + nameImg + "'")

del blueprint

# that img for drawing main dots
img = cv2.imread('img/' + nameImg)
gray = np.float32(only_blueprint)

answer = 'n'
while (answer != 'y'):
	print('data for CornerHarris formula (example "9,11,0.04") = (blockSize,kSize,harris)')
	coef = raw_input()
	coef = coef.split(',')
	blockSize = int(coef[0])
	kSize = int(coef[1])
	harris = float(coef[2])
	# finding corners
	dst = cv2.cornerHarris(gray,blockSize,kSize,harris)
	ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
	dst = np.uint8(dst)
	ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
	corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
	example = img
	example[dst>0.1*dst.max()]=[0,0,255]
	corners_len = len(corners)
	print('Corners: ' + str(corners_len))
	if (sd == 'd'):
		cv2.imshow('image', img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	else:
		cv2.imwrite('img/coord_' + nameImg,img)
	print('That is suitable for us?(y/n)')
	answer = raw_input()

print('Data generating...')
lines = []

print('Space checking angle. For example "3"')
answer = raw_input()
r1 = -1 * int(answer)
r2 = int(answer)

for b in range(r1,r2):
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

b = set(tuples(lines))
l = []
for z in range(0, len(b)):
	l.append(b.pop())

print('Dumping JSON')
data = json.dumps({'lines' : l})
file = open('data/' + nameImg + '.json', 'w')
file.write(data) 
file.close()
print('Data was writed')
