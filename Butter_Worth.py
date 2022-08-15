import matplotlib.pyplot as plt 
import cv2 
import numpy as np 

def main():

    img_path='./image.jpg'
    rgb=plt.imread(img_path)
    print(rgb.shape)
    plt.subplot(2,4,1)
    plt.imshow(rgb)
    plt.title('RGB')

    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(gray.shape)
    plt.subplot(2,4,2)
    plt.imshow(gray,cmap='gray')
    plt.title('Gray')

    F=np.fft.fft2(gray)
    plt.subplot(2,4,3)
    plt.imshow(np.log1p(np.abs(F)),cmap='gray')
    plt.title('FFT')

    shift_the_f_img=np.fft.fftshift(F)
    plt.subplot(2,4,4)
    plt.imshow(np.log1p(np.abs(shift_the_f_img)),cmap='gray')
    plt.title('Centered')

    
    M,N=gray.shape
    H=np.zeros((M,N),dtype=np.float32)
    D0=10
    n=10
    for u in range(M):
        for v in range(N):
            D=np.sqrt((u-M/2)**2+(v-N/2)**2)
            H[u,v]=1/(1+(D/D0)**n)
    
    plt.subplot(2,4,5)
    plt.imshow(H,cmap='gray')
    plt.title('Butterworth')

    btter_shift =shift_the_f_img*H
    G=np.fft.ifftshift(btter_shift)
    g=np.abs(np.fft.ifft2(G))

    plt.subplot(2,4,6)
    plt.imshow(g,cmap='gray')
    plt.title('Apply Butter filter')
    
    plt.savefig('Butter.jpg')
    plt.show()

    


if __name__ == '__main__':
    main()