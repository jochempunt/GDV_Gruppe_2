from ast import For
from audioop import avg
import math
from statistics import median
import cv2
import numpy as np

import os

#delacrations
hue = 100 # 30 :yellow 40:green pink:0
hue_range = 13
saturation = 150 
saturation_range = 200 # 100 is yellow #200 is blue
value = 200
value_range = 100
lower_blue = np.array([hue - hue_range, saturation -
                       saturation_range, value - value_range])
upper_blue = np.array([hue + hue_range, saturation +
                       saturation_range, value + value_range])

# load all chewing gum ball images
chewing_gum_img_list = []
img_list = os.listdir("images")
for img in img_list:
    if "chewing" in img:
        chewing_gum_img_list.append(img)

for img_string in chewing_gum_img_list:
    img = cv2.imread( 'images\\'+ img_string, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (800, 600))

    # convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # create a mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)




    def morph_shape(val):
        if val == 0:
            return cv2.MORPH_RECT
        elif val == 1:
            return cv2.MORPH_CROSS
        elif val == 2:
            return cv2.MORPH_ELLIPSE


    def erosion(shape, kernelsize, image):
        kernl_element = cv2.getStructuringElement(shape, (2 * kernelsize + 1, 2 * kernelsize + 1), (kernelsize, kernelsize))
        return cv2.erode(image, kernl_element)


    def dilatation(shape, kernelsize, image):
        kernl_element = cv2.getStructuringElement(shape, (2 * kernelsize + 1, 2 * kernelsize + 1), (kernelsize, kernelsize))
        return cv2.dilate(image, kernl_element)


    def opening(shape, kernelsize, image):
        image = erosion(shape, kernelsize, image)
        return dilatation(shape, kernelsize, image)


    def closing(shape, kernelsize, image):
        image = dilatation(shape, kernelsize, image)
        return erosion(shape, kernelsize, image)


    kernel_size = 8
    kernel_shape = morph_shape(2)
    mask = opening(kernel_shape, kernel_size, mask)
    mask = erosion(kernel_shape, kernel_size, mask)
    kernel_size = 4
    mask = dilatation(kernel_shape, kernel_size, mask)


    # find connected components
    connectivity = 8
    (numLabels, labels, stats, centroids) = cv2.connectedComponentsWithStats(mask, connectivity, cv2.CV_32S)

    component_size_min = 11
    component_counter = 0
    green = (0, 255, 0)

    # area_list = []

    for i in range(1, numLabels):
        height = stats[i, cv2.CC_STAT_HEIGHT]
        width = stats[i, cv2.CC_STAT_WIDTH]
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        area = stats[i, cv2.CC_STAT_AREA]

        
        
        if (height > component_size_min) and (width > component_size_min):
            component_counter += 1
            #area_list.append(area)
            cv2.rectangle(img, (x, y), (x + width, y + height), green, 3)


    # ANSATZ --> WENN 2 balls zu nahe wären und sie als eines gelten würden,
    # ist allerdings zu ungenau
    # calculate average size of alll found componanents
    """ area_list.sort()
    area_range = 300
    extra_components = 0
    area_sum = 0
    for area in area_list:
        area_sum += area
    area_avg = area_sum / len(area_list) """
    # if area size of component is bigger then average area
    # calculate the number of approximated components
    # --> this is for when multiple elements are too close to eachother
    """ for area in area_list:
        if area > area_avg + area_range:
            temp = round(area / area_avg)
            extra_components += round(area / area_avg) - 1 """




    print('We have found ' + str(component_counter) + ' blue balls in: ' + img_string)


    # show the original image with drawings in one window
    cv2.imshow('Original image', img)

    # show the mask image in another window
    cv2.imshow('Mask image', mask)

    key = cv2.waitKey(0)
    if key == ord('e'):
        continue
    elif key == ord('q'): 
        cv2.destroyAllWindows()
        break
        

# close applikation
cv2.waitKey(0)
cv2.destroyAllWindows()
