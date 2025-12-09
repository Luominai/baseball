from utils import setup_video_capture
import cv2 as cv

# threshold = 1600, blur = 9
video = "videos/Frisco Memorial scrimmage pitching side view - Andy Zappe (1080p, h264).mp4"
# threshold = 1600, blur = 9
# video = "videos/Physical Literacy Video Model Throwing (Side View) - Canucks Autism Network Video Models (1080p, h264).mp4"
# threshold = 1600, blur = 9
# video = "videos/Noah Yoder Face On Side View Vs Hanover HS - Adams Performance Fitness and Physical Therapy (1080p, h264).mp4"
# threshold = 1200, blur = 3
# video = "videos/Pitching, Side view, June 2025 - Cienna Alvarez (480p, h264).mp4"
# video = "videos\RHP Will Hodges Hanover HS_Liberty Commit) Side View 2nd Inning - Adams Performance Fitness and Physical Therapy (1080p, h264).mp4"
# video = "videos\FRONT ROW AT THE REDS_CARDINALS GAME! - Ethan's Sports Cards & More (720p, h264).mp4"

scale = .7
threshold = 1600
blur = 9

# Press Q to exit
# Press S to pause
# Press D to skip to the next frame

bg_sub = cv.createBackgroundSubtractorKNN()
bg_sub.setDist2Threshold(threshold)
bg_sub.setHistory(10)

def process(img):

    # blur the original image, then apply background subtraction 
    img = cv.blur(img, (blur, blur))
    img = bg_sub.apply(img)

    img = cv.resize(img, None, fx=scale, fy=scale)
    cv.imshow("bg_sub plus blur", img)

    # # apply canny edge detection to original image
    # img2 = cv.Canny(img, 200, 400)
    # cv.imshow("canny", img2)

    # # inflate the edges
    # img3 = cv.blur(img2, (7,7))
    # ret, img3 = cv.threshold(img3, 30, 200, cv.THRESH_BINARY)
    # cv.imshow("blurred canny", img3)

    # # subtract the inflated edges from the original images to reduce background noise
    # img4 = cv.subtract(img1, img3)
    # # ret, img4 = cv.threshold(img4, 100, 255, cv.THRESH_BINARY)
    # cv.imshow("diff", img4)

setup_video_capture(process, video)