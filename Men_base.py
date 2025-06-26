def constanza():
    print("Mi nombre es constanza barra y tengo 19 años")


def tomas():
    print("Mi nombre es tomas tengo 19 años")


# Menú base del programa
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("4. Función de integrante 4")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        constanza()
    elif op == "2":
        pass # Aquí se llamará a la función del integrante 2
    elif op == "3":
        tomas()
    elif op == "4": 
        pass # Aquí se llamará a la función del integrante 4
    else:
        print(" Opción inválida.")  
