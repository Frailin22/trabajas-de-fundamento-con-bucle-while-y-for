# Este programa pide al usuario un número entero y luego imprime todos los números desde ese número hasta el 0 en orden descendente utilizando el bucle while

num = int(input("Ingrese un numero entero: "))
while num >= 0:
    print(num)
    num -= 1