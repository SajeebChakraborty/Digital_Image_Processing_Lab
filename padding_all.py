import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
	img = plt.imread('image2.jpg')
	
	grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	grayscale = cv2.resize(grayscale, (500, 500))
	
	plt.figure(figsize=(15,15))

	'''Built-in Neighborhood'''
	kernel = np.ones((3,3), dtype=np.uint8) * 1/9
	neighborhood = cv2.filter2D(src=grayscale, ddepth=-1, kernel=kernel)
	
	plt.subplot(1,2,1)
	plt.title('Built in Neighborhood')
	plt.imshow(neighborhood, cmap='gray')
	
	'''Custom Neighborhood'''
	row, col = grayscale.shape
	k_r, k_c = kernel.shape
	
	new_row = row + k_r - 1
	new_col = col + k_c - 1
	
	zero_padding = np.zeros((new_row, new_col), dtype=np.uint8)
	
	r, c = int(k_r/2), int(k_c/2)
	
	zero_padding[r:r+row, c:c+col] = grayscale
	conv_img = np.zeros((row, col), dtype=np.uint8)
	
	for i in range(row):
		for j in range(col):
			mat = zero_padding[i:i+k_r, j:j+k_c]
			val = np.sum(np.multiply(mat, kernel))
			
			if val < 0:
				conv_img[i,j] = 0
			elif val > 255:
				conv_img[i,j] = 255
			else:
				conv_img[i,j] = val
			
	
	plt.subplot(1,2,2)
	plt.title('Custom Neighborhood')
	plt.imshow(conv_img, cmap='gray')
	
	plt.show()

if __name__ == '__main__':
	main()