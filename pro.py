import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read original image
image = cv2.imread("c1.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.png', gray)

# Apply median filter for smoothing
blurM = cv2.medianBlur(gray, 5)
cv2.imwrite('blurM.png', blurM)

# Apply Gaussian filter for smoothing
blurG = cv2.GaussianBlur(gray, (9, 9), 0)
cv2.imwrite('blurG.png', blurG)

# Histogram equalization
histoNorm = cv2.equalizeHist(gray)
cv2.imwrite('histoNorm.png', histoNorm)

# Create a CLAHE object for Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
claheNorm = clahe.apply(gray)
cv2.imwrite('claheNorm.png', claheNorm)


# Contrast stretching
def pixelVal(pix, r1, s1, r2, s2):
    if 0 <= pix <= r1:
        return (s1 / r1) * pix
    elif r1 < pix <= r2:
        return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2) / (255 - r2)) * (pix - r2) + s2

# Define parameters
r1, s1, r2, s2 = 70, 0, 200, 255

# Vectorize the function to apply it to each value in the NumPy array
pixelVal_vec = np.vectorize(pixelVal)

# Apply contrast stretching
contrast_stretched = pixelVal_vec(gray, r1, s1, r2, s2)
contrast_stretched_blurM = pixelVal_vec(blurM, r1, s1, r2, s2)

cv2.imwrite('contrast_stretch.png', contrast_stretched)
cv2.imwrite('contrast_stretch_blurM.png', contrast_stretched_blurM)

# Edge detection using Canny edge detector
edge = cv2.Canny(gray, 100, 200)
cv2.imwrite('edge.png', edge)

edgeG = cv2.Canny(blurG, 100, 200)
cv2.imwrite('edgeG.png', edgeG)

edgeM = cv2.Canny(blurM, 100, 200)
cv2.imwrite('edgeM.png', edgeM)
