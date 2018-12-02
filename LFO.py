from PIL import Image
from io import BytesIO
import numpy as np
import wavio
import numpy as np
from numpy import ndarray
from map_song import Map

class LFO:

    def __init__(self, rate):
        if rate == 5:
            self.map_lfo = Map("LFO_5.wav").get_grayscale_map()
        elif rate == 10:
            self.map_lfo = Map("LFO_10.wav").get_grayscale_map()
        elif rate == 15:
            self.map_lfo = Map("LFO_15.wav").get_grayscale_map()
        elif rate == 20:
            self.map_lfo = Map("LFO_20.wav").get_grayscale_map()
