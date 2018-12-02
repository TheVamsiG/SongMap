from PIL import Image
from io import BytesIO
import numpy as np
import wavio
import numpy as np
from numpy import ndarray
from map_song import Map

class Oscillator:

    "class to generate either a sin/square oscillator"

    def sinInit(self):

        map_sin = Map("C4.wav")
        c_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("D4.wav")
        d_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("E4.wav")
        e_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("F4.wav")
        f_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("G4.wav")
        g_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("A4.wav")
        a_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("B4.wav")
        b_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("C5.wav")
        c_5 = map_sin.get_grayscale_map()

        return [c_4, d_4, e_4, f_4, g_4, a_4, b_4, c_5]

    def sqInit(self):

        map_sin = Map("C4_SQ.wav")
        c_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("D4_SQ.wav")
        d_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("E4_SQ.wav")
        e_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("F4_SQ.wav")
        f_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("G4_SQ.wav")
        g_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("A4_SQ.wav")
        a_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("B4_SQ.wav")
        b_4 = map_sin.get_grayscale_map()
        map_sin.get_new_map("C5_SQ.wav")
        c_5 = map_sin.get_grayscale_map()

        return [c_4, d_4, e_4, f_4, g_4, a_4, b_4, c_5]

    def __init__(self, oscname):
        if oscname == "sin":
            self.osc = self.sinInit()
        elif oscname == "sq":
            self.osc = self.sqInit()
