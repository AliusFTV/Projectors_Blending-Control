import cv2
import numpy as np


class ImageProcessor:
    def __init__(self):
        pass

    @staticmethod
    def adjust_brightness(image, ambient_light):
        adjusted_image = cv2.addWeighted(image, 1.0, ambient_light, 0.5, 0)
        return adjusted_image

    @staticmethod
    def enhance_sharpness(image):
        sharpened_image = cv2.filter2D(image, -1, kernel=np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))
        return sharpened_image

    @staticmethod
    def increase_resolution(image, scale_factor):
        resized_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
        return resized_image

