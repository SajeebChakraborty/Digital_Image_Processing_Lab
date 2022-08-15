import matplotlib.pyplot as plt
import cv2
import numpy as np
import math

def plot_hisogram(img):

    pixel=[]
    intencity=[]
    
    for k in range(256):
        tem_cnt=0
        pixel.append(k)
        for i in range(height):
            for j in range(width):
                if(img[i][j]==k):
                    tem_cnt=tem_cnt+1
        intencity.append(tem_cnt)
    return pixel,intencity

path="./image2.jpg"
img=cv2.imread(path,0)
height,width=img.shape

pixel,intencity=plot_hisogram(img)

pdf=[]

for i in range(256):
    
    pdf.append(intencity[i]/(height*width))
 
cdf=[]

for i in range(256):

    if(i==0):
        cdf.append(pdf[i])
        
    else:
        cdf.append(pdf[i-1]+pdf[i])

equ_hist=[]

for i in range(256):
    
    equ_hist.append(math.ceil(cdf[i]*255))
    
new_img=np.zeros((height,width),np.int8)

for i in range(height):
    for j in range(width):
    
        new_img[i][j]=equ_hist[img[i][j]]
        

plt.subplot(4,2,1)
plt.imshow(new_img)

plt.show()

