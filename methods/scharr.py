import cv2 
import numpy as np
import math
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor

IMAGE_NAME = '../images/brush.png' # Paste image name here

img = cv2.imread(IMAGE_NAME, 0)

width = len(img[0])
height = len(img)

img2 = img.copy()

gx = [
    [-3, 0, 3],
    [-10, 0, 10],
    [-3, 0, 3]
]

gy = [
    [3, 10, 3],
    [0, 0, 0],
    [-3, -10, -3]
]

for i in range(1, width - 1):
    for j in range(1, height - 1):
        gradientX = (
            gx[0][0] * img[j - 1][i - 1] + 
            gx[0][2] * img[j - 1][i + 1] + 
            gx[1][0] * img[j][i - 1] + 
            gx[1][2] * img[j][i + 1] + 
            gx[2][0] * img[j + 1][i - 1] + 
            gx[2][2] * img[j + 1][i + 1]
        )
        
        gradientY = ( 
            gy[0][0] * img[j - 1][i - 1] + 
            gy[0][1] * img[j - 1][i] + 
            gy[0][2] * img[j - 1][i + 1] + 
            gy[2][0] * img[j + 1][i - 1] + 
            gy[2][1] * img[j + 1][i] + 
            gy[2][2] * img[j + 1][i + 1]
        )

        gradientMagn = math.sqrt(gradientX * gradientX + gradientY * gradientY)
        img2[j][i] = gradientMagn

plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('Original image')

plt.subplot(122)
plt.imshow(img2, cmap = 'gray')
plt.title('Scharr operator')

plt.show()