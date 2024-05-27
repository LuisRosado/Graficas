import numpy as np
import matplotlib.pyplot as plt

def polinomio(x):
    return x**5 - 3*x**4 + 2*x**3 - x**2 + 5*x - 7

def primera_derivada(x):
    return 5*x**4 - 12*x**3 + 6*x**2 - 2*x + 5

def segunda_derivada(x):
    return 20*x**3 - 36*x**2 + 12*x - 2

x = np.linspace(-2, 3, 400)  # Generar valores de x

plt.figure(figsize=(10, 6))

# Graficar el polinomio y sus derivadas
plt.plot(x, polinomio(x), label='Polinomio de 5 términos')
plt.plot(x, primera_derivada(x), label='Primera derivada')
plt.plot(x, segunda_derivada(x), label='Segunda derivada')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica del polinomio y sus derivadas')
plt.legend()
plt.grid(True)
plt.show()
