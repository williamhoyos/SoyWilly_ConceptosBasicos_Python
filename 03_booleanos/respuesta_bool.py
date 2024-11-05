#ejercicio 1:
def clasificar_edad (edad):
    if edad < 13:
        return "Es un niño"

    elif edad in range(13,18):
        return "Es un adolescente"

    else:
        return "Es un adulto"
try:
    edad = int(input("Ingrese su edad: "))
    respuesta = clasificar_edad(edad)
    print(respuesta)

except ValueError:
    print("Ingrese un numero valido para la edad")

#Ejercicio 2:
def es_positivo(numero):
    return numero > 0
numero = float(input("Ingresa un numero positivo o negativo: "))
print(es_positivo(numero))