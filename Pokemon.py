import pickle
import matplotlib.pyplot as plt

# Cargar los datos de los archivos pickle
with open('nombrePokemon.pickle', 'rb') as handle:
    nombres = pickle.load(handle)
with open('datosPokemon.pickle', 'rb') as handle:
    datos = pickle.load(handle)

# Seleccionar los primeros 30 Pokémon
nombres_30 = nombres[:30]
datos_30 = datos[:30]

# Extraer los datos relevantes para los ejes x e y
ataque = [dato[1] for dato in datos_30]  # Ataque
defensa = [dato[2] for dato in datos_30]  # Defensa

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.scatter(ataque, defensa, c='b', marker='o', label='Pokemones')

# Etiquetas y título
plt.xlabel('Ataque')
plt.ylabel('Defensa')
plt.title('Ataque vs Defensa de los primeros 30 Pokémon')
plt.legend()

# Anotar los nombres de los Pokémon
for i, nombre in enumerate(nombres_30):
    plt.annotate(nombre, (ataque[i], defensa[i]))

# Mostrar el gráfico
plt.grid(True)
plt.show()
