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
    gray=gray/255
    plt.subplot(2,4,2)
    plt.imshow(gray,cmap='gray')
    plt.title('GRAY')
   

    F=np.fft.fftshift(np.fft.fft2(gray))
    plt.subplot(2,4,3)
    plt.imshow(np.log1p(np.abs(F)),cmap='gray')


    P,Q=F.shape
    H=np.zeros((P,Q),dtype=np.float32)
    for u in range(P):
        for v in range(Q):
            H[u,v]=-4*np.pi*np.pi*((u-P/2)**2+(v-Q/2)**2)

    plt.subplot(2,4,4)
    plt.imshow(H,cmap='gray')
    plt.title('Laplacian Filter')

 
    Lap=H*F
    Lap=np.fft.ifftshift(Lap)
    Lap=np.real(np.fft.ifft2(Lap))

    plt.subplot(2,4,5)
    plt.imshow(Lap,cmap='gray')
    plt.title('Laplacian Image')

    old_image=np.max(Lap)-np.min(Lap)
    new_range=1 -(-1)
    laplacian_filter=(((Lap-np.min(Lap))*new_range)/old_image)+(-1)
    plt.subplot(2,4,6)
    plt.imshow(laplacian_filter,cmap='gray')
    plt.title('Laplacian Image Scaled')

    c = -1
    g = gray+ c*laplacian_filter
    g = np.clip(g, 0, 1)
    plt.subplot(2,4,7)
    plt.imshow(g,cmap='gray')
    plt.title('Laplacian')
    plt.savefig('Laplacian.jpg')
    plt.show()

if __name__ == '__main__':
    main()