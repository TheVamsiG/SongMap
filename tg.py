
import wavio
import numpy as np
from map_song import Map
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


mapper_sin = Map("LFO_10.wav")
mapper_wn = Map("LFO_15.wav")

im_gray = mapper_sin.get_grayscale_map()
plt.gray()

im_grayb = mapper_wn.get_grayscale_map()
#filter = ((im_grayb[0])/np.amax(np.amax(im_grayb[0])))
#im_graydnl = cv2.bilateralFilter((np.float32(im_grayb[0])/np.amax(np.amax(im_grayb[0]))), 3, 25, 25)
#im_graydnr = cv2.bilateralFilter((np.float32(im_grayb[0])/np.amax(np.amax(im_grayb[0]))), 3, 25, 25)


plt.subplot(1,2,1)
plt.imshow(im_grayb[0])
plt.title("left")
plt.subplot(1,2,2)
plt.imshow(im_grayb[1])
plt.title("right")


plt.figure()
plt.subplot(1,2,1)
plt.imshow(im_gray[0])
plt.title("left")
plt.subplot(1,2,2)
plt.imshow(im_gray[1])
plt.title("right")

plt.show()

mapper_wn.get_remap(im_graydnl, im_graydnr)
