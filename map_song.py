#! /bin/usr/python3
import wavio
import numpy as np


class Map:
    """
    Class to map songs to images
    """
    def __init__(self, filename):
        """Initialization Function: reads file and errors if it doesn't exist """
        try:
            self.wave = wavio.read(filename)
        except Exception:
            self.wave = None
            raise Exception("Could not read the file")

    def get_grayscale_map(self):
        """ Creates Grayscale Image in a square of waveform sent in"""
        left_channel = self.wave.data[:, 0]
        left_clip = np.clip(left_channel, 0, left_channel.max())
        left_crop = left_clip[:int(np.sqrt(len(left_clip)))**2]
        return np.reshape(left_crop, (int(np.sqrt(len(left_clip))), int(np.sqrt(len(left_clip)))))

    def get_rgb_map(self):
        """ Creates RGB Image in a square of waveform sent in"""
        left_channel = self.wave.data[:, 0]

        red_image = np.array([left_channel[3*i] for i in range(int(len(left_channel)/3))])
        green_image = np.array([left_channel[3*i + 1] for i in range(int(len(left_channel)/3))])
        blue_image = np.array([left_channel[3*i + 2] for i in range(int(len(left_channel)/3))])

        red_crop = red_image[:int(np.sqrt(len(red_image)))**2]
        green_crop = green_image[:int(np.sqrt(len(green_image)))**2]
        blue_crop = blue_image[:int(np.sqrt(len(blue_image)))**2]

        red_reshape = np.reshape(red_crop, (int(np.sqrt(len(red_crop))), int(np.sqrt(len(red_crop)))))
        green_reshape = np.reshape(green_crop, (int(np.sqrt(len(green_crop))), int(np.sqrt(len(green_crop)))))
        blue_reshape = np.reshape(blue_crop, (int(np.sqrt(len(blue_crop))), int(np.sqrt(len(blue_crop))))) 

        image = np.zeros((len(red_reshape), len(red_reshape), 3))
        image[:, :, 0] = np.clip(red_reshape, 0, red_reshape.max())/red_reshape.max()
        image[:, :, 1] = np.clip(green_reshape, 0, green_reshape.max())/green_reshape.max()
        image[:, :, 2] = np.clip(blue_reshape, 0, blue_reshape.max())/blue_reshape.max()

        return image
