from utilis import *
import numpy as np
import cv2


imagePath = "images/s3.jpg"
height = 450
width = 450


# step 1: prepare the image using image preprocessing
# this will modify the image to make the image easier to see
# grayscale, gaussian blur, adaptive threshold

img = cv2.imread(imagePath)
img = cv2.resize(img, (width, height))
imgThreshold = preProcess(img)


# step 2: find contours for our image to make sudoku easily recognizable
contourCopy = img.copy()
contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_contour = maxContour(contours, contourCopy) # function written in utilis that finds and displays the maxContour

#Step 3: extract the sudoku grid from image to recognize the numbers
# this step will take a screenshot of the outline basically and create a new image

#if max_contour is not None:
 isolatedSudoku(max_contour, img)

# Create a 2x3 grid for displaying images
grid = np.zeros((2*img.shape[0], 3*img.shape[1], 3), dtype=np.uint8)

# Place each image in the grid
grid[:img.shape[0], :img.shape[1]] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grid[:img.shape[0], img.shape[1]:2*img.shape[1]] = cv2.cvtColor(imgThreshold, cv2.COLOR_GRAY2RGB)
grid[:img.shape[0], 2*img.shape[1]:] = cv2.cvtColor(contourCopy, cv2.COLOR_BGR2RGB)
grid[img.shape[0]:2*img.shape[0], :img.shape[1]] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grid[img.shape[0]:2*img.shape[0], img.shape[1]:2*img.shape[1]] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grid[img.shape[0]:2*img.shape[0], 2*img.shape[1]:] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the grid
cv2.imshow("All Images", grid)
cv2.waitKey(0)
cv2.destroyAllWindows()

