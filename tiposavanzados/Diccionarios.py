punto= {"x":1.1,"y":2.2} 
# Diccionario con claves x e y. Las claves son inmutables y string por defecto

print(punto["x"]) # Accede al valor asociado a la clave "x" que en este caso es 1.1s

punto["z"]=3.3 # Agrega una nueva clave "z" con el valor 3.3 al diccionario punto
# Accede al valor asociado a la clave "z" que en este caso es 3.3
print(punto.get("z", 99)) # Si la clave "z" no existe, devuelve 99 en lugar de generar un error

for clave, valor in punto.items(): # Itera s1obre las claves del diccionario punto
    print(f"Clave: {clave}, Valor: {valor}") # Imprime la clave y su valor asociado

usuarios=[{"nombre":"Juan","edad":25},{"nombre":"Ana","edad":30},{"nombre":"Luis","edad":20}]
for usuario in usuarios: # Itera sobre la lista de diccionarios usuarios
    print(f"Nombre: {usuario['nombre']}") # Imprime el nombre y la edad de cada usuario
