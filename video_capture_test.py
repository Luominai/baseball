from utils import setup_video_capture
import cv2 as cv

video = "videos/Frisco Memorial scrimmage pitching side view - Andy Zappe (1080p, h264).mp4"
# video = "videos/Physical Literacy Video Model Throwing (Side View) - Canucks Autism Network Video Models (1080p, h264).mp4"
# video = "videos/Noah Yoder Face On Side View Vs Hanover HS - Adams Performance Fitness and Physical Therapy (1080p, h264).mp4"
# video = "videos/Pitching, Side view, June 2025 - Cienna Alvarez (480p, h264).mp4"

# Press Q to exit
# Press S to pause
# Press D to skip to the next frame

bg_sub = cv.createBackgroundSubtractorKNN()
bg_sub.setDist2Threshold(3600)
bg_sub.setHistory(10)

def process(img):
    img = cv.resize(img, None, fx=0.36, fy=0.36)

    img1 = bg_sub.apply(img)
    cv.imshow("bg_sub", img1)

    img2 = cv.Canny(img, 250, 400)
    cv.imshow("canny", img2)

    img3 = cv.blur(img2, (7,7))
    ret, img3 = cv.threshold(img3, 0, 200, cv.THRESH_BINARY)
    cv.imshow("blurred canny", img3)

    img4 = cv.subtract(img1, img3)
    # ret, img4 = cv.threshold(img4, 100, 255, cv.THRESH_BINARY)
    cv.imshow("diff", img4)

setup_video_capture(process, video)