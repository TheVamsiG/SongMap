
import wavio
import numpy as np
from map_song import Map
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
from HypeFincher import HypeFincher
try:
    import pyaudio
except Exception:
    print ('Please download pyaudio, run \n brew install port audio \n pip install pyaudio')
    exit(0)

def play_on_key(map_instance, left_img, right_img):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                         channels=2,
                         rate=map_instance.wave.rate,
                         output=True)
    new_data = np.int16(map_instance.get_map_value(left_img, right_img))
    stream.write(new_data.tostring())
    stream.close()

def play_sine(synth_array, index, map_instance):
    desired_array = synth_array[index]
    play_on_key(map_instance, desired_array[0], desired_array[1])

mappy = Map('440SIN.wav')

test = HypeFincher("sin", "sin", "sin", "sin")

test.LFO_EN(1, True, 5)
test.Wavelet_EN(False, 'LL')
test.Gabor_EN(False, (np.pi/4))
test.JPEG_EN(False, 100)
test.Bilateral_EN(False, 1)
test.TomCruise_En(False)
test.Drake_EN(False)




vamsi_test_wf = test.Synthesize()
print(len(vamsi_test_wf))
while(1):
    key = input('Play Key')
    try:
        key = int(key)
        if key<9 and key>0:
            play_sine(vamsi_test_wf, key-1, mappy)
    except Exception:
        print('goodbye')
        break
