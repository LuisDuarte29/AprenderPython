BUSCAR=10
for numero in range(5):
    if numero==BUSCAR:
        print(f"He encontrado el número {BUSCAR}")
        break
else:
    print("No he encontrado el número")