import numpy as np
import matplotlib.pyplot as plt

# Paramètres
sigma = 1  # Vous pouvez ajuster sigma ici
x_fixed = np.sqrt(np.log(2) / sigma)  # Fixer x à racine(ln(2) / sigma)
y = np.linspace(-2, 2, 500)  # Valeurs de y

# Fonction exacte
f_exact = 0.5 * np.exp(-sigma * y**2)

# Approximation de Taylor
f_taylor = 0.5 - 0.5 * sigma * y**2

# Graphique 1 : Fonction exacte et approximation de Taylor sur le même tracé
plt.figure(figsize=(10, 6))
plt.plot(y, f_exact, label="Gaussienne exacte", linestyle='-', linewidth=2)
plt.plot(y, f_taylor, label="Approximation de Taylor", linestyle='--', linewidth=2)
plt.title("Gaussienne et approximation de Taylor (x fixé à √(ln(2)/σ))")
plt.xlabel("y")
plt.ylabel("f(y)")
plt.legend()
plt.grid(True)
plt.show()