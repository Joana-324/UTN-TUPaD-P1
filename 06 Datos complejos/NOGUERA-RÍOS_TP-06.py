#Datos Complejos
#Estudiante: Joana Noguera Ríos


#Actividad 1
# Diccionario original con frutas y precios
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agrego frutas nuevas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Muestro resultado
print(precios_frutas)
print()


#Actividad 2
# Diccionario modificado del punto anterior
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualizo precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Muestro resultado actualizado
print(precios_frutas)
print()


#Actividad 3
# Diccionario actualizado
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Obtener solo las frutas (claves del diccionario)
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista de frutas
print(lista_frutas)
print()


#Actividad 4
# Crear un diccionario vacío
agenda = {}

# Cargar 5 contactos
for i in range(5):
    nombre_original = input(f"Ingrese nombre del contacto {i+1}: ")
    numero = input(f"Ingrese número de {nombre_original}: ")
    nombre = nombre_original.lower()  # Convertimos a minúsculas
    agenda[nombre] = numero

# Consultar un contacto
consulta_original = input("Ingrese nombre de contacto para obtener número: ")
consulta = consulta_original.lower()

# Verificar si existe
if consulta in agenda:
    print(f"El número de {consulta_original} es: {agenda[consulta]}")
else:
    print(f"No se encontró el contacto '{consulta_original}'.")

print()


#Actividad 5
import string  # Para acceder a los signos de puntuación

# Solicitar frase al usuario
frase = input("Ingresá una frase: ")

# Pasar todo a minúsculas
frase = frase.lower()

# Eliminar signos de puntuación
for signo in string.punctuation:
    frase = frase.replace(signo, "")

# Separar la frase en palabras
palabras = frase.split()

# Crear un set para palabras únicas
palabras_unicas = set(palabras)

# Crear un diccionario para contar las veces que aparece cada palabra
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Mostrar resultados
print("\nPalabras únicas:")
print(palabras_unicas)

print("\nCantidad de veces que aparece cada palabra:")
for palabra, cantidad in contador_palabras.items():
    print(f"{palabra}: {cantidad}")

print()


#Actividad 6
# Diccionario para guardar las notas de cada alumno
alumnos = {}

# Ingresar datos
for i in range(3):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    
    # Ingresar 3 notas separadas por espacios y convertirlas a enteros
    notas_str = input(f"Ingresá 3 notas de {nombre}, separadas por espacios: ")
    notas = tuple(map(int, notas_str.split()))
    
    # Guardar en el diccionario
    alumnos[nombre] = notas

# Mostrar promedio de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

print()


#Actividad 7
# Estudiantes que aprobaron Parcial 1
parcial1 = {"Ana", "Luis", "Marta", "Carlos", "Sofía"}

# Estudiantes que aprobaron Parcial 2
parcial2 = {"Carlos", "Sofía", "Elena", "Julián"}

# Aprobados en ambos parciales
ambos = parcial1 & parcial2

# Aprobados en solo uno de los dos
solo_uno = parcial1 ^ parcial2

# Aprobados en al menos uno (unión)
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("Estudiantes que aprobaron ambos parciales:", ambos)
print("Estudiantes que aprobaron solo uno de los dos:", solo_uno)
print("Estudiantes que aprobaron al menos uno:", al_menos_uno)
print()


#Actividad 8
# Inventario inicial
stock = {
    "manzanas": 8,
    "bananas": 9,
    "naranjas": 5
}

# Mostrar inventario inicial
print("Inventario inicial:", stock)

# Consultar un producto
producto = input("\nIngresá el nombre de un producto: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = input("¿Querés agregar más unidades? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    print(f"El producto '{producto}' no existe en el inventario.")
    nuevo = input("¿Querés agregarlo? (s/n): ").lower()
    if nuevo == "s":
        cantidad = int(input("¿Cuántas unidades tiene?: "))
        stock[producto] = cantidad
        print(f"{producto} fue agregado con {cantidad} unidades.")

# Mostrar el inventario final
print("\nInventario actualizado:", stock)
print()


#Actividad 9
# Agenda inicial
agenda = {
    ("lunes", "10:00"): "Clase de Matemática",
    ("martes", "14:00"): "Reunión con el equipo",
    ("viernes", "09:00"): "Entrenamiento"
}

# Mostrar agenda inicial
print("Agenda actual:")
for horario, evento in agenda.items():
    print(f"{horario[0].capitalize()} a las {horario[1]}: {evento}")

# Consultar un evento
dia = input("\nIngresá un día de la semana para consultar agenda: ").lower()
hora = input("Ingresá una hora: ")

clave = (dia, hora)

if clave in agenda:
    print(f"En {dia.capitalize()} a las {hora} tenés: {agenda[clave]}")
else:
    print(f"No hay eventos agendados para el {dia.capitalize()} a las {hora}.")
print()


#Actividad 10 

# Diccionario original: país → capital
pais_a_capital = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio",
    "Brasil": "Brasilia",
    "Italia": "Roma"
}

# Invertir el diccionario: capital → país
capital_a_pais = {}

for pais, capital in pais_a_capital.items():
    capital_a_pais[capital] = pais

# Mostrar el nuevo diccionario
print("Diccionario invertido (capital → país):")
for capital, pais in capital_a_pais.items():
    print(f"{capital}: {pais}")