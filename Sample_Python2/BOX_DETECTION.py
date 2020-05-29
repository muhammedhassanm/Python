import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
IMAGE_PATH =r'C:/Users/Muhammed Hassan M/Desktop/Images/TIF_102_Table_14.jpg'   

def display_img(image):
    fig = plt.figure(figsize=(20,16))
    ax = fig.add_subplot(111)
    ax.imshow(image, cmap="gray")
    
def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))

    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)

def box_extraction(img_for_box_extraction_path):

    img = cv2.imread(img_for_box_extraction_path, 0)  # Read the image
    (thresh, img_bin) = cv2.threshold(img, 128, 255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Thresholding the image
    img_bin = 255-img_bin  # Invert the image

    cv2.imwrite("Image_bin.jpg",img_bin)
   
    # Defining a kernel length
    kernel_length = np.array(img).shape[1]//40
     
    # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
    verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    # A kernel of (3 X 3) ones.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Morphological operation to detect verticle lines from an image
    img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
    verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
    cv2.imwrite("verticle_lines.jpg",verticle_lines_img)

    # Morphological operation to detect horizontal lines from an image
    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
    cv2.imwrite("horizontal_lines.jpg",horizontal_lines_img)

    # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
    alpha = 0.5
    beta = 1.0 - alpha
    # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
    img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
    img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
    (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#    bitxor = cv2.bitwise_xor(img,img_final_bin)
#    bit_not = cv2.bitwise_not(bitxor)
    # For Debugging
    # Enable this line to see verticle and horizontal lines in the image which is used to find boxes
    cv2.imwrite("img_final_bin.jpg",img_final_bin)
    # Find contours for image, which will detect all the boxes
    _,contours, hierarchy = cv2.findContours(
        img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Sort all the contours by top to bottom.
    (contours, boundingBoxes) = sort_contours(contours, method="top-to-bottom")

    idx = 0
    for c in contours:
        # Returns the location and width,height for every contour
        x, y, w, h = cv2.boundingRect(c)
        if w>100:
        # If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
    
            idx += 1
            new_img = img[y:y+h, x:x+w]
            
            new_img = cv2.resize(new_img,None,fx=2.5,fy=2.5,interpolation=cv2.INTER_LINEAR)
            retval, thresh_gray = cv2.threshold(new_img,thresh=200, maxval=255,type=cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)
            cv2.bitwise_not(thresh_gray,thresh_gray)
#            kernel for dilate and erode = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            kernel = np.ones((3,3), np.uint8)
            new_img = cv2.dilate(thresh_gray, kernel, iterations=1)
            new_img = cv2.erode(new_img, kernel, iterations=1)
#            new_img = cv2.adaptiveThreshold(cv2.bilateralFilter(new_img,9,75,75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            new_img = cv2.GaussianBlur(new_img,(3,3),1)
            
            cv2.imwrite(str(idx) + '.png', new_img)
            text =  pytesseract.image_to_string(new_img,config=r'--psm 6')
#            -c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz
            print(text)
#     For Debugging#    Enable this line to see all contours.
    cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
    cv2.imwrite("img_contour.jpg", img)


box_extraction(IMAGE_PATH)