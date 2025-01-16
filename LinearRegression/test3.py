import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Apply the dark theme
plt.style.use("cyberpunk")

weight = np.array([1, 2, 3, 4, 5])
size = np.array([2.9, 4, 5, 7, 12])

weight_mean = np.mean(weight)
size_mean = np.mean(size)

total_sum_of_squares = sum((size[i] - size_mean) ** 2 for i in range(len(size)))
m = sum( (weight[i] - weight_mean) * (size[i] - size_mean) for i in range(len(weight)) ) / sum ((weight[i] - weight_mean) ** 2 for i in range(len(weight)))
c = size_mean - m * weight_mean
print(f"m = {m}\nc = {c}")

predicted_size = m * weight + c

residual_sum_of_squares = sum((size[i] - predicted_size[i]) ** 2 for i in range(len(size)))

r_squared = 1 - residual_sum_of_squares / total_sum_of_squares

print(f"R^2 = {r_squared}")

plt.plot(weight, size, color = "orange", marker = "o")
plt.plot(weight, predicted_size, color = "green", marker = "D")

mplcyberpunk.make_lines_glow()

plt.show()
