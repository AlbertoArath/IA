import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

# Define the x values from 0 to 3π/2
x = np.linspace(0, 3 * np.pi / 2, 1000)

# Define the function e^(-x) * cos(8x)
y = np.exp(-x) * np.cos(8 * x)
y1 = - np.exp(-x)
y2 = np.exp(-x)

# Find the local maxima (crests) and minima (troughs)
crests = argrelextrema(y, np.greater)[0]  # Indices of the local maxima
troughs = argrelextrema(y, np.less)[0]    # Indices of the local minima

# Create the plot
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Plot the original function
ax1.plot(x, y, label=r'$e^{-x} \cdot \cos(8x)$', color='#0087F0')
ax1.plot(x, y2, label=r'$e^{-x}$', color='orange', linewidth=2, alpha=0.8)
ax1.plot(x, y1, label=r'$-e^{-x}$', color='orange', linewidth=2, alpha=0.8)

# Plot red dots at the crests and troughs
ax1.plot(x[crests], y[crests], 'ro', label='Crests')
ax1.plot(x[troughs], y[troughs], 'ro', label='Troughs')

# Set title and legend
ax1.set_title(r' f(x) = $e^{-x} \cos(8x)$')
ax1.legend()

# Customize axis positions and ticks as before
xticks = np.arange(0, 3 * np.pi / 2 + np.pi / 8, np.pi / 8)
xtick_labels = []
for i in range(len(xticks)):
    if i == 0:
        xtick_labels.append("")
    else:
        xtick_labels.append(r'$\frac{' + str(i) + r'\pi}{8}$')

ax1.set_xticks(xticks)
ax1.set_xticklabels(xtick_labels, rotation=45)
ax1.set_yticks([-1, 1])
ax1.set_yticklabels(['-1', '1'])

# Customize spines (axes)
ax1.spines['left'].set_position('zero')
ax1.spines['bottom'].set_position('zero')
ax1.spines['top'].set_color('none')
ax1.spines['right'].set_color('none')

fig.set_facecolor('#f0f0f0')
ax1.set_facecolor('#d9d9d9')

# Show the plot
plt.show()