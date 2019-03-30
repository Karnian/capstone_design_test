#import os
import cv2
import numpy as np

def get_color(img, height, weight):
    color_list = []

    for i in range(0, 30):
        for j in range(0, 30):
            rgb = [img[i][j][0], img[i][j][1], img[i][j][2]]
            print(sum(rgb))
            if sum(rgb) != 0:
                if len(color_list) == 0:
                    color_list.append(rgb)
                elif rgb not in color_list:
                    color_list.append(rgb)

    print(color_list)

img = cv2.imread("./test_file/U.png", cv2.IMREAD_COLOR)

#print(img)

height = img.shape[0]
weight = img.shape[1]
#print(height , weight)

get_color(img, height, weight)

for i in range(0, 30):
    for j in range(0, 30):
        rgb = [img[i][j][0], img[i][j][1], img[i][j][2]]
#img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#lower_blue = (10, 140, 50)
#upper_blue = (15, 150, 60)
#img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

#img_result = cv2.bitwise_and(img, img, mask = img_mask)


#cv2.imshow('img_color', img)
#cv2.imshow('img_mask', img_mask)
#cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()