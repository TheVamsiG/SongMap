import wavio
import numpy as np
from numpy import ndarray


class Map:
    """
    Class to map songs to images
    """

    #self.right_gray_image
    #self.left_gray_image

    def __init__(self, filename):
        """Initialization Function: reads file and errors if it doesn't exist """
        try:
            self.wave = wavio.read(filename)
            self.left_channel = self.wave.data[:, 0]
            self.right_channel = self.wave.data[:, 1]
        except Exception:
            self.wave = None
            raise Exception("Could not read the file")


    def get_grayscale_map(self):

        """ Creates Grayscale Image in a square of waveform sent in"""
        left_crop = self.left_channel[:int(np.sqrt(len(self.left_channel)))**2]
        right_crop = self.right_channel[:int(np.sqrt(len(self.right_channel)))**2]
        left_gray_image = np.reshape(left_crop, (int(np.sqrt(len(self.left_channel))), int(np.sqrt(len(self.left_channel)))))
        right_gray_image = np.reshape(right_crop, (int(np.sqrt(len(self.right_channel))), int(np.sqrt(len(self.left_channel)))))

        return [left_gray_image, right_gray_image]

    def get_new_map(self, filename):

        self.wave = wavio.read(filename)
        self.left_channel = self.wave.data[:, 0]
        self.right_channel = self.wave.data[:, 1]

        return


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
    def get_map_value(self, tobrml, tobrmr):

        left_channel_rrshape = np.reshape(tobrml, (1, tobrml.shape[1]**2))
        right_channel_rrshape = np.reshape(tobrmr, (1, tobrmr.shape[1]**2))
        new_data = np.zeros((tobrml.shape[1]**2, 2))
        new_data[:,0] = left_channel_rrshape
        new_data[:,1] = left_channel_rrshape
        swidth = 2;

        return new_data

    def get_remap(self, tobrml, tobrmr):
        new_data = get_mat_value(tobrml, tobrmr)
        wavio.write("remap.wav", new_data, rate=self.wave.rate, sampwidth=self.wave.sampwidth);

        return
