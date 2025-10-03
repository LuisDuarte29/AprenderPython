mascotas=["perro","gato","pez"]

#enumrate sirve para obtener el índice y el valor al mismo tiempo
for indice, mascota in enumerate(mascotas): # Itera sobre la lista mascotas con índice
    print(f"Índice: {indice}, Mascota: {mascota}") # Imprime el índice y la mascota