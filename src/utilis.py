import cv2
import numpy as np

def preProcess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray, (3,3),6) 
    blur = cv2.bilateralFilter(gray,9,75,75)
    threshold_img = cv2.adaptiveThreshold(blur,255,1,1,11,2)
    return threshold_img


def isSquare(contours):
    perimeter = cv2.arcLength(contours, True)
    approx = cv2.approxPolyDP(contours, 0.02 * perimeter, True)
    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(contours)
        aspectRatio = float(w)/h
        if aspectRatio >= 0.9 and aspectRatio <= 1.1:
            return True
    return False


def maxContour(contours, img): # allows for openCV to find the sudoku grid because that will usually be the biggest contour
    max_contour = None
    max_area = 0

    for contour in contours:
       if isSquare(contour):
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour
    print(max_area)
    print(max_contour)
    if max_contour is not None:
        return cv2.drawContours(img, [max_contour], 0, (255, 0, 0), 2)
    else:
        return img


def isolatedSudoku(contours, original_Image ):
    x, y, w, h =  cv2.boundingRect(contours.astype('uint8')) # the boundingRect function returns 4 variables including the top-left coordinate (x,y), width (w) and height (h) 
    new_image = original_Image[y:y+h, x:x+w] # creates a image 
    cv2.drawContours(new_image, [contours], 0, (255, 255, 255), -1)
    cv2.imshow("Sudoku", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
