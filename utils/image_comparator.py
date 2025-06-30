import cv2
from PIL import Image, ImageChops


class ImageComparator:
    @staticmethod
    def compare_images(image1_path, image2_path, diff_path=None, threshold=0.99):
        img1 = Image.open(image1_path)
        img2 = Image.open(image2_path)
        diff = ImageChops.difference(img1, img2)
        if diff.getbbox():
            if diff_path:
                diff.save(diff_path)
            return False
        return True

    @staticmethod
    def compare_images_ssim(image1_path, image2_path, threshold=0.99):
        img1 = cv2.imread(image1_path)
        img2 = cv2.imread(image2_path)

        if img1 is None or img2 is None:
            return False

        # Resize images to the same size if needed
        if img1.shape != img2.shape:
            img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

        # Compute Structural Similarity Index (SSIM)
        from skimage.metrics import structural_similarity as ssim

        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        score, _ = ssim(gray1, gray2, full=True)
        return score >= threshold
