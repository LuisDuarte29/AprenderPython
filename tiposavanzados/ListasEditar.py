usuarios=[["Juan",25],["Ana",30],["Luis",20]]

nombres=[]
#este seria filter pero en vez de usar una función lambda usamos una comprensión de listas
nombres=[usuario for usuario in usuarios] # Crea una nueva lista nombres con los primeros elementos de cada sublista en usuarios
nombresMap = list(map(lambda usuario:usuario[0],usuarios)) # Crea una nueva lista nombres con los primeros elementos de cada sublista en usuarios
#este seria filter pero en vez de usar una función lambda usamos una comprensión de listas
nombres=[usuario for usuario in usuarios if usuario[1]>21] # Crea una nueva lista nombres con los primeros elementos de cada sublista en usuarios
#este seria filter usando una función lambda
nombresFilter=list(filter(lambda usuario:usuario[1]>21,usuarios)) # Crea una nueva lista nombres con los primeros elementos de cada sublista en usuarios
print(nombresFilter)
print(nombresMap)
