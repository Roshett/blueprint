import cv2
import numpy as np
blueprint = cv2.imread('img/image4.jpg', cv2.COLOR_BGR2GRAY)

# deep black color
intensity = 140

low_black = (0,0,0)
high_black = (intensity,intensity,intensity)
only_blueprint = cv2.inRange(blueprint, low_black, high_black)
cv2.imwrite('img/bp4.jpg',only_blueprint)

# blur
#kernel_size = 5
#blur_gray = cv2.GaussianBlur(only_blueprint,(kernel_size, kernel_size),0)
#cv2.imshow("blur_gray", blur_gray)

i = 0
string = ""
while i < len(only_blueprint):
    j = 0
    while j < len(only_blueprint[0]):
	if only_blueprint[i][j] == 255:
	    only_blueprint[i][j] = 1
	string = string + str(only_blueprint[i][j])
    	j = j + 1
    string = string + "\n"
    i = i + 1

file = open("map/map.txt", "w")
file.write(string) 
file.close()

print("prepare")
cv2.waitKey(0)

# working lines
#edges = cv2.Canny(only_blueprint, 0, 150)
 
#lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
 
#for line in lines:
#    x1, y1, x2, y2 = line[0]

#cv2.imshow("Blue_print", only_blueprint) 
#cv2.imshow("Edges", edges)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


