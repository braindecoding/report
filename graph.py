import matplotlib.pyplot as plt
import numpy as np

# Current data from the image
methods = ['Miyawaki', 'BCCA', 'DCCAE-A', 'DCCAE-S', 'De-CNN', 'DGMM', 'ifir']
binary_patterns_mse = [0.3, 0.25, 0.23, 0.27, 0.1, 0.08, 0.0276]
handwritten_digits_mse = [0.22, 0.18, 0.15, 0.12, 0.05, 0.03, 0.0276]

# Error bars are just example values, if you have the specific values, they should be replaced
binary_patterns_error = [0.05] * len(methods)
handwritten_digits_error = [0.02] * len(methods)

# Creating the figure and axes
fig, ax = plt.subplots()

# Bar width
bar_width = 0.35

# X locations for groups
index = np.arange(len(methods))

# Plotting both categories
bar1 = ax.bar(index - bar_width/2, binary_patterns_mse, bar_width, label='Binary patterns',
              yerr=binary_patterns_error, capsize=5, color='r')
bar2 = ax.bar(index + bar_width/2, handwritten_digits_mse, bar_width, label='Handwritten digits',
              yerr=handwritten_digits_error, capsize=5, color='y')

# Labels, title and axes ticks
ax.set_xlabel('Methods')
ax.set_ylabel('Average MSE')
ax.set_title('Average MSE by method and category')
ax.set_xticks(index)
ax.set_xticklabels(methods, rotation=45, ha="right")
ax.legend()

# Make the y-axis label, ticks and tick labels match the line color.
ax.tick_params('y')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xticks(index)
ax.set_xticklabels(methods)

# Save the figure
plt.tight_layout()
output_file = '/mnt/data/updated_mse_chart.png'
plt.savefig(output_file)

output_file
