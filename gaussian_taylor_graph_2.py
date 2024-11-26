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

# Différence entre les deux
difference = f_exact - f_taylor

# Graphique 2 : Différence entre la fonction exacte et l'approximation de Taylor
plt.figure(figsize=(10, 6))
plt.plot(y, difference, label="Différence (exacte - Taylor)", linestyle=':', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title("Différence entre la fonction exacte et l'approximation de Taylor")
plt.xlabel("y")
plt.ylabel("Différence")
plt.legend()
plt.grid(True)
plt.show()