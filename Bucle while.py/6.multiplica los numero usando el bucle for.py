# Este programa imprime la tabla de multiplicar de un número dado por el usuario, desde el 1 hasta el 10, utilizando un bucle for.

num = int(input("Ingrese el numero a multiplicar: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")