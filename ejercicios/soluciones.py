# Soluciones para los ejercicios - nivel básico

from datetime import datetime
import json

def suma_prod_div(a, b):
    """Devuelve (suma, producto, division_or_None)."""
    suma = a + b
    prod = a * b
    div = None
    if b != 0:
        div = a / b
    return suma, prod, div

def to_int_safe(s, default=None):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default


def año_cumple_100(nombre, edad):
    try:
        edad = int(edad)
    except (ValueError, TypeError):
        return "Edad inválida"
    año_actual = datetime.now().year
    año_100 = año_actual + (100 - edad)
    return f"{nombre} cumplirá 100 años en {año_100}"


def clasificar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

def primeros_n_pares_for(n):
    res = []
    for i in range(n):
        res.append(2 * i)
    return res

def primeros_n_pares_while(n):
    res = []
    i = 0
    while len(res) < n:
        res.append(2 * i)
        i += 1
    return res


def factorial_iter(n):
    if n < 0:
        raise ValueError("n debe ser >= 0")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def factorial_rec(n):
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n in (0, 1):
        return 1
    return n * factorial_rec(n - 1)

x = 10

def ejemplo_alcance():
    x = 5
    return x


def filtrar_positivos_corregido(lista):
    res = []
    for x in lista:
        if x > 0:
            res.append(x)
    return res


def añadir_elemento(lst, el):
    lst.append(el)
    return lst

def eliminar_por_indice(lst, idx):
    try:
        lst.pop(idx)
    except IndexError:
        pass
    return lst

def buscar_elemento(lst, el):
    try:
        return lst.index(el)
    except ValueError:
        return -1

def invertir_sin_reverse(lst):
    return [lst[i] for i in range(len(lst) - 1, -1, -1)]


def combina_tuplas(t1, t2):
    return t1 + t2

def quitar_duplicados_preservando_orden(lista):
    vistos = set()
    res = []
    for x in lista:
        if x not in vistos:
            vistos.add(x)
            res.append(x)
    return res


def add_contact(agenda, nombre, telefono):
    agenda[nombre] = telefono
    return agenda

def buscar_contacto(agenda, nombre):
    return agenda.get(nombre)

def editar_contacto(agenda, nombre, nuevo_telefono):
    if nombre in agenda:
        agenda[nombre] = nuevo_telefono
        return True
    return False

def eliminar_contacto(agenda, nombre):
    return agenda.pop(nombre, None) is not None


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b


def guardar_agenda(agenda, ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(agenda, f, ensure_ascii=False, indent=2)

def cargar_agenda(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


if __name__ == "__main__":
    print("Pruebas rápidas:")
    print('suma_prod_div(6,3)=', suma_prod_div(6, 3))
    print('to_int_safe("abc", 0)=', to_int_safe("abc", 0))
    print(año_cumple_100("Ana", 30))
    print('clasificar_numero(-5)=', clasificar_numero(-5))
    print('primeros_n_pares_for(5)=', primeros_n_pares_for(5))
    print('factorial_iter(5)=', factorial_iter(5))
    print('filtrar_positivos_corregido([1,-2,3])=', filtrar_positivos_corregido([1, -2, 3]))
