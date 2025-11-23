import time
import cv2
import numpy as np
import mss
from tkinter_screenshot import setup_screen
from pprint import pprint

rectangle = setup_screen(1.25)
start_x, start_y, end_x, end_y = rectangle["start_x"], rectangle["start_y"], rectangle["end_x"], rectangle["end_y"]
top = min(start_y, end_y)
left = min(start_x, end_x)
width = abs(end_x - start_x)
height = abs(end_y - start_y)

monitor = {"top": top, "left": left, "width": width, "height": height}

with mss.mss() as sct:
    while "Screen capturing":
        img = np.array(sct.grab(monitor))
        cv2.imshow("OpenCV/Numpy normal", img)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break