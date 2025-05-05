import matplotlib.pyplot as plt
import numpy as np

# Core Functionality Demonstration

# 1. Basic Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', label='Sine Wave')  # Line plot with blue solid line
plt.title('Basic Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)  # Add grid
plt.legend()  # Add legend
plt.savefig('line_plot.png')  # Save instead of showing
plt.close()

# 2. Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='green')  # Bar chart with green bars
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.savefig('bar_chart.png')
plt.close()

# 3. Scatter Plot with Customization
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.5, cmap='viridis')  # Scatter with variable size and color
plt.title('Customized Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.colorbar(scatter, label='Color Scale')  # Add colorbar
plt.savefig('scatter_plot.png')
plt.close()

# 4. Subplots (Multiple Plots in One Figure)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10), sharex=True)  # Two subplots, stacked vertically
ax1.plot(x, y1, 'r-')  # Red sine wave
ax1.set_title('Sine Wave')
ax1.set_ylabel('sin(x)')
ax2.plot(x, y2, 'b-')  # Blue cosine wave
ax2.set_title('Cosine Wave')
ax2.set_xlabel('X Axis')
ax2.set_ylabel('cos(x)')
plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig('subplots.png')
plt.close()

