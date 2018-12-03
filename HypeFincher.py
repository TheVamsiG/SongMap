import wavio
import numpy as np
from numpy import ndarray
from PIL import Image
from io import BytesIO
from map_song import Map
from LFO import LFO
from Oscillator import Oscillator

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



        """Initialization Function: reads file and errors if it doesn't exist """
        self.osc_1 = Oscillator(osc1type).osc;
        print("oscillator 1 has been initialized to ", osc1type)
        print("\n")
        self.osc_2 = Oscillator(osc2type).osc;
        print("oscillator 2 has been initialized to", osc2type)
        print("\n")
        self.osc_3 = Oscillator(osc3type).osc;
        print("oscillator 3 has been initialized to", osc3type)
        print("\n")
        self.osc_4 = Oscillator(osc4type).osc;
        print("oscillator 4 has been initialized to", osc4type)
        print("\n")


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

    def Synthesize(self):

        osc_1_l = [self.osc_1[0][0], self.osc_1[1][0], self.osc_1[2][0], self.osc_1[3][0], self.osc_1[4][0], self.osc_1[5][0], self.osc_1[6][0], self.osc_1[7][0]]
        osc_1_r = [self.osc_1[0][1], self.osc_1[1][1], self.osc_1[2][1], self.osc_1[3][1], self.osc_1[4][1], self.osc_1[5][1], self.osc_1[6][1], self.osc_1[7][1]]
        osc_2_l = [self.osc_2[0][0], self.osc_2[1][0], self.osc_2[2][0], self.osc_2[3][0], self.osc_2[4][0], self.osc_2[5][0], self.osc_2[6][0], self.osc_2[7][0]]
        osc_2_r = [self.osc_2[0][1], self.osc_2[1][1], self.osc_2[2][1], self.osc_2[3][1], self.osc_2[4][1], self.osc_2[5][1], self.osc_2[6][1], self.osc_2[7][1]]
        osc_3 = self.osc_3
        osc_4 = self.osc_4

        if self.LFO1_stat:
            LFO1 = LFO(self.LFO1_rate)
            for i in range(len(osc_1_l)):
                osc_1_l[i] = np.multiply(LFO1.map_lfo[0], osc_1_l[i])
            for i in range(len(osc_1_r)):
                osc_1_r[i] = np.multiply(LFO1.map_lfo[1], osc_1_r[i])
            print("success!")

        return self.osc_3
