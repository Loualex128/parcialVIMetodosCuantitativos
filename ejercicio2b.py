import matplotlib.pyplot as plt
import numpy as np

# Fijamos z = 50 (por ejemplo)
z_fixed = 50

# Creamos una malla de valores para x e y
x = np.linspace(0, 100-z_fixed, 100)
y = np.linspace(0, 100-z_fixed, 100)
X, Y = np.meshgrid(x, y)

# Calculamos los valores de la función de costos
Z = 5*X**2 + 3*Y**2 + z_fixed**2

# Creamos el gráfico de contorno
plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar()
plt.xlabel('Cantidad de producto A')
plt.ylabel('Cantidad de producto B')
plt.title('Costo para z = 50')
plt.show()