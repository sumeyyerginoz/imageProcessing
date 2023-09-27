import cv2
# The file name should not contain Turkish characters.

img = cv2.imread("/Users/sumeyye/Desktop/artifical intellegent/image deep learning /imageReadingSaving/image.png",0) # Reads the image in a single channel (grayscale)=(0)
#print(img)



### Resizing the image without distorting its aspect ratio ###

def resizewithAspectRatio (img,width=None,height=None,inter=cv2.INTER_AREA):
   
    dimension=None
    (h,w)=img.shape[:2]
    
    if width is None and height is None:
        return img
        
    if width is None:
        r=height/float(h)
        dimension=(int(w*r),height)
        
    else:
        r=width/float(w)
        dimension=(width,int(h*r))
        
    return (cv2.resize(img, dimension,interpolation=inter))

    
#img=cv2.resize(140,140)  # Can resize the image to the desired dimensions

cv2.namedWindow("image",cv2.WINDOW_NORMAL)  # To allow the window to be resizable

cv2.imshow("image",img) # Name of the window where the image will be displayed, and the variable


#cv2.imwrite("...",img) # To save the image, provide the file path("...")

cv2.waitKey(0)
cv2.destroyAllWindows() # # To close all windows

