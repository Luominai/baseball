import cv2 as cv
import numpy as np
from tkinter_screenshot import setup_screen
import mss

def setup_mss(process, ready, scale = 1.25):
    rectangle = setup_screen(scale)
    start_x, start_y, end_x, end_y = rectangle["start_x"], rectangle["start_y"], rectangle["end_x"], rectangle["end_y"]
    top = min(start_y, end_y)
    left = min(start_x, end_x)
    width = abs(end_x - start_x)
    height = abs(end_y - start_y)

    monitor = {"top": top, "left": left, "width": width, "height": height}

    first_img = True

    with mss.mss() as sct:
        while "Screen capturing":
            img = np.array(sct.grab(monitor))
            if first_img:
                ready(img)
                first_img = False
            process(img)

            if cv.waitKey(25) & 0xFF == ord("q"):
                cv.destroyAllWindows()
                break