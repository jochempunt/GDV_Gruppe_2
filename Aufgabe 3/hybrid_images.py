# Copy from GDV_tutorial_12.py and change three lines...
# Inspired by https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
from cmath import nan
from multiprocessing import Event
from turtle import position
import numpy as np
import cv2

# define global arrays for the clicked (reference) points
ref_pt_src = []
ref_pt_dst = []


# TODO define one callback functions for each image window
def clickSrc(event, x, y, flags, param):
    # grab references to the global variables
    global ref_pt_src
    # if the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN:
        positionCount = len(ref_pt_src)
        if( positionCount == 0):
            ref_pt_src = [(x,y)]
        else:
            ref_pt_src.append((x,y))
        
        # draw a circle around the clicked point
        cv2.circle(img_high,ref_pt_src[positionCount],3,(0,0,255),2)
        # redraw the image
        cv2.imshow("origin",img_high)

def clickDst(event, x, y, flags, param):
    # grab references to the global variables
    global ref_pt_dst
    # if the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN:
        posCount = len(ref_pt_dst)
        if(posCount == 0):
            ref_pt_dst = [(x,y)]
        else:
            ref_pt_dst.append((x,y))
        # draw a circle around the clicked point
        cv2.circle(dst_transform, ref_pt_dst[posCount],3,(0,0,255),2)
        # redraw the image
        cv2.imshow("transformed",dst_transform)


def hp_filter(_img,_sigma):
    ksize = (0,0)
    return cv2.subtract(_img,cv2.GaussianBlur(_img,ksize,_sigma))

def apply_gaussian(_img, _kernel_size):
    sigma = 6
    kernel1D = cv2.getGaussianKernel(_kernel_size, sigma)
    gaus_kernel = np.transpose(kernel1D) * kernel1D
    gaus_kernel = cv2.flip(gaus_kernel, -1)
    ddepth = -1
    return cv2.filter2D(_img, ddepth, gaus_kernel)      

# Load image and resize for better display
img_high = cv2.imread('images\\person1.jpg',cv2.IMREAD_COLOR)
img_high = cv2.resize(img_high, (400, 400), interpolation=cv2.INTER_CUBIC)

img_low = cv2.imread('images\\person4.jpg',cv2.IMREAD_COLOR)
img_low = cv2.resize(img_low, (400, 400), interpolation=cv2.INTER_CUBIC)


img_high_edited = hp_filter(img_high,10)
img_edited2 = apply_gaussian(img_low, 25)


rows, cols, dim = img_high.shape
clone_high = img_high.copy()
clone_low = img_low.copy()
dst_transform = img_low
cv2.namedWindow("origin")
cv2.setMouseCallback("origin",clickSrc)
cv2.namedWindow("transformed")
cv2.setMouseCallback("transformed",clickDst)

result_img = nan
computationDone = False
while True:
    if not(computationDone) and (len(ref_pt_src) == 3 and len(ref_pt_dst) == 3):
        T_affine = cv2.getAffineTransform(np.float32(ref_pt_src), np.float32(ref_pt_dst))
        print('\nAffine transformation:\n', '\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_affine]))
        dst_transform = cv2.warpAffine(img_high_edited, T_affine, (cols, rows))   
        dst_transform = cv2.addWeighted(dst_transform, 0.5, img_edited2, 
        0.5, 4)
        result_img = dst_transform;
       
        computationDone = True   
    cv2.imshow('origin', img_high)
    cv2.imshow('transformed', dst_transform)

    key = cv2.waitKey(1) & 0xFF   
    # TODO if the 'r' key is pressed, reset the transformation
    if key == ord("r"):
        dst_transform = clone_low.copy()
        img_high = clone_high.copy()
        ref_pt_src = []
        ref_pt_dst = []
        computationDone = False
    
    elif key == ord("s"):
        ref_pt_dst = []
        ref_pt_src = []
        cv2.imwrite('images\\newTransformation.jpg', result_img)
        dst_transform = clone_low.copy()
        img_high = clone_high.copy()
        computationDone = False
    # if the 'q' key is pressed, break from the loop
        
    elif key == ord("q"):
        break

cv2.destroyAllWindows()
