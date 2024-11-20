"""
Listas: Son mutables, lo que significa que puedes cambiar sus elementos después de haberlas creado. Se definen usando corchetes [].

lista_nombres = ["Ana", "Luis", "Carlos"]
"""
#Ejemplo mutables:

lista_nombres = ["Ana", "Luis", "Carlos"]
lista_nombres.append("Maria")  # Agrega "Maria" al final de la lista
lista_nombres[1] = "Jose"      # Cambia "Luis" por "Jose"
print(lista_nombres)           # Muestra: ["Ana", "Jose", "Carlos", "Maria"]

"""
Tuplas: Son inmutables, lo que significa que no puedes cambiar sus elementos una vez que las has creado. Se definen usando paréntesis ().

tupla_colores = ("Rojo", "Azul", "Verde")
"""
#Ejemplo inmutables:
tupla_colores = ("Rojo", "Azul", "Verde")
print(tupla_colores[0])  # Muestra: "Rojo"

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Usos de listas:

#Añadir un elemento al final de la lista:
"""
lista.append("Amarillo")
"""
#Eliminar un elemento específico
"""
lista.remove("Amarillo")
"""
#Ordena alfabeticamente:
"""
lista.sort()
"""

#Filtrar:
edades = [12, 17, 19, 24, 15, 22, 16, 25]
edades_mayores = [edad for edad in edades if edad > 18]  # Filtra las edades mayores de 18
print(edades_mayores)  # Muestra: [19, 24, 22, 25]

#Encontrar maximo o minimo:
"""
ccalificacion_max = max(calificaciones)  # Encuentra la calificación más alta
calificacion_min = min(calificaciones)  # Encuentra la calificación más baja
"""
#Contar veces que se repite algo:
nombres = ["Ana", "Luis", "Carlos", "Ana", "Maria", "Luis", "Carlos", "Ana"]
conteo_nombres = {nombre: nombres.count(nombre) for nombre in set(nombres)}
print("Conteo de nombres:", conteo_nombres)  # Muestra cuántas veces aparece cada nombre

#Lista anidada:
calificaciones_estudiantes = [
#      [0]       [1]      
    ["Ana", [85, 90, 78]],
    ["Luis", [76, 88, 91]],
    ["Carlos", [92, 79, 85]]
]

for estudiante in calificaciones_estudiantes:
    nombre = estudiante[0]
    calificaciones = estudiante[1]
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre} tiene un promedio de: {promedio}")


