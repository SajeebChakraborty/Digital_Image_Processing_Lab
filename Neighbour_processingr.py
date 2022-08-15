import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    
    path="./image.jpg"
    img=plt.imread(path)
    
    kernel1=np.array((
        
        [1,-2,1],
        [4,-7,8],
        [3,6,5]
    
    
    ))
    
    proces=cv2.filter2D(img,-1,kernel1)
    plt.subplot(4,2,1)
    plt.title("proces")
    plt.imshow(proces)
    
    kernel2=np.zeros((3,3),np.int8)
    
    proces=cv2.filter2D(img,-1,kernel2)
    plt.subplot(4,2,2)
    plt.title("proces")
    plt.imshow(proces)
    
    
    kernel3=np.ones((3,3),np.int8)
    
    proces=cv2.filter2D(img,-1,kernel3)
    plt.subplot(4,2,3)
    plt.title("proces")
    plt.imshow(proces)
    
    plt.show()


if __name__ == "__main__":
    main()