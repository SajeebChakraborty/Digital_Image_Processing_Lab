import numpy as np


def dialation(img, kernel, iterations=1):
    def dilate(src, kernel):
        dst = np.zeros(src.shape, dtype=np.uint8)
        for i in range(1, src.shape[0] - 1):
            for j in range(1, src.shape[1] - 1):
                if src[i, j] == 255:
                    dst[i-1:i+2, j-1:j+2] = kernel
        return dst
    for i in range(iterations):
        img = dilate(img, kernel)
    return img

