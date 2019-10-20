# -*- coding: utf-8 -*-
"""LaplacianFilter-spatial

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pc6xNLPWQALsMeNqXElzhG_GyojVniEn
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import convolve

import PIL
from PIL import Image
img = np.asarray(PIL.Image.open("SanFrancisco.jpg"))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray.shape

h=np.array([[0,1,0],[1,-4,1],[0,1,0]])

sp=convolve(gray,h)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(sp,cmap = 'gray')
plt.title('Laplacian_spatial'), plt.xticks([]), plt.yticks([])
plt.show()