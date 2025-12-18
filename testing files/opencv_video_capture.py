# Code taken from here:
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

import time
import numpy as np
import cv2 as cv

# Threshold: 5000, varThreshold: 80
# cap = cv.VideoCapture('videos\Physical Literacy Video Model Throwing (Side View) - Canucks Autism Network Video Models (1080p, h264).mp4')
# Threshold: 600, History: 100
# cap = cv.VideoCapture('videos\Pitching, Side view, June 2025 - Cienna Alvarez (480p, h264).mp4')
video = 'videos/pitch_01.mp4'
cap = cv.VideoCapture(video)

background_subtraction = cv.createBackgroundSubtractorMOG2(varThreshold=160)
# background_subtraction = cv.createBackgroundSubtractorKNN()
# background_subtraction.setDist2Threshold(400)
# background_subtraction.setHistory(10)

# print(background_subtraction.getkNNSamples())     2
# print(background_subtraction.getHistory())        500
# print(background_subtraction.getDist2Threshold()) 400

previous_time = None

while cap.isOpened():
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    fg_mask = background_subtraction.apply(frame)
    cv.imshow('frame', fg_mask)

    # current_time = time.time()
    # if previous_time:
    #     print(current_time - previous_time)
    # previous_time = current_time

    if cv.waitKey(10) == ord('q'):
        break
 
cap.release()
cv.destroyAllWindows()