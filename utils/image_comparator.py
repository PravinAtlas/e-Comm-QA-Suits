import cv2
import numpy as np


class ImageComparator:
    @staticmethod
    def compare_images(image1_path, image2_path):
        img1 = cv2.imread(image1_path)
        img2 = cv2.imread(image2_path)
        if img1 is None or img2 is None:
            return False
        if img1.shape != img2.shape:
            img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        # Compare pixel values directly
        return np.array_equal(img1, img2)
