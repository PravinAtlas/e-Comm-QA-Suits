from PIL import Image, ImageChops

class ImageComparator:
    @staticmethod
    def compare_images(image1_path, image2_path, diff_path=None):
        img1 = Image.open(image1_path)
        img2 = Image.open(image2_path)
        diff = ImageChops.difference(img1, img2)
        if diff.getbbox():
            if diff_path:
                diff.save(diff_path)
            return False
        return True