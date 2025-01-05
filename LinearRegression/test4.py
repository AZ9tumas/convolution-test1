import matplotlib.pyplot as plt
import mplcyberpunk

# Apply the cyberpunk style
plt.style.use('cyberpunk')

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 5]

# Create the plot
plt.plot(x, y, marker='o', label='Sample Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Cyberpunk Themed Plot')
plt.legend()

# Add glow effects
mplcyberpunk.add_glow_effects()

# Display the plot
plt.show()

