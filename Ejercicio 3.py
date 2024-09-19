#3er ejercicio, programa para almacenar una contraseña
#Almacenar la contraseña en una variable (en este caso, "contraseña")
contraseña_guardada = "contraseña"

#Solicitar al usuario que ingrese la contraseña
contraseña_ingresada = input("Ingrese la contraseña: ")

#Comparar la contraseña ingresada con la guardada
if contraseña_ingresada == contraseña_guardada:
#Si las contraseñas coinciden, mostrar un mensaje.
    print("Contraseña correcta")
else:
#Si las contraseñas no coinciden, mostrar un mensaje de error.
    print("Contraseña incorrecta")
