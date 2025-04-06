#Trabajo Práctico n°3
#Estudiante: Joana Noguera Ríos.

#Actividad 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Usted es mayor de edad.")

#Actividad 2
Nota = float(input("ingrese su nota: "))
if Nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#Actividad 3
numero = int(input("Ingrese un número par: "))
while numero % 2 != 0:
    print("Por favor, ingrese un número par.")
    numero = int(input("Ingrese un número par: "))
print("Ha ingresado un número par.")

#Actividad 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a.")
elif 12<= edad < 18:
    print("Adolescente.")
elif 18<= edad <30:
    print("Adulto/a joven.")
else:
    print("Adulto.")

#Actividad 5
while True:
    contraseña = input("Ingrese contraseña (de 8 a 14 caracteres): ")
    if len(contraseña) >= 8 and len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta.")
        break
    else:
        print("Por favor, intente nuevamente.")

#Actividad 6
import random
import statistics

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)

try:
    moda = statistics.mode(numeros_aleatorios)
except statistics.StatisticsError:
    moda = None

print("Lista de números aleatorios:")
numeros_aleatorios.sort()
print(numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if moda is not None:
    if media > mediana > moda:
        print("Sesgo POSITIVO.")
    elif media < mediana < moda:
        print("Sesgo NEGATIVO.")
    elif media == mediana == moda:
        print("SIN SESGO.")
    else:
        print("No hay un sesgo claro según los valores obtenidos.")
else:
    print("No se puede determinar el sesgo porque no hay una única moda.")

#Actividad 7
frase = input("Ingrese una frase o palabra: ")

# Verificamos si termina en vocal (minúscula o mayúscula)
if frase[-1].lower() in "aeiou":
    frase += "!"
    
print(frase)

#Actividad 8
nombre = input("Ingrese su nombre: ")
print("¿Cómo desea ver su nombre?")
print("1: En mayúsculas.")
print("2: En minúsculas.")
print("3: Con la primera letra en mayúscula.")

opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida. Debe ingresar 1, 2 o 3.")

#Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto según la escala de Richter: "))

if magnitud < 3:
    print("Muy leve.")
elif 3 <= magnitud < 4:
    print("Leve.")
elif 4 <= magnitud < 5:
    print("Moderado.")
elif 5 <= magnitud < 6:
    print("Fuerte.")
elif 6 <= magnitud < 7:
    print("Muy Fuerte.")
elif magnitud >= 7:
    print("Extremo.")
else:
    print("Valor inválido.")

#Actividad 
hemisferio = input("¿En qué hemisferio te encontrás? (N/S): ").strip().upper()
mes = int(input("¿En qué mes del año? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

estacion = ""

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"

if estacion:
    print(f"Estás en {estacion}.")