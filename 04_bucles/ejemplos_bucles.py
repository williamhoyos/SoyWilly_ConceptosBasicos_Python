"""
Bucles while
El bucle while se ejecuta mientras una condición sea True. Se utiliza cuando no se sabe exactamente cuántas veces se debe repetir el bloque de código.
"""

#Ejemplo 1:
contador = 1
while contador <= 5:
    print("WHILE Esta es la vuelta número", contador)
    contador += 1

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejemplo 2:
def adivinar_numero_secreto():
    numero_secreto = 7  # Definimos el número secreto
    intentos = 0  # Contador de intentos

    while True:
        intento = int(input("Adivina el número secreto (entre 1 y 10): "))
        intentos += 1  # Incrementa el contador de intentos

        if intento == numero_secreto:
            print("¡Felicidades! Has adivinado el número.")
            break  # Salimos del bucle al adivinar correctamente
        elif intento < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")

    print(f"Has adivinado el número en {intentos} intentos.")

# Llamamos a la función
adivinar_numero_secreto()
"""
Bucles for
El bucle for se usa para iterar sobre una secuencia, como una lista, cadena o rango de números. Es útil cuando sabes cuántas veces quieres que se ejecute el bloque de código.
"""
#Ejemplo 1:
for numero in range(1, 6):
    print("FOR Esta es la vuelta número", numero)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejemplo 2:
def verificar_longitud_nombre(nombre):
    return len(nombre) > 5  # Devuelve True si el nombre tiene más de 5 letras

# Bucle para pedir cinco nombres
for i in range(5):  # Repetimos el proceso cinco veces
    nombre = input("Ingresa un nombre: ")
    if verificar_longitud_nombre(nombre):
        print(f"El nombre '{nombre}' tiene más de 5 letras.")
    else:
        print(f"El nombre '{nombre}' tiene 5 letras o menos.")