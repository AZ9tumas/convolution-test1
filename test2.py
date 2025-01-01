from PIL import Image
from scipy.signal import convolve2d
import numpy as np

def convolve_image(image_path = "./images.png", 
                   final_image_path = "final_image1.png", 
                   kernel = np.full((3, 3), 1/9)):

    image = Image.open(image_path).convert("RGB")
    img_arr = np.array(image)

    print("Image Shape: ", img_arr.shape)

    final_image_arr = np.zeros_like(img_arr)

    for channel in range(3):
        convolved_channel = convolve2d(img_arr[:, :, channel], kernel, mode = "same")
        final_image_arr[:, :, channel] = np.clip(convolved_channel, 0, 255)

    final_image = Image.fromarray(final_image_arr)
    final_image.save(final_image_path)

gaussian_filter = 1/16 * np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

convolve_image(
    image_path = "./images.png",
    kernel = gaussian_filter,
    final_image_path = "./binarization/smooth.png"
)
