

def suma_avanzada():
    numeros = input("Ingresa los números separados por espacio: ").split()
    try:
        numeros = [float(num) for num in numeros]
        return sum(numeros)
    except ValueError:
        print("Error: Asegúrate de ingresar solo números.")
        return None
