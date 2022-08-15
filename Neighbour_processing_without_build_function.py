
 
import matplotlib.pyplot as plt
import cv2
import numpy as np
import cv2


#image load
img_path = "./image.jpg"
rgb_img = cv2.imread(img_path)
# print(rgb_img.shape)


grayscale = cv2.cvtColor(rgb_img,cv2.COLOR_RGB2GRAY)
# print(grayscale.shape)

# padding the image
def padding(img):
    width, height = img.shape
#     print(img.shape)
    new_img = np.zeros(shape=(width+2, height+2))
    width, height = new_img.shape
    new_img[1:width-1, 1:height-1] = img
#     print(new_img.shape)
    return new_img


pad_img = padding(grayscale)

# convolution implement
def convolution(img,kernel):
    img = padding(img)
    
#     print(img)
    
    _,k = kernel.shape
#     print(k)
    width, height = img.shape
    print(width, height)
    new_width, new_height = width-k+1, height-k+1
    print(new_width, new_height)
    conv_img = np.zeros(shape=(new_width,new_height))
    print(conv_img)
    
    for i in range(new_width):
        for j in range(new_height):
            mat = img[i:i+k, j:j+k]
            conv_img[i,j] = np.sum(np.multiply(kernel,mat))
            
            if(conv_img[i,j] < 0):
                conv_img[i,j] = 0
            elif(conv_img[i,j] > 255):
                conv_img[i,j] = 255
    return conv_img
    

def plot_img(img_set,title_set):
    a = 2; b = 2
    n = len(img_set)
    figure = plt.figure(figsize=(20,20))
    
    for i in range(n):
        ch = len(img_set[i].shape)
        
        plt.subplot(a,b,i+1)
        if ch == 3:
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i], cmap='gray')

    plt.show()
kernel = np.array([[2, 0, -2], [1, 0, -1], [2, 0, -2]])
kernel

custom_kernel = convolution(grayscale, kernel)
built_in_kernel = cv2.filter2D(grayscale,-1, kernel)

img_set = [rgb_img, grayscale,custom_kernel, built_in_kernel]
title_set = ['RGB', 'GRAYSCALE', 'CUSTOM', 'BUILT-IN']
plot_img(img_set, title_set)