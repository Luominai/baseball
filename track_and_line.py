import cv2 as cv
from matplotlib import pyplot as plt

# import tkinter_canvas
# import tkinter_screen
# import tkinter_screenshot
# import opencv_video_capture 
import utils as utils

# def process(img):
#     cv.imshow('OpenCV/Numpy normal', img)

bg_sub = cv.createBackgroundSubtractorKNN()
bg_sub.setDist2Threshold(3600)
bg_sub.setHistory(10)

blur_m = 7
def process(img):
    img = cv.resize(img, None, fx=0.34, fy=0.34)

    # apply background subtraction to original image
    img1 = bg_sub.apply(img)
    cv.imshow("bg_sub", img1)

    # apply canny edge detection to original image
    img2 = cv.Canny(img, 250, 400)
    cv.imshow("canny", img2)

    # inflate the edges
    img3 = cv.blur(img2, (blur_m,blur_m))
    ret, img3 = cv.threshold(img3, 0, 200, cv.THRESH_BINARY)
    cv.imshow("blurred canny", img3)

    # subtract the inflated edges from the original images to reduce background noise
    img4 = cv.subtract(img1, img3)
    # ret, img4 = cv.threshold(img4, 100, 255, cv.THRESH_BINARY)
    cv.imshow("diff", img4)

# from opencv docs: https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
def find_ball(ball, frame, number):
    w, h = ball.shape[::-1]
    res = cv.matchTemplate(frame, ball, cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv.rectangle(frame,top_left, bottom_right, 255, 2)

    plt.subplot(122),plt.imshow(frame,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.savefig("box_0"+str(number)+".png")

    # return ()


number = 1
video = 'videos/pitch_0'+str(number)+'.mp4'
frames = ['frames/pitch_0'+str(number)+'_0_canny.jpg','frames/pitch_0'+str(number)+'_1_canny.jpg','frames/pitch_0'+str(number)+'_2_canny.jpg','frames/pitch_0'+str(number)+'_3_canny.jpg']
sample_ball = 'balls/ball_0'+str(number)+".jpg"

def main(): 
    utils.setup_video_capture(process, 'videos/memorial_pitch.mp4')

    # grab sample of ball from choosen frame using tkinter

    # find area, ratio of length to hieght, orientation
    # ball_img = cv.imread(sample_ball,cv.IMREAD_GRAYSCALE)

    # if ball_img is None:
    #     print("Couldn't open sample ball img")
    #     return

    # ball_coors = []
    # for i in range(5,8):
    #     current_frame = cv.imread('frames/whole_run_'+str(i)+'_canny.jpg',cv.IMREAD_GRAYSCALE)
    #     if current_frame is None: 
    #         print("Missing freame " + str(i))
    #         return
        # ball_coors.append(find_ball(ball_img,current_frame,i))

    # draw a line of the ball's travel
        # cv2.line(image, start_point, end_point, color, thickness, lineType)

    return

main()



