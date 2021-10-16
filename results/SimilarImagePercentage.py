import cv2 as cv2
import numpy as np

image2 = cv2.imread("example05 (without car).jpg")
image1 = cv2.imread("example05.jpg")

# check similarities between two images
# sift algorithm for feature matching
# https://docs.opencv.org/master/da/df5/tutorial_py_sift_intro.html
sift = cv2.SIFT_create()  # The scale-invariant feature transform (SIFT)
# is a feature detection algorithm
# in computer vision to detect and describe local features in images
kp1, des1 = sift.detectAndCompute(image1, None)
kp2, des2 = sift.detectAndCompute(image2, None)
print("Key points in first image :" + str(len(kp1)))  # key points in image 1
print("Key points in second image :" + str(len(kp2)))  # key points in imag 2

index_params = dict(algorithm=0, trees=5)
search_params = dict()
# Fast Library for Approximate Nearest Neighbors
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)
# print("match:"+ str(len(matches)))
good_points = []
for m, n in matches:
    # print(str(m) +"--"+str(n))
    if m.distance < 0.99 * n.distance:  # must change the ratio value to distort the percentage value
        good_points.append(m)

numOfKeyPoint = 0
if len(kp1) <= len(kp2):
    numOfKeyPoint = len(kp1)
else:
    numOfKeyPoint = len(kp2)

print("The matching percentage of the images : " +
      str((len(good_points) / numOfKeyPoint) * 100))

print("Good matches: " + str(len(good_points)))  # good matches in key points
# all the match points will be visible by this
result = cv2.drawMatches(image1, kp1, image2, kp2, good_points, None)
# cv2.imshow("output", result)
# cv2.waitKey(0)
