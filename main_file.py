import numpy as np
from map_song import Map
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
                         output=True,
                         output_device_index=1)
    new_data = np.int16(map_instance.get_map_value(left_img, right_img))
    stream.write(new_data.tostring())
    stream.close()
    
mappy = Map('440SIN.wav')
[left_gray, right_gray] = mappy.get_grayscale_map()
while(1):
    key = input('Play Key ')
    if key == 'E':
        break
    if key == 'C':
        play_on_key(mappy, left_gray, right_gray)

