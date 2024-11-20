#Ejercicio 1:
lista_compras = ["manzanas", "platanos", "leche"]
lista_compras[2] = "jugo"
print(lista_compras)

#Ejercicio 2:
dias_semana = ("lunes", "martes", "miercoles", "jueves", "viernes, sabado", "domingo")
print(dias_semana[2])

#Ejercicio 3:
productos = ["Manzanas", "Platanos", "Peras", "Naranjas"]
productos.append("Uvas")
productos[1] = "Mangos"
productos.remove("Naranjas")
productos.sort()
print(productos)

#Ejercicio 4:

#Opcion corta:
tupla_ciudades = [
#       [0]               [1]
    ("cartacho", (40.7128, -74.0060)),
    ("medallo", (34.0522, -118.2437)),
    ("turbayork", (41.8781, -87.6298))
]

for i in tupla_ciudades:
    print(f"La coordenada de {i[0]} es: {i[1]}")

#Opcion larga pero mas organizada en nombres
tupla_ciudades = [
#       [0]               [1]
    ("cartacho", (40.7128, -74.0060)),
    ("medallo", (34.0522, -118.2437)),
    ("turbayork", (41.8781, -87.6298))
]

for i in tupla_ciudades:
    ciudad = i[0]
    coordenadas = i[1]
    print(f"La coordenada de {ciudad} es: {coordenadas}")

#Ejercicio 5:
lista = input("Ingresa varios numeros y separelos con espacio: ")
lista_separada = lista.split()
suma = sum(int(numero) for numero in lista_separada)
print(suma)