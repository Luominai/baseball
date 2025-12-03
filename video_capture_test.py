from utils import setup_video_capture
import cv2 as cv

video = "videos/FRONT ROW AT THE REDS_CARDINALS GAME! - Ethan's Sports Cards & More (720p, h264).mp4"

def process(img):
    cv.imshow("OpenCV/Numpy normal", img)

setup_video_capture(process, video)