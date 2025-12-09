import cv2
import numpy as np

# 1. Load and threshold the image to ensure it's binary
src1 = cv2.imread('img1.png', 0) # Read as grayscale
ret, thresh = cv2.threshold(src1, 127, 255, cv2.THRESH_BINARY) # Ensure binary

# 2. Perform connected component labeling
connectivity = 8
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S)

# 1. Load and threshold the image to ensure it's binary
src2 = cv2.imread('img2.png', 0) # Read as grayscale
ret2, thresh2 = cv2.threshold(src2, 200, 255, cv2.THRESH_BINARY) # Ensure binary

# 2. Perform connected component labeling
connectivity = 8
num_labels2, labels2, stats2, centroids2 = cv2.connectedComponentsWithStats(thresh2, connectivity, cv2.CV_32S)

max_area = 0

for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]
    x_center = int(centroids[i,0])
    y_center = int(centroids[i,1])
    if area > max_area:
        max_area = area
        max_x = x_center
        max_y = y_center

max_area = 0

for i in range(1, num_labels2):
    area = stats2[i, cv2.CC_STAT_AREA]
    x_center = int(centroids2[i,0])
    y_center = int(centroids2[i,1])
    if area > max_area:
        max_area = area
        max_x2 = x_center
        max_y2 = y_center

print(f"Center of baseball in img1: ({max_x}, {max_y})")
print(f"Center of baseball in img2: ({max_x2}, {max_y2})")

img_line = cv2.line(src1, (max_x, max_y), (max_x2, max_y2), 255, 1)
cv2.imwrite('img_line.png',img_line)