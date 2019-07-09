import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
# %matplotlib inline

img = cv2.imread('./other/undistort_img/a.jpg')
print(img.size)

plt.rcParams['figure.figsize'] = (400, 200) # 设置figure_size尺寸

plt.imshow(img)
plt.show()
