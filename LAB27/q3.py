"""Copy the following lines into your code and
rng = np.random.default_rng(7)
length = rng.integers(50, 800, size=100) # amino acids
weight = length * 0.11 + rng.normal(0, 3, size=100) # kDa (about 110 Da per residue)
membrane = rng.random(100) < 0.3
1. Plot a scatter plot of molecular weight against length, with membrane and soluble
proteins in different colours and marker shapes, and a legend.
2. Ues alpha so overlapping points stay visible.
3. Save the figure as protein_size.png at 150dpi, then open the file to check it. Your
plot should show a streight line trend with 30 membrane proteins mixed throughout the
cloud."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
length = rng.integers(50, 800, size=100)
weight = length * 0.11 + rng.normal(0, 3, size=100)
membrane = rng.random(100) < 0.3

fig, ax = plt.subplots()

ax.scatter(length[~membrane], weight[~membrane], color="tab:blue", marker="o", alpha=0.6, label="Soluble")
ax.scatter(length[membrane], weight[membrane], color="tab:orange", marker="s", alpha=0.6, label="Membrane")

ax.set_title("Protein Molecular Weight vs Length")
ax.set_xlabel("Length (amino acids)")
ax.set_ylabel("Molecular Weight (kDa)")
ax.legend()

fig.savefig("protein_size.png")
plt.show()

#2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("protein_size.png")

fig, ax = plt.subplots()
ax.imshow(img)
ax.axis("off")
plt.show()