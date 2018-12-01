from PIL import Image
from io import BytesIO
import numpy as np


class JPEGConvert():
    def __init__(self, _left_img, _right_img):
        self.left_img = _left_img
        self.right_img = _right_img

    def generate_img(self, left_img, right_img):
        quality=100
        imageL = Image.fromarray(left_img).convert('RGB')
        imageR = Image.fromarray(right_img).convert('RGB')

        outL = BytesIO()
        outR = BytesIO()
        imageL.save(outL, format='jpeg', quality=quality, optimize=True)
        imageR.save(outR, format='jpeg', quality=quality, optimize=True)
        
        imageL = Image.open(outL)
        imageR = Image.open(outR)

        im_arrL = np.frombuffer(imageL.tobytes(), dtype=np.uint8)
        im_arrL = im_arrL.reshape((imageL.size[1], imageL.size[0], 3))

        left_gray = np.dot(im_arrL[...,:3], [.299, .587, .114])


        im_arrR = np.frombuffer(imageR.tobytes(), dtype=np.uint8)
        im_arrR = im_arrR.reshape((imageR.size[1], imageR.size[0], 3))


        right_gray = np.dot(im_arrR[...,:3], [.299, .587, .114])

        return left_gray, right_gray
