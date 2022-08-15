import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():

	path="./image.jpg"
	img=cv2.imread(path,0)
	
	equ_img=cv2.equalizeHist(img)
	
	plt.subplot(4,2,1)
	plt.imshow(equ_img)
    
    
    
	plt.savefig("Output.jpg")
   
   	
	plt.show()


if __name__ == "__main__":
	main()