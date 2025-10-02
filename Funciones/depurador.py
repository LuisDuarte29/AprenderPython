def largo(texto):
    resultado=0
    for _ in texto: # Usamos _ porque no necesitamos el valor del elemento
        resultado+=1
    return resultado

L=largo("Hola Mundo")
print(L)