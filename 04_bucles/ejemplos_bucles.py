"""
Bucles while
El bucle while se ejecuta mientras una condición sea True. Se utiliza cuando no se sabe exactamente cuántas veces se debe repetir el bloque de código.

contador = 1
while contador <= 5:
    print("Esta es la vuelta número", contador)
    contador += 1
--------------------------------------------------------------------------------------------------
Bucles for
El bucle for se usa para iterar sobre una secuencia, como una lista, cadena o rango de números. Es útil cuando sabes cuántas veces quieres que se ejecute el bloque de código.

for numero in range(1, 6):
    print("Esta es la vuelta número", numero)
--------------------------------------------------------------------------------------------------
"""

"""
Ejercicio 1: (bulce for)
Solicita al usuario que ingrese un número y luego utiliza un bucle for para imprimir la tabla de multiplicar de ese número, desde el 1 hasta el 10.
Usa el bucle for para iterar del 1 al 10 y realiza la multiplicación en cada paso.
"""
#Escribe aqui tu codigo:

"""
Ejercicio 2: (bucle while)
Escribe un programa que genere un número aleatorio entre 1 y 10 (puedes usar numero_aleatorio = random.randint(1, 10) para esto) y pida al usuario que adivine el número.
El programa debe continuar pidiendo al usuario que ingrese un número hasta que lo adivine correctamente. Para ayudar al usuario, el programa le dirá si el número ingresado 
es "muy alto" o "muy bajo" en comparación con el número secreto.

Requerimientos:

Usa un bucle while que continúe ejecutándose hasta que el usuario adivine el número.
Imprime mensajes como "Demasiado alto" o "Demasiado bajo" para guiar al usuario.
Al acertar, felicita al usuario e imprime el número de intentos que le tomó adivinar.

Pistas:
Recuerda importar la librería random con import random al inicio del codigo.
Usa un contador para llevar el número de intentos.

Ejemplo:
Estoy pensando en un número entre 1 y 100...
Ingresa tu adivinanza: 50
Demasiado alto. Intenta nuevamente.
Ingresa tu adivinanza: 25
Demasiado bajo. Intenta nuevamente.
Ingresa tu adivinanza: 37
¡Correcto! Adivinaste en 3 intentos.
"""
#Escribe aqui tu codigo:

import random
# Genera un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
intentos = 0  # Inicializa el contador de intentos
# Un bucle while para que el usuario siga intentando
while True:
    numero = int(input("Ingresa tu número: "))
    intentos += 1  # Incrementa el contador de intentos

    if numero < numero_aleatorio:
        print("Demasiado bajo. Intenta nuevamente.")
    elif numero > numero_aleatorio:
        print("Demasiado alto. Intenta nuevamente.")
    else:
        print(f"¡Correcto! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
        break  # Sale del bucle si el número es correcto