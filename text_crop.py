#import os
import cv2
import numpy as np

x = 0
y = 0

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
    return color_list

img = cv2.imread("./test_file/CurrentImage.png", cv2.IMREAD_COLOR)

#print(img)

height = img.shape[0]
weight = img.shape[1]
#print(height , weight)

list = get_color(img, height, weight)

for i in range(0, 30):
    for j in range(0, 30):
        if img[i][j][0] == 14 and img[i][j][1] == 146 and img[i][j][2]:
            x, y = i, j

color = img[x, y]

one_pixel = np.uint8([[color]])
hsv = cv2.cvtColor(one_pixel, cv2.COLOR_BGR2HSV)
hsv = hsv[0][0]
lower_blue1 = 0
upper_blue1 = 0
lower_blue2 = 0
upper_blue2 = 0
lower_blue3 = 0
upper_blue3 = 0
if hsv[0] < 10:
    print("case1")
    lower_blue1 = np.array([hsv[0]-10+180, 30, 30])
    upper_blue1 = np.array([180, 255, 255])
    lower_blue2 = np.array([0, 30, 30])
    upper_blue2 = np.array([hsv[0], 255, 255])
    lower_blue3 = np.array([hsv[0], 30, 30])
    upper_blue3 = np.array([hsv[0]+10, 255, 255])
    #     print(i-10+180, 180, 0, i)
    #     print(i, i+10)

elif hsv[0] > 170:
    print("case2")
    lower_blue1 = np.array([hsv[0], 30, 30])
    upper_blue1 = np.array([180, 255, 255])
    lower_blue2 = np.array([0, 30, 30])
    upper_blue2 = np.array([hsv[0]+10-180, 255, 255])
    lower_blue3 = np.array([hsv[0]-10, 30, 30])
    upper_blue3 = np.array([hsv[0], 255, 255])
    #     print(i, 180, 0, i+10-180)
    #     print(i-10, i)
else:
    print("case3")
    lower_blue1 = np.array([hsv[0], 30, 30])
    upper_blue1 = np.array([hsv[0]+10, 255, 255])
    lower_blue2 = np.array([hsv[0]-10, 30, 30])
    upper_blue2 = np.array([hsv[0], 255, 255])
    lower_blue3 = np.array([hsv[0]-10, 30, 30])
    upper_blue3 = np.array([hsv[0], 255, 255])

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_mask1 = cv2.inRange(img_hsv, lower_blue1, upper_blue1)
img_mask2 = cv2.inRange(img_hsv, lower_blue2, upper_blue2)
img_mask3 = cv2.inRange(img_hsv, lower_blue3, upper_blue3)
img_mask = img_mask1 | img_mask2 | img_mask3


img_result = cv2.bitwise_and(img, img, mask = img_mask)


cv2.imshow('img_color', img)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()