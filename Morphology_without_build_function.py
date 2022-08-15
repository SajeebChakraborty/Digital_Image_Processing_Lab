import matplotlib.pyplot as plt
import cv2
import random
import numpy as np

def main():


	path="./snake.jpg"
	img=plt.imread(path)
	
	grayscale=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	th,binnary=cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY_INV)

	def erotion(img,kernel):
		
		height,width=img.shape
		kernel_height,kernel_width=kernel.shape
		new_img=np.ones((height,width),np.int8)
		
		for i in range(1,height-1):
		
			for j in range(1,width-1):
			
				if(img[i][j]==0):
				
					new_img[i-1:i+2,j-1:j+2]=np.zeros((kernel_height,kernel_width),np.int8)
					
		return new_img
	
	
	def dilation(img,kernel):
		
		height,width=img.shape
		kernel_height,kernel_width=kernel.shape
		new_img=np.zeros((height,width),np.int8)
		
		for i in range(1,height-1):
		
			for j in range(1,width-1):
			
				if(img[i][j]==255):
				
					new_img[i-1:i+2,j-1:j+2]=kernel
					
		return new_img

    
	kernerl=np.ones((3,3),np.int8)
	new_img=erotion(binnary,kernerl)
	
	plt.subplot(4,2,1)
	plt.imshow(new_img)
	
	new_img=dilation(binnary,kernerl)
	
	plt.subplot(4,2,2)
	plt.imshow(new_img)
    
	
	
	opening=erotion(binnary,kernerl)
    
	opening=dilation(opening,kernerl)
    
    
	plt.subplot(4,2,3)
	plt.imshow(opening)
    
    
    
	closing=dilation(binnary,kernerl)
    
	closing=erotion(closing,kernerl)
    
    
	plt.subplot(4,2,4)
	plt.imshow(closing)
	
	plt.show()



if __name__ == "__main__":
	main()