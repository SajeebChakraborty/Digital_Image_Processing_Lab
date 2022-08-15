import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
	
	path="./image_er.jpg"
	img=plt.imread(path)
	
	grayscale=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	th,binary=cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY_INV)
	
	plt.subplot(4,2,1)
	plt.title("image")
	plt.imshow(img,cmap="binary")
	
	kernel1=np.ones((3,3),np.int8)
	
	erode=cv2.erode(img,kernel1,iterations=1)

	plt.subplot(4,2,2)
	plt.title("erode")
	plt.imshow(erode,cmap="binary")
	
	dilate=cv2.dilate(img,kernel1,iterations=1)
	
	plt.subplot(4,2,3)
	plt.title("dilate")
	plt.imshow(dilate,cmap="binary")
	
	opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel1)
	
	plt.subplot(4,2,4)
	plt.title("open")
	plt.imshow(opening,cmap="binary")
	
	
	close=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel1)
	
	plt.subplot(4,2,5)
	plt.title("close")
	plt.imshow(close,cmap="binary")
	
	
	plt.show()
	
	

if __name__ == "__main__":
	main()