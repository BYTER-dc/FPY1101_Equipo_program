def constanza():
    print("Mi nombre es Constanza barra y tengo 19 años")
def jose():
    print("Mi nombre es Jose hernandez y tengo 19 años")
def valentina():
    print("Mi nombre es Valentina lobos y tengo 19 años")
def etaniel():
    print("Mi nombre es Etániel rapu y tengo 19 años")
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
        jose()
    elif op == "3":
        valentina()
    elif op == "4": 
        etaniel()
    else:
        print(" Opción inválida.")  
