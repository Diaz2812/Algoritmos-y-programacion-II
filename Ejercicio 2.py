#2do ejercicio, para calcular el area de un rectangulo
#Solicitar la base y la altura del rectángulo al usuario
base = float(input("Ingrese la base del rectángulo:"))
altura = float(input("Ingrese la altura del rectángulo:"))

#Calcular el área del rectángulo
area = base * altura

#Mostrar el área calculada
print(f"El área del rectángulo es: {area:}")

#Verificar si el área es mayor a 40 y la altura es mayor a 10
if area > 40:
    if altura > 10:
        #Mostrar mensaje de que si se cumplen las condiciones
        print("El área del rectángulo es mayor a 40 y la altura es mayor a 10")
    else:
        #Mostrar mensaje si solo el área cumple la condición
        print("El área del rectángulo es mayor a 40, pero la altura no es mayor a 10")
else:
    if altura > 10:
        #Mostrar mensaje si solo la altura cumple la condición
        print("La altura del rectángulo es mayor a 10, pero el área no es mayor a 40")
    else:
        #Mostrar mensaje si ninguna condición se cumple
        print("El área del rectángulo no cumple las condiciones")
