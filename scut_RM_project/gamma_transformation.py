import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./dark.jpg',0)

plt.figure(figsize=(15,15))
plt.subplot(131)
plt.title('gamma = 1')    
plt.imshow(img, cmap = 'gray')   # 原图

# 默认gamma值为1.0，默认不变化   
def adjust_gamma(image, gamma=1.0):
    invgamma = 1/gamma
    brighter_image = np.array(np.power((image/255), invgamma)*255, dtype=np.uint8)
    return brighter_image

# gamma大于1，变亮
img_gamma = adjust_gamma(img, gamma=3.0) 
plt.subplot(132)
plt.title('gamma > 1')
plt.imshow(img_gamma, cmap="gray")

# gamma小于1，变暗
img_gamma = adjust_gamma(img, gamma=0.5) 
plt.subplot(133)
plt.title('gamma < 1')
plt.imshow(img_gamma, cmap="gray")

plt.show()
