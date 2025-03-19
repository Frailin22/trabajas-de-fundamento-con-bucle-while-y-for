#Este programa para calcular el factorial de un número usando un bucle while

def calcular_factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

# Solicitar al usuario un número
numero = int(input("Ingrese un número para calcular su factorial: "))

# Validar que el número sea no negativo
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    print(f"El factorial de {numero} es {calcular_factorial(numero)}")
