import numpy as np
import cv2
from PIL import Image
from scipy.signal import convolve2d

def apply_sobel_filter(image_path : str, final_image_path : str):

    image = Image.open(image_path).convert("RGB")
    img_arr = np.array(image)

    final_arr = np.zeros_like(img_arr)

    kernel_x = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

    kernel_y = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])

    for channel in range(3):
        convoluted_x = convolve2d(img_arr[:, :, channel], kernel_x, mode = "same")
        convoluted_y = convolve2d(img_arr[:, :, channel], kernel_y, mode = "same")

        gradient = np.sqrt(convoluted_x ** 2 + convoluted_y ** 2)

        final_arr[:, :, channel] = np.clip(gradient, 0, 255)

    final_img = Image.fromarray(final_arr)
    final_img.save(final_image_path)

    print("Applied Sobel's filter.")

    return final_arr


def binarize(image_path : str, final_image_path = "binarized.png", threshold : int = 0):
    
    if not threshold:
        # Calculate optimal threshold
        print("Applying Otsu's method for optimal threshold.")
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        threshold, binarized = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    else:
        img = Image.open(image_path).convert("L")
        img_arr = np.array(img)
        binarized = np.where(img_arr < threshold, 0, 255).astype(np.uint8)

    binarized_image = Image.fromarray(binarized)
    binarized_image.save(final_image_path)
    
    print("Binarization done. Threshold =", threshold)

    return np.array(binarized)
    

# apply_sobel_filter("./smooth.png", "./filter_1.png")
binarize(image_path = "./filter_1.png")
