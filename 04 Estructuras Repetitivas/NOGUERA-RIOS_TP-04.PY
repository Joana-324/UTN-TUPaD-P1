#Trabajo Práctico n°4
#Estudiando: Joana Noguera Ríos


#Actividad 1
#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

cont = 0             # Inicializamos el contador en 0.
while cont <= 100:   # Iniciamos un bucle que se repite mientras el valor de 'cont' sea menor a 100.
    print(cont)      # Mostramos el valor actual de 'cont' en pantalla.
    cont = cont +1   # Aumentamos el valor de 'cont' en 1 en cada iteración.


print("Actividad 2.")
#Actividad 2
#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingrese un número entero: "))           #Pedimos al usuario que ingrese un número entero.
cantidad_digitos= len(str(num))                          #Contamos cantidad de dígitos en el número.
print("La cantidad de dígitos es: ", cantidad_digitos)   #Se muesta el resultado por pantalla.

#Actividad 3 
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores. 

num1 = int(input("Ingrese el primer número: "))                   #Solicitamos los dos valores al usuario.
num2 = int(input("Ingrese el segundo número: "))

menor = min(num1, num2)                                           #Aseguramos que el rango vaya de menor a mayor.
mayor = max(num1, num2)

total = 0                                                         #Inicializamos la variable para acumular la suma

for i  in range(menor, mayor +1):                                  # Sumamos todos los números entre num1 y num2 (inclusive)
    total += i
print("La sumatoria de los números comprendidos entre", menor, "y", mayor , "es: ", total)    #Mostramos el resultado final en pantalla. 

#Actividad 4
#) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

total = 0                                        # Inicializamos la variable para acumular la suma
num = int(input("Ingrese un número o 0 para finalizar: "))          # Pedimos al usuario que ingrese un número entero

while num != 0:                                  # Inicializamos un bucle que acumulara las sumas, mientras el valor ingresado no sea 0.
    total += num 
    print(total)                                 # Mostrará el total de las sumas en pantalla.
    num = int(input("Ingrese otro número: "))    # Pedimos al usuario que agregue valores para seguir sumando.

#Actividad 5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
aleatorio = random.randint(0, 9)                        #Generamos un número aleatorio entre 0 y 9

intentos= 0                                             #Inicializamos el contador de intentos
while True:
    num = int(input("Avidina el número entre 0 y 9: ")) #Creamos el bucle hasta que el usuario adivine el número.
    intentos += 1                                       #Comenzamos a sumar los intentos.

    if num == aleatorio:
        print("¡Adivinaste!, lo lograste en ", intentos, "intentos.")
        break                                           #Salimos del bucle.
    else:
        print("Inténtalo nuevamente: ")


#Actividad 6
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

cont = 98            #Inicializamos el contador en 98
while cont > 0:      #Iniciamos un bucle que se repite mientras el valor de 'cont' sea mayor a 0.
    print(cont)      # Mostramos el valor actual de 'cont' en pantalla.
    cont = cont -2  

#Actividad 7
#) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

total = 0                                                            #Inicializamos la variable para acumular la suma.
num = int(input("Ingrese un número: "))                              #Solicitamos al usuario que ingrese un número.

for i in range(0, num + 1):                                          #Sumamos todos los números entre 0 y el valor del usuario.
     total += i 
print("La sumatoria de los números entre 0 y", num, "es: ", total )  #Se muestra en pantalla el resultado total.

#Actividad 8
#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

CANTIDAD = 100                  #Cantidad de número que se deben ingresar
 
pares = 0                       # Inicialización de contadores
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD):       # Ingreso de los números
    num = int(input(f"Ingrese número: "))

    if num % 2 == 0:            #Si es par o impar
        pares += 1
    else:
        impares += 1

    if num > 0:                 # Si es positivo o negativo
        positivos += 1
    elif num < 0:
        negativos += 1
                                # Se muestra en pantalla
print("Cantidad de números pares: ", pares)
print("Cantidad de números impares: ", impares)
print("Cantidad de números positivos: ", positivos)
print("Cantidad de números negativos: ", negativos)

#Actividad 9
#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

CANTIDAD = 100                          #Cantidad de número que se deben ingresar
sumatoria = 0

for cont in range(1, CANTIDAD+1):       # Ingreso de los valores
    print("Ingrese número entero: ")
    num = int(input())
    sumatoria = sumatoria + num
media = sumatoria / 100                 # Calculamos la media

print("La media de los valores ingresados es de: ", media)

#Actividad 9
#) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese número entero positivo: "))

numero = int(str(numero)[::-1])
print(numero)