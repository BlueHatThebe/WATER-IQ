import numpy as np
from scipy import special
import matplotlib.pyplot as plt

# Parameters
r_max = 10.0  # Maximum radial distance
num_points = 500  # Number of points for computation
wavelength = 0.5  # Wavelength of light (in micrometers)
k = 2 * np.pi / wavelength  # Wave number
aperture_radius = 1.0  # Radius of the circular aperture

# Create radial grid
r = np.linspace(0, r_max, num_points)
theta = np.linspace(0, 2 * np.pi, num_points)
R, Theta = np.meshgrid(r, theta)

# Compute Bessel function for diffraction pattern
# Intensity is proportional to [2*J1(kr)/(kr)]^2
kr = k * aperture_radius * R
bessel_term = special.j1(kr)  # First-order Bessel function of the first kind
intensity = (2 * bessel_term / (kr + 1e-10))**2  # Avoid division by zero

# Average over theta to get radial intensity profile
radial_intensity = np.mean(intensity, axis=0)

# Create 2D intensity pattern for visualization
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Plotting
plt.figure(figsize=(12, 5))

# 2D intensity pattern
plt.subplot(1, 2, 1)
plt.pcolormesh(X, Y, intensity, cmap='inferno')
plt.colorbar(label='Intensity')
plt.title('2D Diffraction Pattern')
plt.xlabel('X (μm)')
plt.ylabel('Y (μm)')
plt.axis('square')

# Radial intensity profile
plt.subplot(1, 2, 2)
plt.plot(r, radial_intensity, 'b-', label='Radial Intensity')
plt.title('Radial Intensity Profile')
plt.xlabel('Radial Distance (μm)')
plt.ylabel('Intensity')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Compute and print the position of the first minimum (Airy disk radius)
first_zero = special.jn_zeros(1, 1)[0]  # First zero of J1
airy_radius = first_zero / (k * aperture_radius)
print(f"Airy disk radius: {airy_radius:.3f} micrometers")