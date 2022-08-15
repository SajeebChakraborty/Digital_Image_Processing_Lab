import cv2
import matplotlib.pyplot as plt
import numpy as np

import Morphology.Dialation as MD
import Morphology.Erosion as ME

'''reading image'''
rgbImg = plt.imread('snake.jpg')
plt.figure(figsize=(14,6))
plt.subplot(3, 2, 1)
plt.title('Gray Image')
plt.imshow(rgbImg)

grayImg = cv2.cvtColor(rgbImg, cv2.COLOR_BGR2GRAY)


binaryImg = cv2.threshold(grayImg, 127, 255, type=cv2.THRESH_BINARY_INV)[1]

plt.subplot(3, 2, 2)
plt.title('Binary Image')
plt.imshow(binaryImg, cmap='gray')


'''Dialation'''
structureElement = np.ones((3, 3), dtype=np.uint8)
dilation = cv2.dilate(binaryImg, structureElement, iterations=1)

plt.subplot(3, 2, 3)
plt.title('Dialation')
plt.imshow(dilation, cmap='gray')

'''dialation custom'''
customDialate = MD.dialation(binaryImg, structureElement, 1)
plt.subplot(3,2,4)
plt.title('Custom Dialation')
plt.imshow(customDialate, cmap='gray')





'''Erosion'''

erosionImg = cv2.erode(binaryImg, structureElement, iterations=1)
plt.subplot(3,2,5)
plt.title('Erosion')
plt.imshow(erosionImg, cmap='gray')

'''Custom erosion'''

erosionImg2 = ME.erosion(binaryImg, structureElement, iterations=1)
plt.subplot(3,2,6)
plt.title('Custom Erosion')
plt.imshow(erosionImg, cmap='gray')


plt.tight_layout()
plt.show()


'''Opening'''

openingImg = cv2.erode(binaryImg, structureElement, iterations=1)
openingImg = cv2.dilate(openingImg, structureElement, iterations=1)

plt.subplot(2,2,1)
plt.title('Opening')
plt.imshow(openingImg, cmap='gray')


openingImg = ME.erosion(binaryImg, structureElement, iterations=1)
openingImg = MD.dialation(openingImg, structureElement, iterations=1)

plt.subplot(2,2,2)
plt.title('Opening Custom')
plt.imshow(openingImg, cmap='gray')


'''Closing'''

closingImg = cv2.dilate(binaryImg, structureElement, iterations=1)
closingImg = cv2.erode(closingImg, structureElement, iterations=1)

plt.subplot(2,2,3)
plt.title('Closing')
plt.imshow(closingImg, cmap='gray')


closingImg = MD.dialation(binaryImg, structureElement, iterations=1)
closingImg = ME.erosion(closingImg, structureElement, iterations=1)

plt.subplot(2,2,4)
plt.title('Closing Custom')
plt.imshow(closingImg, cmap='gray')

plt.tight_layout()
plt.show()


