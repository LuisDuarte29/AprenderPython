def hola(nombre="Defecto"): # Definición de la función Hola que recibe un parámetro nombre con valor por defecto "Defecto"
    print(f"Hola Mundo{nombre}")

hola("Pepe") # Llamada a la función Hola con el argumento "Pepe"

def muchosParametros(*numeros):
    for numero in numeros:
        print(numero)

muchosParametros(1,2,3,4,5,6,7,8,9) # Llamada a la función muchosParametros con múltiples argumentos

#keywords arguments
def muchosParametros2(**numeros):
    for clave, valor in numeros.items():
        print(f"{clave}: {valor}")

muchosParametros2(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9) # Llamada a la función muchosParametros2 con múltiples argumentos clave-valor
