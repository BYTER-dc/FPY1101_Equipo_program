

def Datos_Jose():
    print("Mi nombre es Jose Tomas y tengo 19 años")
def datos_constanza():
    print("mi nombre es constanza y tengo 19 años")





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
        datos_constanza()
    elif op == "2":
        Datos_Jose()
    elif op == "3":
        pass # Aquí se llamará a la función del integrante 3
    elif op == "4":
        pass # Aquí se llamará a la función del integrante 3
    else:
        print(" Opción inválida.")  
