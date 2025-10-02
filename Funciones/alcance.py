def saludar():
    mensaje = "Hola Mundo"
    print(mensaje)

# Ejemplo de función con variable local que no puede ser accedida desde fuera en este caso la variable mensaje
def SaludaChanchito():
    mensaje = "Hola Chanchito Feliz"
    print(mensaje)

saludar()
SaludaChanchito()