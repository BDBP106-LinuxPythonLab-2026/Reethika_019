"""(2) Use the following data to
genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]
control = np.array([950, 1200, 310, 150, 420])
treated = np.array([940, 1180, 610, 75, 430])
1. Draw control and treated bars next to each other for each gene, with a legend.
2. Print the fold change (treated/control) for each gene, rounded to 2 decimals.
3. Which gene roughly doubled, and which halved?
(Hint: Use positions x=np.arange(len(genes)), draw control at x-width/2 and treated
at x+width/2 with width=0.4, then label the ticks with ax.set_xticks(x,labels=genes).
Your output should show: TP53 at 1.97 (doubled) and MYC at 0.5 (halved), GAPDH
and ACTB barely change, as expected for reference genes."""


#1
import numpy as np
import matplotlib.pyplot as plt

genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]
control = np.array([950, 1200, 310, 150, 420])
treated = np.array([940, 1180, 610, 75, 430])

x = np.arange(len(genes))
width = 0.4

fig, ax = plt.subplots()
ax.bar(x - width/2, control, width=width, label="Control", color="tab:blue")
ax.bar(x + width/2, treated, width=width, label="Treated", color="tab:orange")

ax.set_xticks(x)
ax.set_xticklabels(genes)
ax.set_xlabel("Genes")
ax.set_ylabel("Expression")
ax.set_title("Gene Expression: Control vs Treated")
ax.legend()

fig.savefig("gene_expression.png")
plt.show()

#2

import numpy as np

genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]
control = np.array([950, 1200, 310, 150, 420])
treated = np.array([940, 1180, 610, 75, 430])

fold_change = np.round(treated / control, 2)

for gene, fc in zip(genes, fold_change):
    print(f"{gene}: {fc}")


#3

import numpy as np

genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]
control = np.array([950, 1200, 310, 150, 420])
treated = np.array([940, 1180, 610, 75, 430])

fold_change = np.round(treated / control, 2)

for gene, fc in zip(genes, fold_change):
    if fc >= 1.8:
        print(f"{gene} roughly doubled ({fc})")
    elif fc <= 0.6:
        print(f"{gene} roughly halved ({fc})")