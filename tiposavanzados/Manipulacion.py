mascotas=["perro","gato","pez"]
mascotas.append("loro") # Agrega "loro" al final de la lista mascotas
mascotas.insert(1,"hamster") # Inserta "hamster" en la posición 1 de la lista mascotas
mascotas.remove("gato") # Elimina "gato" de la lista mascotas
print(mascotas[0:3]) # Imprime los primeros tres elementos de la lista mascotas

numeros=[1,2,3,4,5,6,7,8,9,10]
pares=list(filter(lambda x: x%2==0, numeros)) # Filtra los números pares de la lista numeros
print(numeros[1::2])

perro, gato, pez= mascotas # Desempaqueta la lista mascotas en las variables perro, gato y pez
print(perro)

perro, *otros= mascotas # Desempaqueta la lista mascotas en la variable perro y el resto en la lista otros