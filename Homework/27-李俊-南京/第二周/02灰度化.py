import cv2
import matplotlib.pyplot as plt

'''
知识点：
任何一个彩色图像他在空间域的点 都是由一个三维的向量组成， f(x,y) = (r,g,b)  ==>f(10,10) = (64,128,10)
灰色图像空间域表示：f(x,y) = t（强度值  ）

彩色空间到灰色空间的 变化公式：#  Y灰度值 = 0.2125 R + 0.7154 G + 0.0721 B 
两点特性：
0.2125 +0.7154+0.0721 =1
0.2125*255 +0.7154*255+0.0721*255 =255 保证算出来的灰度值是0到255的区间

空间意义：彩色向量  到系数向量 的投影  （了解一下数学 向量中点积 知识点【在点积运算中，第一个向量投影到第二个向量上】）
''' 

def RGB2GRAY(imgage):
    return 0.2125 * imgage[:,:,0] + 0.7154 * imgage[:,:,1]+ 0.0721* imgage[:,:,2]

img = cv2.imread("/Users/sirlijun/Documents/009、八斗学院人工智能学习/003、八斗人工智能/第二周/代码/lenna.png")[:,:,[2,1,0]]

gray = RGB2GRAY (img)
print(img)
plt.imshow(img)
plt.figure()
plt.imshow(gray,cmap='gray')
plt.show()

