
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
sigma = 1  # Vous pouvez ajuster sigma ici
y = np.linspace(-2, 2, 500)

# Fonction exacte
f_exact = 0.5 * np.exp(-sigma * y**2)

# Approximation de Taylor
f_taylor = 0.5 - 0.5 * sigma * y**2

# Différence
difference = f_exact - f_taylor

# Tracés
plt.figure(figsize=(10, 6))

# Courbes
plt.plot(y, f_exact, label="Gaussienne exacte", linestyle='-', linewidth=2)
plt.plot(y, f_taylor, label="Approximation de Taylor", linestyle='--', linewidth=2)
plt.plot(y, difference, label="Différence (exacte - Taylor)", linestyle=':', linewidth=2)

# Configuration
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title("Gaussienne et approximation en série de Taylor")
plt.xlabel("y")
plt.ylabel("f(y)")
plt.legend()
plt.grid(True)
plt.show()
