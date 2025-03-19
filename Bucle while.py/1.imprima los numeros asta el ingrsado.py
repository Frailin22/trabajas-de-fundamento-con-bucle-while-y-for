# Este programa pide al usuario ingresar un número entero positivo y muestra todos los números del 1 hasta el número ingresado.

num = int(input("Digite un numero entero posiotivo \n"))

if num < 0:
    print("El numero ingrsado no es positivo.")
    exit()
else: 
    # inicializar la variable en 1
    i = 1
    while i <= num:
        print(1)
        i += 1
