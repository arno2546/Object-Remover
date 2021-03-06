import argparse
import cv2
import numpy as np
from PIL import Image
from matplotlib import cm

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path input image on which we'll perform inpainting")
ap.add_argument("-m", "--mask", type=str, required=True,
	help="path input mask which corresponds to damaged areas")
ap.add_argument("-a", "--method", type=str, default="telea",
	choices=["telea", "ns"],
	help="inpainting algorithm to use")
ap.add_argument("-r", "--radius", type=int, default=3,
	help="inpainting radius")
args = vars(ap.parse_args())
# initialize the inpainting algorithm to be the Telea et al. method
flags = cv2.INPAINT_TELEA
# check to see if we should be using the Navier-Stokes (i.e., Bertalmio
# et al.) method for inpainting
if args["method"] == "ns":
	flags = cv2.INPAINT_NS
image = cv2.imread(args["image"])
mask = cv2.imread(args["mask"])
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image,(500,700))
mask = cv2.resize(mask,(500,700))
print(type(mask))
mask = Image.fromarray(np.uint8(cm.gist_earth(mask)*255))
R, G, B = mask.convert('RGB').split()
r = R.load()
g = G.load()
b = B.load()
w, h = mask.size

# Convert non-black pixels to white
for i in range(w):
    for j in range(h):
        if(r[i, j] != 0 or g[i, j] != 0 or b[i, j] != 0):
            r[i, j] = 255 # Just change R channel

# Merge just the R channel as all channels
mask = Image.merge('RGB', (R, R, R))
mask = mask.save("mask.jpg")
mask = cv2.imread("mask.jpg")
output = cv2.inpaint(image, mask, args["radius"], flags=flags)
# show the original input image, mask, and output image after
# applying inpainting
cv2.imshow("Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Output", output)
cv2.waitKey(0)