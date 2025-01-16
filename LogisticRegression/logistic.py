import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

plt.style.use("cyberpunk")

sigmoid = lambda z: 1 / (1 + np.exp(-z))

x = np.linspace(-np.pi, np.pi, 150)
print(x.shape)

plt.plot(x, sigmoid(x))

mplcyberpunk.make_lines_glow()
plt.show()
