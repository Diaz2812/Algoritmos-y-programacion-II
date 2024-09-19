#6to ejercicio, descuento de zapatos

precio_zapato = 80

#Solicitar al usuario el número de zapatos que comprara
cantidad_zapatos = int(input("Ingrese el número de zapatos comprados: "))
#Calcular el total sin descuento
total_sin_descuento = cantidad_zapatos * precio_zapato
#Inicializar el descuento
descuento = 0
#Determinar el descuento según la cantidad de zapatos
if cantidad_zapatos >=30:
    descuento = 0.40  
elif cantidad_zapatos > 20:
    descuento = 0.20  
elif cantidad_zapatos > 10:
    descuento = 0.10  
#Calcular el total con descuento
total_con_descuento = total_sin_descuento * (1 - descuento)
#Mostrar el total a pagar
print(f"El total a pagar es: ${total_con_descuento:}")
