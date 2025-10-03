"""
Enunciados de ejercicios - nivel básico

Cada sección agrupa ejercicios relacionados con los archivos en tu repositorio.
Copia cada enunciado a su archivo correspondiente y resuélvelo ahí.
"""

# 1) Tipos y conversiones (Numeros, Conversion, Caracteres)
# A. Escribe una función `suma_prod_div(a, b)` que devuelva una tupla (suma, producto, división)
#    - Si la división no es posible (división por cero), devuelve None en lugar del resultado de la división.

def suma_prod_div(a, b):
    suma=a+b
    prod=a*b
    div=None
    if b!=0 or a!=0:
        div=a/b
    return (suma,prod,div)
# B. Escribe `to_int_safe(s, default=None)` que convierte una cadena a int o devuelve `default` si falla.
def to_int_safe(s, default=None):
    if s.isdigit():
        return int(s)
    else:
        return default
resto=to_int_safe("ho")
print(resto)
# 2) Entrada/salida y primer programa (PrimerEjercicio)
# A. Programa que pida nombre y edad y devuelva el año en que la persona cumplirá 100 años.
def anio_cumple_100(nombre, edad, anio_actual):
    aniocumpla100=anio_actual+(100-edad)
    print(f"{nombre} cumplira 100 años en el año {aniocumpla100}")
anio_cumple_100("Ana",26,2025)

# 3) Control de flujo (ifElse, for, while)
# A. `clasificar_numero(n)` que devuelva 'positivo', 'negativo' o 'cero'.
def clasificar_numero(n):
    if n>0:
        return "positivo"
    elif n<0:
        return "negativo"
    else:
        return "cero"
# B. `primeros_n_pares_for(n)` y `primeros_n_pares_while(n)` que devuelvan una lista con los primeros n números pares.
def primeros_n_pares_for(n):
    for i in n:
        if i!=0:
            if i%2==0:
                print(i)
primeros_n_pares_for(range(10))

def  primeros_pares_forLista(n):
    res=[]
    for i in range(n):
        if i%2==0:
            res.append(i)
    return res
print(primeros_pares_forLista(10))
# 4) Funciones y alcance (funcionesNormal, alcance, return)
# A. Implementa `factorial_iter(n)` y `factorial_rec(n)` (iterativo y recursivo).

# B. Explica con código la diferencia entre variable local y global.

# 5) Depuración (depurador)
# A. Crea una función con un bug simple y escribe su versión corregida (p. ej. filtrar positivos)
# 6) Listas y manipulación (Listas, ListasEditar, IterarListas, Manipulacion)
# A. `añadir_elemento(lst, el)`, `eliminar_por_indice(lst, idx)`, `buscar_elemento(lst, el)` (devuelve índice o -1).

def anadir_elemento(lst,el):
    lst.append(el)
    return lst
print(anadir_elemento([1,2,3],"Hola"))

def eliminar_por_indice(lst,idx):
    lst.remove(idx)
    return lst
print(eliminar_por_indice([1,2,3,4,5],2))

def buscar_elemento(lst,el):
    if el in lst:
        return lst[3]
    else:
        return None
print(buscar_elemento([1,2,3,4,5],3))



# B. `invertir_sin_reverse(lst)` devuelve una copia invertida sin usar .reverse().
def invertir_sin_reverse(lst):
    return lst[::-1]
print(invertir_sin_reverse([1,2,3,4,5]))


# 7) Tuplas y Sets (Tuplas, Sets)
# A. `combina_tuplas(t1, t2)` que devuelva la tupla combinada.
def combina_tuplas(t1,t2):
    return t1+t2
print(combina_tuplas((1,2,3),(4,5,6)))
# B. `quitar_duplicados_preservando_orden(lista)` usando `set()` internamente.
def quitar_duplicados_presenvandoOrden(lista1):
    listaSet=set(lista1)
    return listaSet
print(quitar_duplicados_presenvandoOrden([1,1,2,3,4]))

# 8) Diccionarios (Diccionarios, editarElementos)
# A. Mini agenda: `add_contact(agenda, nombre, telefono)`, `buscar_contacto(agenda, nombre)`,
#    `editar_contacto(agenda, nombre, nuevo_telefono)`, `eliminar_contacto(agenda, nombre)`.
# 10) Ejercicio integrador
# A. Guarda y carga una agenda (diccionario) en disco usando JSON: `guardar_agenda(agenda, ruta)` y `cargar_agenda(ruta)`.

# Opcional: para cada ejercicio añade ejemplos de uso en comentarios.
