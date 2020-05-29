import cv2
import numpy as np
import matplotlib.pyplot as plt 
IMAGE_PATH ='C:/Users/Muhammed Hassan M/Desktop/Images/TIF_35_Table_6.jpg'   
img = cv2.imread(IMAGE_PATH)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# a little helper function to display our image in a bigger plot
def display_img(image):
    fig = plt.figure(figsize=(20,16))
    ax = fig.add_subplot(111)
    ax.imshow(image, cmap="gray")

img = cv2.bitwise_not(img)
th2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)

cv2.imwrite("th2.jpg", th2)
display_img(th2)

horizontal = th2
vertical = th2
rows,cols = horizontal.shape

#inverse the image, so that lines are black for masking
horizontal_inv = cv2.bitwise_not(horizontal)
#perform bitwise_and to mask the lines with provided mask
masked_img = cv2.bitwise_and(img, img, mask=horizontal_inv)
#reverse the image back to normal
masked_img_inv = cv2.bitwise_not(masked_img)

cv2.imwrite("result2.jpg", masked_img_inv)
display_img(masked_img_inv)


horizontalsize = int(cols / 30)
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize,1))
horizontal = cv2.erode(horizontal, horizontalStructure, (-1, -1))
horizontal = cv2.dilate(horizontal, horizontalStructure, (-1, -1))

cv2.imwrite("horizontal.jpg", horizontal)
display_img(horizontal)
#=============================================================

import cv2

image = cv2.imread(IMAGE_PATH)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Remove horizontal
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,1))
detected_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(image, [c], -1, (255,255,255), 2)
#    display_img(image)
# Repair image
repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,6))
result = 255 - cv2.morphologyEx(255 - image, cv2.MORPH_CLOSE, repair_kernel, iterations=2)

cv2.imshow('thresh', thresh)
cv2.imshow('detected_lines', detected_lines)
cv2.imshow('image', image)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()