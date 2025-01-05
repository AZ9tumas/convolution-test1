import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Apply the dark theme
plt.style.use("cyberpunk")

weight = np.array([1, 2, 3, 4, 5])
size = np.array([2.9, 4, 5, 7, 12])

weight_mean = np.mean(weight)
size_mean = np.mean(size)

m = sum( (weight[i] - weight_mean) * (size[i] - size_mean) for i in range(len(weight)) ) / sum ((weight[i] - weight_mean) ** 2 for i in range(len(weight)))
c = size_mean - m * weight_mean
print(m)

predicted_size = m * weight + c

plt.plot(weight, size, color = "orange", marker = "o")
plt.plot(weight, predicted_size, color = "green", marker = "D")

mplcyberpunk.make_lines_glow()

plt.show()
