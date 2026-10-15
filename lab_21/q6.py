
"""(6) cell_metabolism with inner function"""
def cell_metabolism(glucose, oxygen):
    def energy_output():
        # 1 glucose + 6 oxygen -> 38 ATP
        possible = min(glucose, oxygen // 6)
        return possible * 38

    return energy_output()

print("Total ATP:", cell_metabolism(5, 24))