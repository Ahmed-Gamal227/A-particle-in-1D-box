import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Constants
L = 1.0  # Length of the box
n_states = 6  # Number of quantum states to animate
x = np.linspace(0, L, 500)  # Spatial grid
time = np.linspace(0, 2 * np.pi, 3000)  # Time grid (slightly more frames for smoother animation)

# Wavefunction Ψ(x, t) for a given quantum number n
def psi_t(x, n, L, t):
    k = n * np.pi / L  # Wave number
    omega = n**2  # Angular frequency (proportional to energy)
    return np.sqrt(2 / L) * np.sin(k * x) * np.cos(omega * t)

# Energy levels (proportional to n^2)
def energy(n):
    return n**2

# Create the figure
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, L)
ax.set_ylim(0, energy(n_states) + 1.5)
ax.set_xlabel("$x$ (Position)", fontsize=14)
ax.set_ylabel("$n$-state energy levels", fontsize=14)
ax.set_title("Particle in a 1D Infinite Potential Box", fontsize=16)

# Initialize plot elements
lines = []
colors = ["blue", "red", "green", "black", "orange", "purple"]  # Colors for different states
for n in range(1, n_states + 1):
    line, = ax.plot([], [], label=f"n={n}", color=colors[n - 1])
    lines.append(line)
    ax.hlines(energy(n), 0, L, linestyles="dotted", colors=colors[n - 1])  # Energy levels

# Draw box walls
ax.vlines(0, 0, energy(n_states) + 1.5, colors="gray", linestyles="solid")
ax.vlines(L, 0, energy(n_states) + 1.5, colors="gray", linestyles="solid")

# Add a legend
ax.legend(fontsize=12)

# Animation update function
def update(t):
    for n, line in enumerate(lines, start=1):
        wavefunction = psi_t(x, n, L, t)
        energy_level = energy(n)
        line.set_data(x, wavefunction + energy_level)  # Shift wavefunction by energy level
    return lines

# Create the animation
ani = FuncAnimation(fig, update, frames=time, blit=True, interval=40)  # Adjust interval for smoother speed

# Save animation as a video
#writer = FFMpegWriter(fps=60, metadata={"title": "Particle in a Box"})
#ani.save("particle_in_box.mp4", writer=writer)

print("Animation saved as 'particle_in_box.mp4'")
plt.show()