# Programa que solicita una contraseña hasta que el usuario la ingrese correctamente

CONTRASENA_CORRECTA = "secreta"

while True:
    contrasena = input("Ingrese la contraseña: ")
    if contrasena == CONTRASENA_CORRECTA:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Inténtelo de nuevo.")
