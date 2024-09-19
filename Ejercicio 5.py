#5to ejercicio, programa para evaluar el rendimiento de empleados en Corpoelec

#Definir la puntuación máxima y el salario base
salario_base = 2400

#Solicitar al usuario que ingrese su puntuación
puntuacion = float(input("Ingrese su puntuación (0.0, 0.4, 0.6 o más): "))

#Inicializar variables para el nivel de rendimiento y el salario
nivel_rendimiento = ""
salario = 0

#Evaluar la puntuación y determinar el nivel de rendimiento y el salario
if puntuacion < 0.4:
    nivel_rendimiento = "bajo"
    salario = 0  #No recibe salario si tiene bajo rendimiento
elif 0.4 <= puntuacion < 0.6:
    nivel_rendimiento = "medio"
    salario = salario_base * puntuacion  #Salario para puntuación media
else:  #puntuacion >= 0.6
    nivel_rendimiento = "alto"
    salario = salario_base * puntuacion  #Salario para puntuación alta

#Mostrar el resultado al usuario
print(f"Nivel de rendimiento: {nivel_rendimiento}")
print(f"Cantidad de dinero que recibirá: {salario} €")
