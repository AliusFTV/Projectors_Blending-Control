import cv2
import numpy as np


class ImageProcessor:
    def __init__(self):
        pass

    @staticmethod
    def adjust_brightness(image):
        adjusted_image = cv2.addWeighted(image, 1.0, np.zeros(image.shape, image.dtype), 0.5, 0)
        return adjusted_image

    @staticmethod
    def enhance_sharpness(image):
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpened_image = cv2.filter2D(image, -1, kernel)
        return sharpened_image

    @staticmethod
    def increase_resolution(image, scale_factor=2.0):
        width = int(image.shape[1] * scale_factor)
        height = int(image.shape[0] * scale_factor)
        dim = (width, height)
        resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
        return resized_image

