#ejercicio 1:
def clasificar_edad (edad):
    if edad < 13:
        return "Es un niño"

    elif edad >= 13 and edad <= 17: #if edad in range(13,18):
        return "Es un adolescente"

    elif edad >= 18:
        return "Es un adulto"
try:
    IngreseEdad = int(input("Ingrese su edad: "))
    respuesta = clasificar_edad(IngreseEdad)
    print(respuesta)

except ValueError:
    print("Ingrese un numero valido para la edad")