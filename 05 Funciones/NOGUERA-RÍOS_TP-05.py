


#Actividad 1

def imprimir_hola_mundo(): #Definimos función que imprime saludo
    print("Hola Mundo!")

imprimir_hola_mundo() #Llamamos a la función desde el programa principal



#Actividad 2

def saludar_usuario(nombre): #Definimos la función que recibe un nombre y devuelve un saludo personalizado
    return f"Hola {nombre}!"

nombre_usuario = input("¿Cuál es tu nombre? ") #Solicitamos el nombre al usuario
saludo = saludar_usuario(nombre_usuario) #Llamamos a la función y mostramos el resultado
print(saludo)



#Actividad 3

def informacion_personal(nombre, apellido, edad, residencia): #Definimos función que imprime la información personal recibida como parámetros
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ") #Pedimos los datos al usuario
apellido = input("Ingrese su apellido: ")
residencia = input("Ingrese su lugar de residencia: ")

while True: # Validamos que la edad sea un número entero positivo
    try:
        edad = int(input("Ingrese su edad: "))
        if edad >= 0:
            break
        else:
            print("La edad no puede ser negativa.")
    except ValueError:
        print("Error. Ingrese un número entero.")

informacion_personal(nombre, apellido, edad, residencia) # Llamamos a la función con los datos ingresados



#Actividad 4

def calcular_area_circulo(radio): # Definimos función para calcular el área del círculo
    return 3.1416 * (radio ** 2)

def calcular_perimetro_circulo(radio): # Definimos función para calcular el perímetro del círculo
    return 2 * 3.1416 * radio


while True:
    radio = float(input("Ingrese el radio del círculo: ")) # Validación del ingreso del radio
    if radio > 0:
        break
    else:
        print("Error, ingrese un radio positivo: ")
    
area = calcular_area_circulo(radio) # Llamamos a las funciones y mostramos los resultados
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")



#Actividad 5

def segundos_a_horas(segundos): # Definimos función que convierte segundos a horas
    return segundos // 3600

while True: # Solicitamos los segundos al usuario con validación

    try:
        segundos = int(input("Ingrese cantidad de segundos: "))
        if segundos >= 0:
            break
        else:
            print("No se permiten valores negativos.")
    except ValueError:
        print("Error, ingrese un número entero.")

horas = segundos_a_horas(segundos) # Llamamos a la función y mostramos el resultado
print(f"{segundos} segundos equivalen a {horas} horas.")



#Actividad 6

def tabla_multiplicar(numero): # Definimos función que imprime la tabla de multiplicar del número ingresado
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

while True: # Pedimos el número al usuario con validación
    try:
        numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
        break
    except ValueError:
        print("Entrada inválida. Ingresá un número entero.")

tabla_multiplicar(numero) # Llamamos a la función


    
#Actividad 7

def operaciones_basicas(a, b): # Definimos función que devuelve suma, resta, multiplicación y división entre dos números
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

while True: # Solicitamos dos números al usuario con validación
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("Entrada inválida. Ingrese números válidos.")

suma, resta, multiplicacion, division = operaciones_basicas(a, b) # Llamamos a la función y mostramos los resultados

print("Resultados de las operaciones:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")



#Actividad 8

def calcular_imc(peso, altura): # Definimos función que calcula el índice de masa corporal
    return  peso / (altura **2)

while True: # Solicitar peso con validación
    try:
       peso = float(input("Ingrese peso en kilogramos: "))
       if peso > 0:
           break
       else:
           print("Ingrese un valor positivo.")
    except ValueError:
        print("Error. Ingrese números válidos.")

while True: # Solicitar altura con validación
    try:
       altura = float(input("Ingrese altura en metros: "))
       if altura > 0:
           break
       else:
           print("Ingrese un valor positivo.")
    except ValueError:
        print("Error. Ingrese números válidos.")

imc = calcular_imc(peso,altura) # Llamamos a la función y mostramos el resultado

print(f"Su índice de masa corporal es {imc:.2f} .")



#Actividad 9

def celsius_a_fahrenheit(celsius): # Definimos función que convierte grados Celsius a Fahrenheit
    return celsius * (9/5) + 32

while True: # Solicitamos temperatura con validación
    try:
        celsius = float(input("Ingrese grados Celsius: "))
        break
    except ValueError:
        print("Error, ingrese un número válido.")

fahrenheits = celsius_a_fahrenheit(celsius) # Llamamos a la función y mostramos el resultado

print(f"{celsius} °C equivalen a {fahrenheits} °F.")



#Actividad 10

def calcular_promedio(a, b, c): # Definimos función que calcula el promedio de tres números
    return (a+b+c)/3

def pedir_numero(mensaje): # Función para pedir números con validación
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error. Ingresá un número válido.")

a = pedir_numero("Ingrese el primer número: ") # Pedimos los tres números al usuario
b = pedir_numero("Ingrese el segundo número: ")
c = pedir_numero("Ingrese el tercer número: ")

promedio = calcular_promedio(a, b, c) # Calculamos el promedio y lo mostramos

print(f"El promedio de los tres valores es: {promedio}")