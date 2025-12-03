from pprint import pprint
import cv2 as cv
import numpy as np
from utils import setup_mss

# bg_sub = cv.createBackgroundSubtractorKNN()
# bg_sub.setHistory(10)

bg_sub = cv.createBackgroundSubtractorMOG2(history=8)

def ready(img):
    # global edge_pixels
    # edge_pixels = np.full(img.shape, 0)
    pass

def process(img):
    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # edge_pixels = cv.Canny(gray, 50, 100)
    # lines = cv.HoughLinesP(edge_pixels, 1, np.pi/180, 200)
    # if lines is not None:   
    #     for line in lines:
    #         x1,y1,x2,y2=line[0]
    #         cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    # circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,
    #                         param1=200,param2=8,minRadius=0,maxRadius=6)
    
    # if circles is not None:
    #     circles = np.uint16(np.around(circles))
    #     for i in circles[0,:]:
    #         # draw the outer circle
    #         cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    #         # draw the center of the circle
    #         cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
            
    # img = edge_pixels
    img = bg_sub.apply(img)
    cv.imshow("OpenCV/Numpy normal", img)
    
setup_mss(process, ready)