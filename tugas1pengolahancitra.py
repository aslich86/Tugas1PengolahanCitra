# -*- coding: utf-8 -*-
"""Tugas1PengolahanCitra.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qiXg1GC0Gm2WDeL0dI_bX9l53fWwB17e
"""

# pip install numpy
import numpy as np
import imageio as img
import matplotlib.pyplot as plt

image = img.imread("/images.jpeg")

# Extract each color channel
red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

# Create blank images for each channel
imgRed = np.zeros_like(image)
imgGreen = np.zeros_like(image)
imgBlue = np.zeros_like(image)

# Assign each channel to the respective blank image
imgRed[:, :, 0] = red
imgGreen[:, :, 1] = green
imgBlue[:, :, 2] = blue

# Plot the images
plt.figure(figsize=(10, 10))

# Original image
plt.subplot(4, 1, 1)
plt.title("Original Image")
plt.imshow(image)

# Red channel image
plt.subplot(4, 1, 2)
plt.title("Red Channel")
plt.imshow(imgRed)

# Green channel image
plt.subplot(4, 1, 3)
plt.title("Green Channel")
plt.imshow(imgGreen)

# Blue channel image
plt.subplot(4, 1, 4)
plt.title("Blue Channel")
plt.imshow(imgBlue)

plt.show()