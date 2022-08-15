import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():

    path="./image.jpg"
    img=plt.imread(path)
    graysacle=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    height,width=img.shape[:2]
    
    mask_set_up=np.zeros((height,width),np.int8)
    
    for i in range(80,300):
        for j in range(80,300):
            
            mask_set_up[i][j]=255
            
    new_img=cv2.bitwise_and(graysacle,graysacle,mask=mask_set_up)
    
    
    
    
    plt.title("masking")
    plt.imshow(new_img)
    
    plt.show()
    


if __name__ == "__main__":
    main()