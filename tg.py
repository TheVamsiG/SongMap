
import wavio
import numpy as np
from map_song import Map
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
from HypeFincher import HypeFincher

test = HypeFincher("sin", "sin", "sin", "sin")
test.LFO_EN(1, True, 5)
test.Synthesize()
