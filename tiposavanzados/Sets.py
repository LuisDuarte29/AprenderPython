primer= {1,1,3,4,5} # Los sets no permiten elementos duplicados
print(primer) # Imprime {1, 3, 4, 5}
primer.add(2) # Agrega el elemento 2 al set primer
print(primer) # Imprime {1, 2, 3, 4, 5}
segundo= set([4,5,6,7,8]) # Crea un set segundo a partir de una lista
print(primer | segundo) # Unión de sets: {1, 2, 3, 4, 5, 6, 7, 8}  esto es igual a primer.union(segundo)
print(primer & segundo) # Intersección de sets: {4, 5} la interseccion es cuando hay elementos comunes esto es igual a primer.intersection(segundo)
print(primer - segundo) # Diferencia de sets: {1, 2, 3} es cuando hay elementos en el primer set que no están en el segundo esto es igual a primer.difference(segundo)
print(primer ^ segundo) # Diferencia simétrica de sets: {1, 2, 3, 6, 7, 8} es cuando hay elementos que están en un set o en otro pero no en ambos esto es igual a primer.symmetric_difference(segundo)