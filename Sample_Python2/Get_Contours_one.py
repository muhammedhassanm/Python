
import cv2
import os 
import glob 
# READ IMAGE
path = 'C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/TIF/TIF_103.tif'
image = cv2.imread(path)


basename = os.path.splitext(os.path.basename(path))[0]
if not os.path.isdir('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/CONTOURS_DETECTED TIF/'+basename):
    os.mkdir('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/CONTOURS_DETECTED TIF/'+basename)


if not image is None:
    # CONVERT TO GRAYSCALE
    
    Im_Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # APPLY INVERSE BINARY THRESHOLDING
    Ret, Thresh = cv2.threshold(Im_Gray, 180, 255, cv2.THRESH_BINARY_INV)
    
    # FIND THE CONTOURS AND SORT THEM IN THE REVESE ORDER OF AREA
    _,Contours, Hierarchy = cv2.findContours(Thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Contours_Sorted = sorted(Contours, key=cv2.contourArea, reverse = True)

    Coordinates = []
    # GET THE TOP 15 CONTOURS
    for In, Cnt in enumerate(Contours_Sorted[:15]):
        area = cv2.contourArea(Cnt)
        archlength= (cv2.arcLength(Cnt,closed=True))
        print(archlength)
        if area<750000:
            X, Y, W, H = cv2.boundingRect(Cnt)
            Coordinates.append((X, Y, W, H))
            cv2.rectangle(image, (X,Y), (X+W, Y+H), (0,0,255), 1)
            cv2.imwrite('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/CONTOURS_DETECTED TIF/'+basename+'/'+'Table_'+ str(In) + '.tif', image[Y:Y+H, X:X+W])
        


