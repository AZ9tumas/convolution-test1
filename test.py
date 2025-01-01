from PIL import Image
from scipy.signal import convolve2d 
import numpy as np

image = Image.open("./prewitt operator/image1.png").convert("RGB")
img_arr = np.array(image)

sobel_kernel_x = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

sobel_kernel_y = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]
])

print(img_arr.shape)
final_img_arr = np.zeros_like(img_arr)

for channel in range(3):
    convolved_x = convolve2d(img_arr[:, :, channel], sobel_kernel_x, mode = "same")
    convolved_y = convolve2d(img_arr[:, :, channel], sobel_kernel_y, mode = "same")
    gradient = np.sqrt(convolved_x ** 2 + convolved_y ** 2)
    final_img_arr[:, :, channel] = np.clip(gradient, 0, 255)

final_img = Image.fromarray(final_img_arr)

final_img.save("./prewitt operator/image1_filter.png")
