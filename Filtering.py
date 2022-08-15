import matplotlib.pyplot as plt
import numpy as np
path='bird.jpg'
print(path)
Image=plt.imread(path)
plt.subplot(2,2,1)
plt.title('Source Image')
plt.imshow(Image)
GrayImage=Image[:,:,0]*.298+Image[:,:,1]*.598+Image[:,:,2]*.114
plt.subplot(2,2,2)
plt.title('GrayImage')
plt.imshow(GrayImage,cmap='gray')
karnel=np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
])
h,w=karnel.shape
print(h,w)
def padding(GrayImage,h):
    k=int(h/2)
    height,width=GrayImage.shape
    print(height,width)
    paddedHeight=height+h-1
    paddedWidth=width+h-1
    paddedArray=np.zeros((paddedHeight,paddedWidth))
    for i in range (height):
        for j in range (width):
            paddedArray[i+k,j+k]=GrayImage[i,j]
    print(paddedArray)
    return paddedArray
def Filtering(paddedArray,karnel):
    pheight,pwidth=paddedArray.shape
    FilterArray=np.zeros((pheight,pwidth))
    l,k=karnel.shape
    for i in range(pheight):
        for j in range (pwidth):
            sum=0
            t=i
            for p in range(l):
                s=j
                for q in range(l):
                    if(t>pheight-1 or s>pwidth-1):
                        break
                    sum=sum+paddedArray[t,s]*karnel[p,q]
                    
                    s=s+1
        
                t=t+1
            sum = sum
            if sum>255:
                sum=255
            elif sum<0:
                sum=0
            # print(sum)
            FilterArray[i][j]=sum
    print(FilterArray)
    return FilterArray


paddedArray=padding(GrayImage,w)
Filter=Filtering(paddedArray,karnel)
plt.subplot(2,2,3)
plt.imshow(Filter,cmap='gray')
plt.show()
