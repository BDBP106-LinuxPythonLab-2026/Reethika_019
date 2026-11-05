"""Copy the following code into your program and
rng = np.random.default_rng(3)
organisms = ["E. coli", "S. cerevisiae", "P. falciparum", "S. coelicolor"]
mean_gc = [51, 38, 19, 72] # approximate genome GC content, %
1. Create a 2x2 grid with plt.subplots(2,2,sharex=True,sharey=True). What do
the options sharex and sharey do?
2. For each organism, simulate 1000 G,C values with rng.normal(gc,4,size=1000)
and draw a histogram in its own panel, using the same bins (np.arange(0,101,2)) for
all four.
3. Mark each mean with a dashed line, and put the organism and its mean in each
panel’s title.
4. Label only the outer axes, and add an overall title with fig.suptitle().

Your plot should show 4 peaks at roughly 19%, 38%, 51%, 72%. Because the x-axes are
shared, the difference between genomes are obvious at a glance."""

#1
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

fig.savefig("grid_setup.png")
plt.show()

#2
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)
organisms = ["E. coli", "S. cerevisiae", "P. falciparum", "S. coelicolor"]
mean_gc = [51, 38, 19, 72]

bins = np.arange(0, 101, 2)

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

for ax, mean in zip(axes.flat, mean_gc):
    gc = rng.normal(mean, 4, size=1000)
    ax.hist(gc, bins=bins)

fig.savefig("gc_histograms.png")
plt.show()

#3
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)
organisms = ["E. coli", "S. cerevisiae", "P. falciparum", "S. coelicolor"]
mean_gc = [51, 38, 19, 72]

bins = np.arange(0, 101, 2)

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

for ax, org, mean in zip(axes.flat, organisms, mean_gc):
    gc = rng.normal(mean, 4, size=1000)
    ax.hist(gc, bins=bins)
    ax.axvline(mean, linestyle="--")
    ax.set_title(f"{org} ({mean}%)")

fig.savefig("gc_histograms_annotated.png")
plt.show()

#4
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)
organisms = ["E. coli", "S. cerevisiae", "P. falciparum", "S. coelicolor"]
mean_gc = [51, 38, 19, 72]

bins = np.arange(0, 101, 2)

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

for ax, org, mean in zip(axes.flat, organisms, mean_gc):
    gc = rng.normal(mean, 4, size=1000)
    ax.hist(gc, bins=bins)
    ax.axvline(mean, linestyle="--")
    ax.set_title(f"{org} ({mean}%)")

fig.supxlabel("GC Content (%)")
fig.supylabel("Count")
fig.suptitle("Genome GC Content Distributions")

fig.savefig("gc_distribution_final.png")
plt.show()