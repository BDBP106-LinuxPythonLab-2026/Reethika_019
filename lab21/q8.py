"""Write a function protein_energy_temp() with an inner function
calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
random or user-input ∆H, ∆S and return stability (`stable’ if ∆G < 0)."""
import random


def protein_energy_temp(temperature_kelvin):

    def calculate_free_energy(enthalpy, entropy):
        delta_g = enthalpy - (temperature_kelvin * entropy)
        return delta_g


    simulated_enthalpy = random.uniform(0.0, 150.0)
    simulated_entropy = random.uniform(0.1, 0.5)
    dg = calculate_free_energy(simulated_enthalpy, simulated_entropy)


    if dg < 0:
        stability = "stable"
    else:
        stability = "unstable"
    print("Temperature: ", temperature_kelvin)
    print("Calculated delta_G: ", dg)
    return stability
protein_state = protein_energy_temp(298.15)
print("Protein State: ", protein_state)
