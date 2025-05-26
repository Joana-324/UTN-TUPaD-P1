

#Actividad 1

# Función recursiva para calcular el factorial de un número
def factorial(n):
    # Caso base: el factorial de 0 o 1 es igual a 1
    if n == 0 or n == 1:
        return 1
    else:
        # Caso recursivo: n! = n * (n-1)!
        return n * factorial(n - 1)

# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea mayor que cero
if numero < 1:
    print("Por favor, ingrese un número mayor o igual a 1.")
else:
    # Mostrar el factorial de todos los números desde 1 hasta el número ingresado
    for i in range(1, numero + 1):
        print(f"El factorial de {i} es {factorial(i)}")



#Actividad 2

# Función recursiva para obtener el valor de Fibonacci en una posición n
def fibonacci_recursivo(posicion):
    # Caso base: F(0) = 0 y F(1) = 1
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        # Caso recursivo: F(n) = F(n-1) + F(n-2)
        return fibonacci_recursivo(posicion-1) + fibonacci_recursivo(posicion-2)
    
# Solicitar al usuario la cantidad de elementos de la serie que desea ver
posicion = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

# Validar que sea una posición válida (0 o mayor)
if posicion < 0:
    print("Por favor, ingrese un número mayor o igual a 0.")
else:
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci_recursivo(i)}")



#Actividad 3

# Función recursiva para calcular la potencia de un número
def potencia(base, exponente):
    # Caso base: cualquier número elevado a la 0 es 1
    if exponente == 0:
        return 1
    else:
        # Caso recursivo: base^exponente = base * base^(exponente - 1)
        return base * potencia(base, exponente - 1)

# Solicitar al usuario los valores de base y exponente
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero positivo o 0): "))

# Validar que el exponente sea válido
if exponente < 0:
    print("Por favor, ingrese un exponente mayor o igual a 0.")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado}")



#Actividad 4

# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    # Caso base: si n es 0 o 1, se devuelve como cadena
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        # Caso recursivo: dividimos entre 2 y concatenamos el residuo
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar un número entero positivo al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"La representación binaria de {numero} es: {binario}")



#Actividad 5

# Función recursiva para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
        # Caso base: si la palabra tiene 0 o 1 letra, es palíndroma
    if len(palabra) <= 1:
        return True
    # Comparar la primera y última letra
    elif palabra[0] != palabra[-1]:
        return False
    else:
        # Llamada recursiva quitando la primera y última letra
        return es_palindromo(palabra[1:-1])

# Solicitar la palabra al usuario
texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

# Verificar si es un palíndromo
if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo.")
else:
    print(f"'{texto}' no es un palíndromo.")



#Actividad 6

# Función recursiva para sumar los dígitos de un número
def suma_digitos(n):
    # Caso base: si el número es menor a 10, es un solo dígito
    if n < 10:
        return n
    else:
        # Caso recursivo: sumar el último dígito y continuar con el resto
        return (n % 10) + suma_digitos(n // 10)

# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")



#Actividad 7

# Función recursiva para contar el total de bloques en la pirámide
def contar_bloques(n):
    # Caso base: si hay un solo nivel, se necesita un solo bloque
    if n == 1:
        return 1
    else:
        # Caso recursivo: bloques en este nivel + bloques en los niveles superiores
        return n + contar_bloques(n - 1)

# Solicitar al usuario la cantidad de bloques en el nivel más bajo
nivel_base = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))

# Validar que sea mayor o igual a 1
if nivel_base < 1:
    print("Debe ingresar un número entero mayor o igual a 1.")
else:
    total = contar_bloques(nivel_base)
    print(f"Se necesitan {total} bloques para construir la pirámide.")



#Avtividad 8

# Función recursiva para contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    # Caso base: si el número es 0, ya no hay más dígitos para contar
    if numero == 0:
        return 0
    else:
        # Tomamos el último dígito
        ultimo = numero % 10
        # Verificamos si coincide con el dígito buscado
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Solicitar al usuario el número y el dígito a buscar
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar (0-9): "))

# Validar que el número sea positivo y el dígito esté entre 0 y 9
if numero < 0 or digito < 0 or digito > 9:
    print("Entrada inválida. Asegúrese de que el número sea positivo y el dígito esté entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} vez/veces en el número {numero}.")