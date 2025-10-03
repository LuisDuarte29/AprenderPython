mascotas=["perro","gato","pez"]
numeros=[2,9,5,1,7,6,3,8,4]
usuarios=[["Juan",25],["Ana",30],["Luis",20]]
def ordenar(elemento):
    return elemento[1] # Retorna el segundo elemento (edad) para usarlo como clave de ordenamiento
usuarios.sort(key=ordenar) # Ordena la lista usuarios por la edad (segundo elemento de cada sublista)

usuarios.sort(key=lambda elemento: elemento[1]) # Ordena la lista usuarios por la edad usando una función lambda




numeros.sort() # Ordena la lista numeros de menor a mayor
numeros.sort(reverse=True) # Ordena la lista numeros de mayor a menor
numero2s=sorted(numeros) # Crea una nueva lista numeros2 con los elementos de numeros ordenados de menor a mayor

mascotas.insert(1,"hamster") # Inserta "hamster" en la posición 1 de la lista mascotas
mascotas.append("loro") # Agrega "loro" al final de la lista mascotas
mascotas.remove("gato") # Elimina "gato" de la lista mascotas
mascotas.pop() # Elimina el último elemento de la lista mascotas
del mascotas[0] # Elimina el elemento en la posición 0 de la lista mascotas
mascotas.clear() # Elimina todos los elementos de la lista mascotas

print(mascotas.count("gato")) # Cuenta cuántas veces aparece "gato" en la lista mascotass
if "gato" in mascotas: # Verifica si "gato" está en la lista mascotas
    print(mascotas.index("gato")) # Imprime el índice de "gato" en la lista mascotas