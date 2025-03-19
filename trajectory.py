import numpy as np
import matplotlib.pyplot as plt

# Define the function
def parabola(x):
    return -4.8*x*x + 12*x + 5

# Generate x values
x = np.linspace(-0, 3, 400)

# Compute y values
y = parabola(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$y = (2-x)*(x+3)$', color='b')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parabolic Trajectory: $y = x^2 + x - 1$')
plt.show()



-4.8x^2 + 12x + 5

x = 12/9.6
-4.8*x*x + 12*x + 5

