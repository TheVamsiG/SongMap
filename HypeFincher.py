import wavio
import numpy as np
from numpy import ndarray
from PIL import Image
from io import BytesIO
from map_song import Map
from Oscillator import Oscillator

class HypeFincher:
    """
    Class to map sounds to images
    """

    def __init__(self, osc1type, osc2type, osc3type, osc4type):
         """Initialization Function: reads file and errors if it doesn't exist """
         self.osc_1 = Oscillator(osc1type).osc;
         print("oscillator 1 has been initialized to")
         print(osc1type)
         print("\n \n")
         self.osc_2 = Oscillator(osc2type).osc;
         print("oscillator 2 has been initialized to")
         print(osc2type)
         print("\n \n")
         self.osc_3 = Oscillator(osc3type).osc;
         print("oscillator 3 has been initialized to")
         print(osc3type)
         print("\n \n")
         self.osc_4 = Oscillator(osc4type).osc;
         print("oscillator 4 has been initialized to")
         print(osc4type)
         print("\n \n")
         self.synthesis = numpy.add(self.osc_1, self.osc_2, self.osc_3, self.osc_4)
