# Este programa pide un número entero positivo luego imprima todos los números impares del 1 hasta el número ingresado con el bucle while

num = int(input("Escriba un numero entero positivo: "))
if num > 0:
    i = 1 + 1
    while i <= num:
        print(i)
        i += 2
    
else:
    print("por favor ingrese un numero positivo: ")
