def sumar_n_numeros():
    numeros_a_sumar = int(input("¿Cuántos números quieres sumar? ")) 

    lista_numeros = []
    for numero in range(numeros_a_sumar):
        numero_a_sumar = float(input(f"Ingresa el número {numero + 1} a sumar: "))
        lista_numeros.append(numero_a_sumar)

    return sum(lista_numeros)

def multiplicar_n_numeros():
    numeros_a_multiplicar = int(input("¿Cuántos números quieres multiplicar? "))

    resultado = 1
    for numero in range(numeros_a_multiplicar):
        numero_a_multiplicar = float(input(f"Ingresa el número {numero + 1} a multiplicar: "))
        resultado *= numero_a_multiplicar

    return resultado

def dividir_dos_numeros():
    dividendo = float(input("Ingresa el dividendo: "))
    divisor = float(input("Ingresa el divisor: "))

    if divisor == 0:
        return "Error: No se puede dividir entre cero."
    
    return dividendo / divisor

