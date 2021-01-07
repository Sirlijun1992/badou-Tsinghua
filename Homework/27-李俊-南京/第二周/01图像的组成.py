import cv2
import matplotlib.pyplot as plt

'''
1、查看图像组成结构
2、更换颜色通道顺序，看看最终显示效果
3、查看通道像素值
'''
img = plt.imread("/Users/sirlijun/Documents/009、八斗学院人工智能学习/003、八斗人工智能/第二周/代码/lenna.png") 
#<class 'numpy.ndarray'>
#print(type(img))   
#print(img[:10,:10,:])
# 顺序默认为012   下面更换了颜色的通道
rgb_img = img[:,:,[2,1,0]]
plt.imshow(rgb_img)
print(rgb_img[:10,:10,:])
plt.show()

#提取R、G、B分量
(B,G,R) = cv2.split(img)
cv2.imshow("Red",R)
cv2.imshow("Green",G)
cv2.imshow("Blue",B)
cv2.waitKey(0)
