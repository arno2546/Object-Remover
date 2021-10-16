import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


image1 = cv2.imread("example01.jpg")
# had to resize so that it could be later subsatracted!
image1 = cv2.resize(image1, (300, 300))
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2 = cv2.imread("example010.jpg")
image2 = cv2.resize(image2, (300, 300))
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

diff = cv2.subtract(image2, image1)
result = not np.any(diff)  # if image is not the same then result will be false

if result is True:
    print("images are the same")
else:
    # images are different. This saves a new resultant image
    cv2.imshow("result.jpg", diff)
    cv2.waitKey(0)
