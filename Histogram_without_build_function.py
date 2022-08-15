import matplotlib.pyplot as plt
import cv2
import numpy

def plot_hisogram(img):

    pixel=[]
    intencity=[]
    
    for k in range(255):
        tem_cnt=0
        pixel.append(k)
        for i in range(height):
            for j in range(width):
                if(img[i][j]==k):
                    tem_cnt=tem_cnt+1
        intencity.append(tem_cnt)
    return pixel,intencity

path="./image3.jpg"
img=cv2.imread(path,0)
height,width=img.shape

pixel,intencity=plot_hisogram(img)

plt.stem(pixel,intencity)        

plt.show()