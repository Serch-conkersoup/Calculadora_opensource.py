

from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_av import suma_avanzada

while True:
    print("""
Bienvenido a la Calculadora
-----------------------------------------
Selecciona una opción:
1) Sumar 2 números
2) Restar 2 números
3) Multiplicar 2 números
4) Dividir 2 números
5) Sumar N números
0) Salir
""")

    opcion = input("> ")

    if opcion == "0":
        print("¡Hasta luego!")
        break

    elif opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"Resultado: {sumar(a, b)}")

    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"Resultado: {restar(a, b)}")

    elif opcion == "3":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"Resultado: {multiplicar(a, b)}")

    elif opcion == "4":
        a = float(input("Ingresa el dividendo: "))
        b = float(input("Ingresa el divisor: "))
        try:
            print(f"Resultado: {dividir(a, b)}")
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == "5":
        resultado = suma_avanzada()
        if resultado is not None:
            print(f"Resultado: {resultado}")

    else:
        print("Opción no válida. Intenta de nuevo.")
