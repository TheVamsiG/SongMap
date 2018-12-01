import numpy as np
import cv2

class GaborDecompose:
    def __init__(self, _left_gray, _right_gray):
        self.left_gray = _left_gray
        self.right_gray = _right_gray
    
    def gabor_decomp(self):
        filters = []
        ksize = 31
        for theta in np.arange(0, np.pi, np.pi / 32):
            params = {'ksize':(ksize, ksize), 'sigma':1.0, 'theta':theta, 'lambd':15.0,
              'gamma':0.02, 'psi':0, 'ktype':cv2.CV_32F}
            kern = cv2.getGaborKernel(**params)
            kern /= 1.5*kern.sum()
            filters.append((kern,params))
        
        gaborL = []
        gaborR = []
        for i in range(len(filters)):
            gaborL.append(cv2.filter2D(self.left_gray, cv2.CV_32F, filters[i][0]))
            gaborR.append(cv2.filter2D(self.right_gray, cv2.CV_32F, filters[i][0]))
        return gaborL, gaborR
