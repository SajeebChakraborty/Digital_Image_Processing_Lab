import numpy as np


def erosion(img, kernel, iterations=1):
    def erode(src, kernel):
        dst = np.ones(src.shape, dtype=np.uint8)
        for i in range(1, src.shape[0] - 1):
            for j in range(1, src.shape[1] - 1):
                if src[i, j] == 0:
                    dst[i-1:i+2, j-1:j+2] = np.zeros(kernel.shape)
        return dst
    for i in range(iterations):
        img = erode(img, kernel)
    return img
