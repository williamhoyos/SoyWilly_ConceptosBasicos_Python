"""
Ejercicio 1: Información de productos
Crea un diccionario con nombres de productos como claves y sus precios como valores. Luego, realiza las siguientes acciones:

Imprime el precio de un producto específico.
Aumenta el precio de todos los productos en un 10%.
Elimina un producto del diccionario.
"""
#Codigo:
"""
productos = {
    "Leche": 5000,
    "Huevos": 16000
}
print(f"La leche cuesta: {productos ["Leche"]} ")
del productos["Huevos"]
diccionario = {productos[valor] * 1.1 for valor in productos}
print(f"La leche cuesta: {diccionario} con el aumento de 10%")
"""


"""
Ejercicio 2: Contar caracteres
Escribe un código que reciba una cadena de texto y cree un diccionario con la cantidad de veces que aparece cada carácter en la cadena.
"""
#Codigo:
"""
texto = input("digite texto: ")
diccionario = {}
for caracter in texto:
    if caracter in diccionario:
        diccionario[caracter] += 1
    else:
        diccionario[caracter] = 1
print(diccionario)
"""

"""
Ejercicio 3: Filtrar un diccionario
Dado un diccionario con nombres de personas y sus edades, escribe un código que elimine a todas las personas mayores de 30 años del diccionario.
"""
#Codigo:
"""
nombres_personas = {"jipeto": 35, "bozuna": 19, "ultron": 14, "deivi": 48}
diccionario = {edad: nombres_personas[edad] for edad in nombres_personas if nombres_personas[edad] < 30}
print(diccionario)
"""

"""
Ejercicio 4: Crear un diccionario de contactos
Crea un diccionario donde las claves sean los nombres de personas y los valores sean sus números de teléfono. Luego:

Añade un nuevo contacto al diccionario.
Actualiza el número de teléfono de un contacto existente.
Imprime todos los contactos.
"""
#Codigo:
"""
contactos = {"jipeto": 353535, "bozuna": 19191919, "ultron": 14, "deivi": 484848}
contactos["willy"] = 99999
contactos["jipeto"] = 6666666
print(contactos)
"""

"""
Ejercicio 5: Diccionario con listas
Crea un diccionario donde las claves sean nombres de categorías (como "frutas", "verduras", "lácteos") y los valores sean listas de elementos que pertenecen a esa categoría. 
Luego, realiza lo siguiente:

Añade un nuevo elemento a una categoría.
Elimina un elemento de una categoría.
Imprime todas las categorías y sus elementos.
"""
#Codigo:
"""
productos = {
    "frutas": ["fresa", "plátano", "pera"], 
    "verduras": ["lechuga", "brócoli", "espinaca"], 
    "lacteos": ["yogur", "leche", "queso"]
}

productos["frutas"].append("manzana")
productos["lacteos"].remove("yogur")

for categoria, elementos in productos.items():
    print(f"{categoria.capitalize()}: {', '.join(elementos)}")
"""

