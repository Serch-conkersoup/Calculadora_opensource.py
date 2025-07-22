from funciones_calculadora import sumar_n_numeros, multiplicar_n_numeros, dividir_dos_numeros

while True:
    print ("""Bienvenido a mi calculadora, por favor, ingresa la opción que desees.
-----------------------------------------------------------------------------------

1) Hacer una suma de N números.
2) Hacer una multiplicación de N números.
3) Hacer una división de 2 números.

0) Salir del programa.
           
""")
    opcion = int(input("> "))
    if opcion == 0:
        break
    elif opcion == 1:
        resultado = sumar_n_numeros()
        print(f"El resultado de tu suma es: {resultado}")
    elif opcion == 2:
        resultado = multiplicar_n_numeros()
        print(f"El resultado de tu multiplicación es: {resultado}")
    elif opcion == 3:
        resultado = dividir_dos_numeros()
        print(f"El resultado de tu división es: {resultado}")
    else:
        print("Opción no válida. Por favor, elige una opción del 0 al 3.")
