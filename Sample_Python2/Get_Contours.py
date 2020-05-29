
import cv2
import os 
import glob 
# READ IMAGE
#Img = cv2.imread('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/TIF/TIF_14.tif')

for image in glob.glob('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/TIF/*.tif'):
    print(image)
    basename = os.path.splitext(os.path.basename(image))[0]
    if not os.path.isdir('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/New folder/'+basename):
        os.mkdir('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/New folder/'+basename)


#if not Img is None:
    # CONVERT TO GRAYSCALE
    image = cv2.imread(image)
    Im_Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # APPLY INVERSE BINARY THRESHOLDING
    Ret, Thresh = cv2.threshold(Im_Gray, 180, 255, cv2.THRESH_BINARY_INV)
    
    # FIND THE CONTOURS AND SORT THEM IN THE REVESE ORDER OF AREA
    _,Contours, Hierarchy = cv2.findContours(Thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Contours_Sorted = sorted(Contours, key=cv2.contourArea, reverse = True)

    Coordinates = []
    # GET THE TOP 15 CONTOURS
    for In, Cnt in enumerate(Contours_Sorted[:15]):
        X, Y, W, H = cv2.boundingRect(Cnt)
        Coordinates.append((X, Y, W, H))
        cv2.rectangle(image, (X,Y), (X+W, Y+H), (0,0,255), 1)
        cv2.imwrite('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/New folder/'+basename+'/'+basename+'_Table_'+ str(In) + '.jpg', image[Y:Y+H, X:X+W])
