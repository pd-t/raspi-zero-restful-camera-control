import numpy as np
import cv2
from example.fastiecm import fastiecm


def stretch_to_greyscale(im):
    out = im + 1.
    out = out / 2.
    out = out * 255.
    return out


def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (r.astype(float) - b.astype(float)) / bottom
    return ndvi


noir_with_filter = cv2.imread('raspi_noir_image_with_blue_filter.jpg')

ndvi = calc_ndvi(noir_with_filter)
ndvi_greyscale = stretch_to_greyscale(ndvi)

color_mapped_ndvi = cv2.applyColorMap(
    ndvi_greyscale.astype(np.uint8),
    fastiecm
)
cv2.imwrite('color_mapped_ndvi.png', color_mapped_ndvi)
