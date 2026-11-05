import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 1000)

f1 = np.log(1 / (np.cos(x)**2))
f2 = np.log(1 / (np.sin(x)**2))

fig, ax = plt.subplots()
ax.plot(x, f1, label=r"$f_1(x) = \ln(1 / \cos^2 x)$")
ax.plot(x, f2, label=r"$f_2(x) = \ln(1 / \sin^2 x)$")

ax.set_ylim(-1, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Trigonometric Logarithmic Functions")
ax.legend()

fig.savefig("trig_functions.png")
plt.show()