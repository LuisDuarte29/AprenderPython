numeros=(1,2,3,4,5) # Tupla de números
punto=tuple([1.1,2.2]) # Tupla de números flotantes creada a partir de una lista
print(punto)
#otra diferencia con las listas es que las tuplas no se pueden modificar
primero, segundo, *otros=numeros # Desempaqueta la tupla numeros en las variables primero, segundo y el resto en la lista otros
print(segundo)