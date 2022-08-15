import cv2
import numpy as np
import matplotlib.pyplot as plt

# original image
f = plt.imread('./image.jpg')
plt.figure(figsize=(15,15))
plt.subplot(4,4,1)
plt.imshow(f, cmap='gray')
plt.title('RGB Image')

gray = cv2.cvtColor(f, cv2.COLOR_RGB2GRAY)
plt.subplot(4,4,2)
plt.imshow(gray, cmap='gray')
plt.title('Gray Image')

# image in frequency domain
F = np.fft.fft2(gray)
plt.subplot(4,4,3)
plt.imshow(np.log1p(np.abs(F)),cmap='gray')
plt.title('FFT Image')
# plt.show()

shift_fft = np.fft.fftshift(F)
plt.subplot(4,4,4)
plt.imshow(np.log1p(np.abs(shift_fft)),cmap='gray')
plt.title('Centered FFT Image')
# plt.show()

# Filter: Low pass filter
M,N = gray.shape
H = np.zeros((M,N), dtype=np.uint8)
D0 = 50
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        if D <= D0:
            H[u,v] = 1
        else:
            H[u,v] = 0
plt.subplot(4,4,5)
plt.imshow(H, cmap='gray')
plt.title('Low Pass Filter')
#plt.show()

# # Ideal Low Pass Filtering
shift_hl = shift_fft * H
plt.subplot(4,4,6)
plt.imshow(np.log1p(np.abs(shift_hl)),cmap='gray')
plt.title('centered & Low pass')
#plt.show()

# # Inverse Fourier Transform
g = np.abs(np.fft.ifft2(shift_hl))
plt.subplot(4,4,7)
plt.imshow(g, cmap='gray')
plt.title('Applied Filter')
#plt.show()


# # Filter: High pass filter
H = 1 - H
plt.subplot(4,4,8)
plt.imshow(H, cmap='gray')
plt.title('High Pass Filter')
#plt.show()


# # Ideal High Pass Filtering
shift_hl = shift_fft * H
plt.subplot(4,4,9)
plt.imshow(np.log1p(np.abs(shift_hl)),cmap='gray')
plt.title('centered & High pass')
#plt.show()

# # Inverse Fourier Transform
g = np.abs(np.fft.ifft2(shift_hl))
plt.subplot(4,4,10)
plt.imshow(g, cmap='gray')
plt.title('Applied High Filter')
plt.savefig('High_low.jpg')
plt.show()