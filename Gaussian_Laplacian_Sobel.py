import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():


    path="./image.jpg"
    image=plt.imread(path)
    
    graysacle=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    
    gasuuisan=cv2.GaussianBlur(graysacle,(3,3),cv2.BORDER_DEFAULT)
    
    laplacian=cv2.Laplacian(gasuuisan,cv2.CV_64F,(3,3))
    
    
    sobelx=cv2.Sobel(gasuuisan,cv2.CV_64F,1,0,ksize=7)
    sobely=cv2.Sobel(gasuuisan,cv2.CV_64F,0,1,ksize=7)
    
    plt.subplot(4,2,1)
    plt.title("gasuuisan")
    plt.imshow(gasuuisan)
    
    plt.subplot(4,2,2)
    plt.title("laplacian")
    plt.imshow(laplacian)
    
    plt.subplot(4,2,3)
    plt.title("sobel x")
    plt.imshow(sobelx)
    
    
    plt.subplot(4,2,4)
    plt.title("sobel y")
    plt.imshow(sobely)
    
    gasuuisan=np.array((
    
        [1,2,1],
        [2,4,2],
        [1,2,1]
    
    
    ),np.int8)
    
    process=cv2.filter2D(graysacle,-1,kernel=gasuuisan)
    
    plt.subplot(4,2,5)
    plt.title("gasuuisan")
    plt.imshow(process,cmap="gray")
    
    laplacian=np.array((
    
        [0,1,0],
        [1,-4,1],
        [0,1,0]
    
    
    ),np.int8)
    
    process=cv2.filter2D(graysacle,-1,kernel=laplacian)
    
    plt.subplot(4,2,6)
    plt.title("laplacian")
    plt.imshow(process,cmap="gray")
    
    sobelx=np.array((
    
        [1,0,-1],
        [2,0,-2],
        [1,0,-1]
    
    
    ),np.int8)
    
    process=cv2.filter2D(graysacle,-1,kernel=sobelx)
    
    plt.subplot(4,2,7)
    plt.title("sobel")
    plt.imshow(process,cmap="gray")
    
    
    
    
    plt.show()
    



if __name__ == "__main__":
    main()