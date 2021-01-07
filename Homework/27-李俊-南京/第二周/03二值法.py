import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
三维空间映射到二值化图像的过程；
三维空间中域值 代表着一个平面 
当灰度图像上的点大于这个阈值平面时，会被映射到1，对应的二维图像就是白点，反之 映射为0，对应的二维图像为黑色。
'''
def RGB2GRAY(imgage):
    return 0.2125 * imgage[:,:,0] + 0.7154 * imgage[:,:,1]+ 0.0721* imgage[:,:,2]

def binaryzation(garyimg, th=0.5):
    binImg = np.copy(garyimg)
    binImg[garyimg >= th] = 1
    binImg[garyimg <= th] = 0
    return binImg


img = cv2.imread("/Users/sirlijun/Documents/009、八斗学院人工智能学习/003、八斗人工智能/第二周/代码/lenna.png")[:,:,[2,1,0]]

grayImg = RGB2GRAY (img/255)
binImg = binaryzation(grayImg)

plt.subplot(121)
plt.imshow(grayImg,cmap='gray')
plt.subplot(122)
plt.imshow(binImg,cmap='gray')
plt.show()
    
