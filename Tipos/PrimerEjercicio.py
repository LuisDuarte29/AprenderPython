
numero1=""
while True:
    if numero1=="":
        numero1=input("Dime un número: ")
        if numero1.lower()=="salir":
            print("Saliendo...")
            break

    numero2=input("Dime otro número: ")
    if numero2.lower()=="salir":
        print("Saliendo...")
        break
    Operacion=input("Dime la operación a realizar (suma, resta, multiplicación, división): ")
    if Operacion.lower()=="salir":
        print("Saliendo...")
        break
    if numero1!=0 and numero2!=0:
        numero1=int(numero1)
        numero2=int(numero2)
    if Operacion=="suma":
        print(f"El resultado de la suma es {numero1+numero2}")
        numero1=numero1+numero2
    elif Operacion=="resta":
        print(f"El resultado de la resta es {numero1-numero2}")
        numero1=numero1-numero2
    elif Operacion=="multiplicacion":
        print(f"El resultado de la multiplicación es {numero1*numero2}")
        numero1=numero1*numero2
    elif Operacion=="division":
        if numero2!=0:
            print(f"El resultado de la división es {numero1/numero2}")
            numero1=numero1/numero2
        else:
            print("No se puede dividir entre 0")
    else:
        print("Operación no válida")
