import pywt
import numpy as np


class WaveletDecompose():

    def __init__(self, _left_img, _right_img):
        self.left_img = _left_img
        self.right_img = _right_img

    def get_wavelet(self):
        coeffsL = pywt.dwt2(self.left_img, 'bior1.3')
        coeffsR = pywt.dwt2(self.right_img, 'bior1.3')

        LLL, (LHL, HLL, HHL) = coeffsL
        LLR, (LHR, HLR, HHR) = coeffsR

        return LLL, LHL, HLL, HHL, LLR, LHR, HLR, HHR
