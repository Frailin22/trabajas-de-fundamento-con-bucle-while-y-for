# Este programa pida al usuario un número entero positivo. El programa debe contar cuántos dígitos tiene el número utilizando un bucle while

num = int(input("Digite un numero enter positivo: "))
if num <= 0:
    print("El numero debe ser positivo")
else:
    contador = 0

    while num > 0:
        num //= 10
        contador += 1
        print(f"El numero tiene {contador} dígitos")
