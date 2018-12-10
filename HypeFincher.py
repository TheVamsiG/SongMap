import wavio
import numpy as np
from numpy import ndarray
from PIL import Image
from io import BytesIO
from map_song import Map
from LFO import LFO
from Oscillator import Oscillator
from filters import Filters
import cv2
import matplotlib.pyplot as plt

class HypeFincher:
    """
    Class to map sounds to images
    """

    def __init__(self, osc1type, osc2type, osc3type, osc4type):

        self.LFO1_stat = False
        self.LFO1_rate = 5;
        self.LFO2_stat = False
        self.LFO2_rate = 5;
        self.DIR_CON = 1
        self.W_Stat = False;
        self.Gab_Stat = False;
        self.Gab_Deg = 0;
        self.JPEG_Stat = False;
        self.Bilateral_Stat = False;
        self.Tom_Stat = False;
        self.Drake_Stat = False;


        """Initialization Function: reads file and errors if it doesn't exist """
        self.osc_1 = Oscillator(osc1type).osc;
        print("oscillator 1 has been initialized to ", osc1type)
        print("\n")
        self.osc_2 = Oscillator(osc2type).osc;
        print("oscillator 2 has been initialized to", osc2type)
        print("\n")
        self.TomL = cv2.imread("TOML.png")
        self.TomR = cv2.imread("TOMR.png")
        self.TomL = cv2.cvtColor(self.TomL, cv2.COLOR_BGR2GRAY)
        self.TomR = cv2.cvtColor(self.TomR, cv2.COLOR_BGR2GRAY)
        self.TomL = self.TomL/np.amax(np.abs(self.TomL))
        self.TomR = self.TomR/np.amax(np.abs(self.TomR))

        self.DrakeL = cv2.imread("DRAKEL.png")
        self.DrakeR = cv2.imread("DRAKER.png")
        self.DrakeL = cv2.cvtColor(self.DrakeL, cv2.COLOR_BGR2GRAY)
        self.DrakeR = cv2.cvtColor(self.DrakeR, cv2.COLOR_BGR2GRAY)
        self.DrakeL = self.DrakeL/np.amax(np.abs(self.DrakeL))
        self.DrakeR = self.DrakeR/np.amax(np.abs(self.DrakeR))



    def LFO_EN(self, lfon, status, rate):
        if isinstance(status, bool):
            if status == True:
                if lfon == 1:
                    self.LFO1_stat = True
                    self.LFO1_rate = rate
                elif lfon == 2:
                    self.LFO2_stat = True
                    self.LFO2_rate = rate
                else:
                    print("ERROR: THERE IS NO LFO ASSOCIATED WITH THE NUMBER ",lfon)
            else:
                self.LFO1_stat = False
        else:
            print("ERROR: ", status, " IS NOT A VALID STATE FOR LFO!")

        return

    def Wavelet_EN(self, status, type):
        if isinstance(status, bool):
            if status == True:
                if type == 'LL':
                    self.W_Stat = True
                    self.W_Type = type
                elif type == 'LH':
                    self.W_Stat = True
                    self.W_Type= type
                elif type == 'HH':
                    self.W_Stat = True
                    self.W_Type= type
                elif type == 'HL':
                    self.W_Stat = True
                    self.W_Type= type
                else:
                        print("ERROR: THERE IS NO LFO ASSOCIATED WITH THE NUMBER ",lfon)
            else:
                    self.W_Stat = False
        else:
                print("ERROR: ", status, " IS NOT A VALID STATE FOR LFO!")

        return

    def Gabor_EN(self, status, angle):

        self.Gab_Stat = status
        self.Gab_Deg = angle

        return

    def JPEG_EN(self, status, quality):

        self.JPEG_Stat = status

        return

    def Bilateral_EN(self, status, quality):

        self.Bilateral_Stat = status

    def TomCruise_En(self, status):

        self.Tom_Stat = status

    def Drake_EN(self, status):
        self.Drake_Stat = status



    def Synthesize(self):
        plot = 0;
        plt.gray()


        osc_1_l = [self.osc_1[0][0], self.osc_1[1][0], self.osc_1[2][0], self.osc_1[3][0], self.osc_1[4][0], self.osc_1[5][0], self.osc_1[6][0], self.osc_1[7][0]]
        osc_1_r = [self.osc_1[0][1], self.osc_1[1][1], self.osc_1[2][1], self.osc_1[3][1], self.osc_1[4][1], self.osc_1[5][1], self.osc_1[6][1], self.osc_1[7][1]]
        osc_2_l = [self.osc_2[0][0], self.osc_2[1][0], self.osc_2[2][0], self.osc_2[3][0], self.osc_2[4][0], self.osc_2[5][0], self.osc_2[6][0], self.osc_2[7][0]]
        osc_2_r = [self.osc_2[0][1], self.osc_2[1][1], self.osc_2[2][1], self.osc_2[3][1], self.osc_2[4][1], self.osc_2[5][1], self.osc_2[6][1], self.osc_2[7][1]]


        if self.Tom_Stat:
            for i in range(len(osc_1_l)):
                osc_1_l[i] = osc_1_l[i]*self.TomL
            for i in range(len(osc_1_r)):
                osc_1_r[i] = osc_1_r[i]*self.TomR
            print("success Tom Cruise enabled!")
            plot += 1;
            plt.figure(plot)
            plt.subplot(1,2,1)
            plt.imshow(self.osc_1[0][0])
            plt.title('Orignal Left Channel')
            plt.subplot(1,2,2)
            plt.imshow(osc_1_l[0])
            plt.title('Tom Cruise Left Channel')

        if self.Drake_Stat:
            for i in range(len(osc_1_l)):
                osc_1_l[i] = osc_1_l[i]*self.DrakeL
            for i in range(len(osc_1_r)):
                osc_1_r[i] = osc_1_r[i]*self.DrakeR
            print("success Drake enabled!")
            plot += 1;
            plt.figure(plot)
            plt.subplot(1,2,1)
            plt.imshow(self.osc_1[0][0])
            plt.title('Orignal Left Channel')
            plt.subplot(1,2,2)
            plt.imshow(osc_1_l[0])
            plt.title('Drake Left Channel')


        """filter bank"""


        if self.LFO1_stat:
            LFO1 = LFO(self.LFO1_rate)
            for i in range(len(osc_1_l)):
                osc_1_l[i] = np.multiply(LFO1.map_lfo[0], osc_1_l[i])
            for i in range(len(osc_1_r)):
                osc_1_r[i] = np.multiply(LFO1.map_lfo[1], osc_1_r[i])
            print("success LFO enabled!")
            plot += 1;
            plt.figure(plot)
            plt.subplot(1,2,1)
            plt.imshow(self.osc_1[0][0])
            plt.title('Orignal Left Channel')
            plt.subplot(1,2,2)
            plt.imshow(osc_1_l[0])
            plt.title('LFO on Left Channel')

        if self.W_Stat:
            for i in range(len(osc_1_l)):
                osc_1_l[i], osc_1_r[i] = Filters.wavelet_filter(osc_1_l[i], osc_1_r[i], self.W_Type);
            print("success Wavelet filtered!")
            plot += 1;
            plt.figure(plot)
            plt.subplot(1,2,1)
            plt.imshow(self.osc_1[0][0])
            plt.title('Orignal Left Channel')
            plt.subplot(1,2,2)
            plt.imshow(osc_1_l[0])
            plt.title('Wavelet on Left Channel')


        if self.Gab_Stat:
            for i in range(len(osc_1_l)):
                osc_1_l[i], osc_1_r[i] = Filters.gabor_filter(osc_1_l[i], osc_1_r[i], self.Gab_Deg);
            print("success Gabor filtered!")
            plot += 1;
            plt.figure(plot)
            plt.subplot(1,2,1)
            plt.imshow(self.osc_1[0][0])
            plt.title('Orignal Left Channel')
            plt.subplot(1,2,2)
            gab_im = self.osc_1[0][0]-osc_1_l[0]
            plt.imshow(osc_1_l[0])
            plt.title('Gabor on Left Channel')

        if self.JPEG_Stat:
            for i in range(len(osc_1_l)):
                osc_1_l[i], osc_1_r[i] = Filters.jpeg_decompose(osc_1_l[i], osc_1_r[i], 100);
            print("success JPEG decomposed!")
            plot += 1;
            plt.figure(plot)
            plt.subplot(1,2,1)
            plt.imshow(self.osc_1[0][0])
            plt.title('Orignal Left Channel')
            plt.subplot(1,2,2)
            plt.imshow(osc_1_l[0])
            plt.title('JPEG on Left Channel')

        if self.Bilateral_Stat:
            for i in range(len(osc_1_l)):
                osc_1_l[i], osc_1_r[i] = Filters.bilateral_filter(osc_1_l[i], osc_1_r[i], 3, 25, 25);
            print("success Bilaterial filtered!")
            plot += 1;
            plt.figure(plot)
            plt.subplot(1,2,1)
            plt.imshow(self.osc_1[0][0])
            plt.title('Orignal Left Channel')
            plt.subplot(1,2,2)
            plt.imshow(osc_1_l[0])
            plt.title('Denoise/Smoothing on Left Channel')


        plt.show()

        """recombine"""
        self.osc_1 = [[osc_1_l[0], osc_1_r[0]], [osc_1_l[1], osc_1_r[1]],[osc_1_l[2], osc_1_r[2]],[osc_1_l[3], osc_1_r[3]],[osc_1_l[4], osc_1_r[4]],[osc_1_l[5], osc_1_r[5]], [osc_1_l[6], osc_1_r[6]], [osc_1_l[7], osc_1_r[7]]]


        return self.osc_1
