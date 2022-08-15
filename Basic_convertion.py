import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    
    path="./image2.jpg"
    image=plt.imread(path)
    
    
    red_chanel=image[:,:,0]
    
    green_chanel=image[:,:,1]
    
    blue_chanel=image[:,:,2]
    
    height,width=image.shape[:2]
    grayscale=np.zeros((height,width),np.int8)
      
  
    grayscale=red_chanel*.2989+green_chanel*.5870+blue_chanel*.1140
    
    
    #binary convertion
    
    #height,width=grayscale.shape
    
    print(height)
   
    #grayscale=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    print(grayscale)
    
    binary=np.zeros((height,width),np.int8)
    
    for i in range(height):
        for j in range(width):
            
            if(grayscale[i][j]<=55):
                binary[i][j]=0
                
            else:
                binary[i][j]=255
                
    

                
    '''
    grayscale=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    th,binary=cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY_INV)
    th,binary=cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY)
  
    
    '''
   
    
    '''
    
    plt.subplot(4,2,1)
    plt.title("image")
    plt.imshow(image)
    
    plt.subplot(4,2,2)
    plt.title("grayscale")
    plt.imshow(grayscale,cmap="gray")
    
    plt.subplot(4,2,3)
    plt.title("binary")
    plt.imshow(binary,cmap="binary")
    
    plt.subplot(4,2,4)
    plt.title("red")
    plt.imshow(red_chanel,cmap="Reds")
    
    plt.subplot(4,2,5)
    plt.title("green")
    plt.imshow(green_chanel,cmap="Greens")
    
    plt.subplot(4,2,6)
    plt.title("red")
    plt.imshow(blue_chanel,cmap="Blues")
    
    
    
    
    plt.subplot(4,2,7)
    plt.title("histogram")
    plt.hist(binary.ravel(),255,[0,255])
    
    
    '''
    
    title_set=["image","grayscale","binary","red_chanel","green_chanel","blue_chanel"]
    img_set=[image,grayscale,binary,red_chanel,green_chanel,blue_chanel]
    
    def plot(title_set,img_set):
    
        n=len(img_set)
        
        for i in range(n):
            img=img_set[i]
            plt.subplot(4,2,i+1)
            ch=len(img.shape)
            
            if(ch==2):
                plt.imshow(img,cmap="gray")
            else:
                plt.imshow(img)
             
         
    
        plt.show()
        
    plot(title_set,img_set)
    
    
if __name__ == "__main__":
    main()
    
    