import matplotlib.pyplot as plt
import cv2
import numpy as np



path="./image.jpg"
img=cv2.imread(path,0)
	
height,width=img.shape
	
bit1=np.zeros((height,width),np.int8)
bit2=np.zeros((height,width),np.int8)
bit3=np.zeros((height,width),np.int8)
bit4=np.zeros((height,width),np.int8)
bit5=np.zeros((height,width),np.int8)
bit6=np.zeros((height,width),np.int8)
bit7=np.zeros((height,width),np.int8)
bit8=np.zeros((height,width),np.int8)
    
bit_slice_img=[bit1,bit2,bit3,bit4,bit5,bit6,bit7,bit8]
bit_operaton=[1,2,4,8,16,32,64,128]
    
for i in range(7):
    
    for j in range(height):
        for k in range(width):
            
            if(img[j][k] & bit_operaton[i]):
                bit_slice_img[i][j][k]=255
    
title_set=["bit1","bit2","bit3","bit4","bit5","bit6","bit7","bit8"]
img_set=[bit1,bit2,bit3,bit4,bit5,bit6,bit7,bit8]
    
    
def plot(title_set,img_set):
        
        n=len(title_set)
        
        for i in range(n):
        
            plt.subplot(4,2,i+1)
            
            img=img_set[i]
            
            plt.imshow(img,cmap="gray")
            plt.title(title_set[i])
            
        plt.show()
        
    
plot(title_set,img_set)

