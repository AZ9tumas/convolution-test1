
import numpy as np
from scipy.signal import convolve2d
from PIL import Image

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
    
    return final_arr

