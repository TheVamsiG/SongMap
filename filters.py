import pywt
import numpy as np
import cv2
from PIL import Image
from io import BytesIO
import numpy.matlib

class Filters():
    """Contains all the filters that we implemented
    These are all static methods to use, first type
    from filters import Filters
    left_wavelet, right_wavelet = Filters.wavelet_filter(left_img, right_img, 'LL')
    left_gabor, right_gabor = Filters.gabor_filter...
    """

    @staticmethod
    def wavelet_filter(left_img, right_img, filter_type):
        """
        Implements Wavelet Filtering
        LL - Low low, LH - Low High, HL - High Low, HH - High High
        """
        coeffsL = pywt.dwt2(left_img, 'bior1.3', mode='periodization')
        coeffsR = pywt.dwt2(right_img, 'bior1.3', mode='periodization')

        LLL, (LHL, HLL, HHL) = coeffsL
        LLR, (LHR, HLR, HHR) = coeffsR
        if filter_type == 'LL':
            LLL = numpy.matlib.repmat(LLL, 2, 2)
            LLR = numpy.matlib.repmat(LLR, 2, 2)
            LLL = .5*left_img + .5*LLL
            LLR = .5*right_img + .5*LLR
            return LLL, LLR
        if filter_type == 'LH':
            LHL = numpy.matlib.repmat(LHL, 2, 2)
            LHR = numpy.matlib.repmat(LHR, 2, 2)
            LHL = .5*left_img + .5*LHL
            LHR = .5*right_img + .5*LHR
            return LHL, LHR
        if filter_type == 'HL':
            HLL = numpy.matlib.repmat(HLL, 2, 2)
            HLR = numpy.matlib.repmat(HLR, 2, 2)
            HLL = .5*left_img + .5*HLL
            HLR = .5*right_img + .5*HLR
            return HLL, HLR

        HHL = numpy.matlib.repmat(HHL, 2, 2)
        HHR = numpy.matlib.repmat(HHR, 2, 2)
        HHL = .5*left_img + .5*HHL
        HHR = .5*right_img + .5*HHR
        return HHL, HHR

    @staticmethod
    def gabor_filter(left_img, right_img, filter_angle):
        """
        Implements gabor filtering
        takes any angle in radians
        """
        params = {'ksize':(31, 31), 'sigma':1.5,
                  'theta':filter_angle, 'lambd':15.0, 'gamma':0.02,
                  'psi':0, 'ktype':cv2.CV_32F
                  }
        kern = cv2.getGaborKernel(**params)
        kern /= 1.5*kern.sum()
        left_filt = cv2.filter2D(left_img, cv2.CV_32F,kern)
        right_filt = cv2.filter2D(right_img, cv2.CV_32F,kern)
        right_filt = (right_filt/np.amax(np.abs(right_filt)))*8192
        left_filt = (left_filt/np.amax(np.abs(left_filt)))*8192


        left_filt = .75*left_filt + .25*left_img
        right_filt = .75*right_filt + .25*right_img

        return left_filt, right_filt

    @staticmethod
    def jpeg_decompose(left_img, right_img, quality):
        """
        Implements JPEG Compression
        This doesn't work properly, but it leads to some cool blocking affects that we can use
        """

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

    @staticmethod
    def bilateral_filter(left_img, right_img, window_size, param2, param3):
        """
        Implements Bilaterial Filtering
        """
        left_bilat = cv2.bilateralFilter((np.float32(left_img)/np.amax(np.amax(left_img))), window_size, param2, param3)
        right_bilat = cv2.bilateralFilter((np.float32(right_img)/np.amax(np.amax(right_img))), window_size, param2, param3)

        left_bilat = left_bilat * np.amax(np.abs(left_img))
        right_bilat = right_bilat * np.amax(np.abs(right_img))
        return left_bilat, right_bilat
