import cv2
import numpy as np
import matplotlib.pyplot as plt
'''
最近邻插值
图像放大时补充的像素取最临近的像素的值。

优缺点：
优点：方法简单，所以处理速度很快，
缺点：放大图像画质劣化明显
'''
import cv2 as cv
 
src = cv.imread("/Users/sirlijun/Documents/009、八斗学院人工智能学习/003、八斗人工智能/第二周/代码/lenna.png")
 
dst = cv.resize(src,(800,800),interpolation=cv.INTER_NEAREST)
 
cv.imshow('outImg', dst)
cv.imwrite("/Users/sirlijun/Documents/009、八斗学院人工智能学习/003、八斗人工智能/第二周/代码/lenna_bak.png", dst)
cv.waitKey(0)


