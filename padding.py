import matplotlib.pyplot as plt
import cv2
import numpy as np

def padding(img,h):
    
    k=int(h/2)
    height,width=img.shape
    new_height=height+h-1
    new_width=width+h-1
        
    padding_img=np.zeros((new_height,new_width),np.int8)
    
    for i in range(height):
        for j in range(width):
            
            padding_img[i+k,j+k]=img[i,j]
            
    return padding_img


def con_img(img,kernel):

    kernel_height,kernel_width=kernel.shape
    img=padding(img,kernel_width)
    
    img_height,img_width=img.shape
    
    filer_img=np.zeros((img_height,img_width),np.int8)
    
    for i in range(img_height):
        for j in range(img_width):
        
        
            sum=0
            img_height_index=i
            
            for m in range(kernel_height):
                img_width_index=j
                for n in range(kernel_height):
                
                    if(img_height_index > img_height-1 or img_width_index > img_width-1):
                        break
                
                    sum=sum+img[img_height_index,img_width_index]*kernel[m,n]
                
                    img_width_index=img_width_index+1
            
                img_height_index=img_height_index+1
            sum=sum
            if(sum <0):
                sum=0
                
            elif(sum>255):
                sum=255
                
            filer_img[i][j]=sum
            
    
    return filer_img
    

kernel=np.array((

    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]


),np.int8)

path="./image.jpg"
img=plt.imread(path)
	
grayscale=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
th,binary=cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY)

new_im=con_img(grayscale,kernel)


plt.imshow(new_im)
        
        
                
                    
    
    
	
	
