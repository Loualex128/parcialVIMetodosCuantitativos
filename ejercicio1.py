import numpy as np
from scipy.optimize import minimize

# Definimos la función objetivo (a minimizar)
def objective(x):
    return -(0.1*x[0] + 0.08*x[1])

# Definimos las restricciones
def constraint1(x):
    return x[0] + x[1] - 1

def constraint2(x):
    return 0.02*x[0]**2 + 0.03*x[1]**2 - 0.05

# Definimos los límites de las variables (opcional, si se conocen)
bounds = ((0, None), (0, None))  # x e y deben ser no negativos

# Creamos las restricciones
con1 = {'type': 'eq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
cons = [con1, con2]

# Establecemos un punto inicial (opcional)
x0 = np.array([0.5, 0.5])

# Resolvemos el problema
sol = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=cons)

# Imprimimos la solución
print("Valores óptimos: x =", sol.x[0], ", y =", sol.x[1])
print("Valor máximo de la función objetivo:", -sol.fun)