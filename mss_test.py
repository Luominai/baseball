import time

import cv2
import numpy as np

import mss
from tkinter_screenshot import setup_screen

(start_x, start_y, end_x, end_y) = setup_screen()
top = min(start_y, end_y)
left = min(start_x, end_x)
width = abs(end_x - start_x)
height = abs(end_y - start_y)

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": top, "left": left, "width": width, "height": height}
    # monitor = {"top": 40, "left": 0, "width": 800, "height": 640}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))

        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", img)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break