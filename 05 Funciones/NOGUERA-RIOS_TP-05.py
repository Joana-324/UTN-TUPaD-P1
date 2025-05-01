#Estudiante: Joana Noguera Ríos.

print("Actividad 1:")
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiplos_de4 = list(range(4, 101, 4))
print (multiplos_de4)

print("Actividad 2:")
#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
colores = ["blanco", "rojo", "azul", "verde", "gris"]
print(colores[3])

print("Actividad 3:")
#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []
animales = []
animales.append("perro")
animales.append("gato")
animales.append("conejo")
print(animales)

print("Actividad 4:")
#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
#Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

print("Actividad 5:")
#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
print("Con 'max(numeros)' obtenemos el número más alto, 22 en este caso. Con 'numeros. remove' lo que hace es eliminar de la lista este número más alto seleccionado.")
print("Al realizar print, este número no aparecerá en la lista que se imprime por pantalla.")

print("Actividad 6:")
#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))
print (numeros[0])
print (numeros[1])

print("Actividad 7:")
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "ford"
autos[2] = "fiat"
print(autos)

print("Actividad 8:")
#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

print("Actividad 9:")
# Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append.
tercer_lista = compras[2]
tercer_lista.append("jugo")

#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

#d) Imprimir la lista resultante por pantalla
print(compras)

print("Actividad 10: ")
#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)