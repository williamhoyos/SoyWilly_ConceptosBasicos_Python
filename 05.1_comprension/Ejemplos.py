"""
Crea una lista de los cubos de los números impares entre 1 y 20.
Usa un rango para generar los números y una condición para filtrar solo los impares.
"""
#Codigo:

#lista = [x**3 for x in range(1, 20) if not x % 2 == 0]
#print(lista)
"""
Filtrar y convertir a mayúsculas:

Dada una lista de palabras ["perro", "gato", "león", "lobo", "elefante"], crea una nueva lista que contenga solo las palabras que tienen más de 4 letras y estén en mayúsculas.
"""
#Codigo:
#palabras = ["perro", "gato", "león", "lobo", "elefante"]
#lista = [x.upper() for x in palabras if len(x) > 4]
#print(lista)
"""
Números divisibles por 3 o 5:

Crea una lista de los números entre 1 y 50 que sean divisibles por 3 o por 5.
"""
#Codigo:
#lista = [x for x in range (1, 50) if x % 3 == 0 or x % 5 == 0]
#print(lista)
"""
Multiplicación de pares y reducción de impares:

Dada una lista de números numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una lista nueva donde:
Los números pares se multipliquen por 2.
Los números impares se dividan por 2.
"""
#Codigo:
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#lista = [x * 2 if x % 2 == 0 else x / 2 for x in numeros]
#print(lista)
"""
ejercicio 5
Extraer la primera letra de cada palabra:

Dada una lista de frases frases = ["Hola mundo", "Python es genial", "Listas de comprensión"], crea una lista que contenga solo la primera letra de cada palabra de todas las frases.
"""
#Codigo:
#frases = ["Hola mundo", "Python es genial", "Listas de comprensión"]
#lista = [palabra for frase in frases for palabra in frase.split()] 
#print(lista)
"""
Ejercicio 6: Filtrar y modificar los números negativos
Dada la siguiente lista de números: [-1, 2, -3, 4, -5, 6, -7, 8], crea una nueva lista con los valores absolutos de los números negativos y los cuadrados de los números positivos.
"""
#Codigo:
####numeros = [-1, 2, -3, 4, -5, 6, -7, 8]
####lista = [abs(nnumero) for nnumero in numeros if nnumero > 0 ]
"""
Ejercicio 7: Crear un diccionario de longitudes de palabras
Dada la lista de palabras ["manzana", "plátano", "cereza", "kiwi"], crea un diccionario donde las claves sean las palabras y los valores sean la longitud de cada palabra.
"""
#Codigo:
#palabras = ["manzana", "plátano", "cereza", "kiwi"]
#diccionario = {x: len(x) for x in palabras}
#print(diccionario)

"""
Ejercicio 8: Filtrar números en un rango con condiciones
Dado un rango de números entre 1 y 100, crea una lista con todos los números que sean divisibles por 5 o 7, pero que no sean divisibles por 3.
"""
#Codigo:
#lista = [x for x in range (1, 101) if (x % 5 == 0 or x % 7 == 0) and x % 3 != 0]
#print(lista)
"""
Ejercicio 9: Invertir las palabras de una lista
Dada la lista de frases ["Python es fácil", "Me gusta programar", "El sol brilla"], crea una lista con las palabras de cada frase invertidas (no las frases completas,
 solo las palabras). Por ejemplo, "Python es fácil" se convertiría en ["nohtyP", "se", "lícaf"].
"""
#Codigo:


"""
Ejercicio 10: Convertir grados Celsius a Fahrenheit
Dada una lista de temperaturas en grados Celsius [-10, 0, 10, 20, 30], crea una lista con las correspondientes temperaturas en grados Fahrenheit, 
usando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.
"""
#Celsius = [-10, 0, 10, 20, 30]
#fahrenheit = [(x * 9/5) + 32 for x in Celsius]
#print(fahrenheit)