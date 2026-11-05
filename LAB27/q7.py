import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
sigmas = [1, 1.5, 2]

fig, ax = plt.subplots()

for sigma in sigmas:
    g = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(- (x**2) / (2 * sigma**2))
    ax.plot(x, g, label=rf"$\sigma = {sigma}$")

ax.set_xlabel("x")
ax.set_ylabel("g(x)")
ax.set_title("Normalized Gaussian Distributions")
ax.legend()

fig.savefig("gaussian_curves.png")
plt.show()