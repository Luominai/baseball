import cv2 as cv
import numpy as np
from tkinter_screenshot import setup_screen
import mss

def setup_mss(process, ready=None, scale = 1.25):
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
            if first_img and ready is not None:
                ready(img)
                first_img = False
            process(img)

            if cv.waitKey(25) & 0xFF == ord("q"):
                cv.destroyAllWindows()
                break

def setup_video_capture(process, path_to_video=""):
    is_paused = True
    skip_frame = True
    frame_count = 0

    bg_sub = cv.createBackgroundSubtractorKNN()
    bg_sub.setDist2Threshold(3600)
    # bg_sub.setHistory(10)
    bg_sub.setHistory(1)

    cap = cv.VideoCapture(path_to_video)
    while cap.isOpened():
        key = cv.waitKey(1)

        if key == ord('q'):
            break
        elif key == ord('s'):
            is_paused = not is_paused
        elif key == ord('d'):
            skip_frame = True
        elif key == ord('f'): # save frame
            output_filename = "frames/"+path_to_video[7:-4]+"_"+str(frame_count)+".jpg"

            img1 = bg_sub.apply(frame)

            # apply canny edge detection to original image
            img2 = cv.Canny(frame, 250, 400)

            # inflate the edges
            img3 = cv.blur(img2, (7,7))
            ret, img3 = cv.threshold(img3, 0, 200, cv.THRESH_BINARY)

            # subtract the inflated edges from the original images to reduce background noise
            img4 = cv.subtract(img1, img3)

            # save
            cv.imwrite(output_filename, img4)
            frame_count += 1

        if is_paused and not skip_frame:
            continue
        
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        bg_sub.apply(frame)
        process(frame)

        skip_frame = False
        
