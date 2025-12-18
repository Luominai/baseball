import cv2 as cv
from matplotlib import pyplot as plt
from pathlib import Path

import utils as utils

bg_sub = cv.createBackgroundSubtractorKNN()
bg_sub.setDist2Threshold(3600)
bg_sub.setHistory(10)

blur_m = 7
def process(img):
    img = cv.resize(img, None, fx=0.34, fy=0.34)
    
    # show orginal image.
    cv.imshow("Oringal", img)

    # apply background subtraction to original image
    img1 = bg_sub.apply(img)
    cv.imshow("Background Subtraction", img1)

    # apply canny edge detection to original image
    img2 = cv.Canny(img, 250, 400)
    cv.imshow("Canny Edge Detection", img2)

    # inflate the edges
    img3 = cv.blur(img2, (blur_m,blur_m))
    ret, img3 = cv.threshold(img3, 0, 200, cv.THRESH_BINARY)
    # cv.imshow("blurred canny", img3)

    # subtract the inflated edges from the original images to reduce background noise
    img4 = cv.subtract(img1, img3)
    # ret, img4 = cv.threshold(img4, 100, 255, cv.THRESH_BINARY)
    cv.imshow("Difference", img4)

# from opencv docs: https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
# position [0,1,2] to respresent grabbing from the front, middle, or end of the ball img
def find_ball(ball, frame, position):
    w, h = ball.shape[::-1]
    res = cv.matchTemplate(frame, ball, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc

    if position == 0: # start
        return (int(top_left[0]), int(top_left[1]+ h))
    elif position == 2: # end
        return (int(top_left[0] + w), int(top_left[1] + (h/2)))
    else: # middle 
        return (int(top_left[0]+(w/2)), int(top_left[1]+(h/2)))

def video_process(path, sample): 
    if not sample: 
        utils.setup_video_capture(process, path)

    video_name = path.split('/')[-1][:-4] # save video name

    # display frames and allow user to select screenshot of ball
    frames = []
    frame_count = 0
    frame_path = "frames/"+video_name+"_"+str(frame_count)+".jpg"
    print(frame_path)
    while Path(frame_path).is_file():
        next_frame = cv.imread(frame_path,cv.IMREAD_GRAYSCALE)

        # check if frame is mostly white to avoid errors as background sub trains or adjust to sudden lighting changes
        white_pixels = cv.countNonZero(next_frame)
        total_pixels = next_frame.size
        white_percentage = (white_pixels / total_pixels)
        if white_percentage < .8:
            frames.append(next_frame)

        frame_count += 1
        frame_path = "frames/"+video_name+"_"+str(frame_count)+".jpg"

    if len(frames) <= 1:
        print('Frame count: '+str(len(frames))+'\nNot enough frames. Reopen program to try again')
        return 

    if not sample: 
        # grab sample of ball from choosen frame using tkinter
        frame_index = input('Select frame from 0 to '+str(len(frames)-1)+': ')
        while frame_index.isalpha() or int(frame_index) > frame_count-1 or int(frame_index) < 0:
            frame_index = input('Please select valid frame number.')

        print('Screenshot ball.')
        cv.imshow('select ball', frames[int(frame_index)])
        ball_path = input('Then enter file path: ')
        while not Path(ball_path).is_file():
            ball_path = input('File not found.\n Please enter valid file path: ')
    else: 
        ball_img = 'balls/memorial_ball.jpg'

    ball_img = cv.imread(ball_path,cv.IMREAD_GRAYSCALE)

    if ball_img is None:
        print("Couldn't open sample ball image.")
        return

    ball_coors = []
    ball_coors.append(find_ball(ball_img,frames[0],0))
    for f in frames:
        ball_coors.append(find_ball(ball_img,f,1))
    ball_coors.append(find_ball(ball_img,frames[-1],2))

    # # draw a line of the ball's travel
    print('Ball coordinates: '+str(ball_coors))
    first_frame = frames[0]
    # check if too far of a distance
    x_threshold = first_frame.shape[1]/3 # one third of the width
    y_threshold = first_frame.shape[0]/3 # one third of the height
    for i in range(1,len(ball_coors)-1):

        x_diff = abs(ball_coors[i][0] - ball_coors[i+1][0])
        y_diff = abs(ball_coors[i][1] - ball_coors[i+1][1])
        # break in over threshold and if line backtracking
        if x_diff > x_threshold or y_diff > y_threshold or ball_coors[i+1][0] < ball_coors[i][0]:
            break

        cv.line(first_frame, ball_coors[i],ball_coors[i+1],80,10)


    cv.imwrite("lines/"+video_name+"_line.jpg", first_frame)

    # # display line
    cv.imshow("tracked line", first_frame)

    return ball_coors

    # delete all created files?
    return



