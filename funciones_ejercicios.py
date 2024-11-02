"""
Ejemplo Función sin Parámetros:

def saludar():
    print("¡Hola! Bienvenido a la programación en Python.")

# Llamamos a la función
saludar()
--------------------------------------------------------------------------------------------------
Ejemplo 2: Función con Parámetros:

def saludar_persona(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a la programación en Python.")

# Llamamos a la función con un argumento
saludar_persona("Carlos")
--------------------------------------------------------------------------------------------------
Ejemplo 3: Función con Retorno:

def sumar(a, b):
    resultado = a + b
    return resultado

# Llamamos a la función y guardamos el valor retornado
suma = sumar(3, 5)
print("La suma es:", suma)
--------------------------------------------------------------------------------------------------
Explicación de input() y float()
En Python, input() permite capturar información del usuario como texto. Por defecto, el valor que se recibe de input() es siempre de tipo cadena de texto (str), aunque 
se ingrese un número. Para usar ese valor como un número en cálculos, se debe convertir a tipo entero (int) o decimal (float), dependiendo de si necesitas números sin decimales o 
con decimales.

Ejemplo básico
Supón que quieres pedir al usuario que ingrese su altura en metros para convertirla a centímetros. Usamos float() porque la altura puede incluir decimales.

def metros_a_centimetros(metros):
    return metros * 100

try:
    # Pedimos al usuario que ingrese su altura en metros

    altura_metros = float(input("Ingresa tu altura en metros (ejemplo: 1.75): "))
    altura_centimetros = metros_a_centimetros(altura_metros)
    print(f"Tu altura en centímetros es: {altura_centimetros} cm")
    
except ValueError:
    print("Por favor, ingresa un número válido.")
--------------------------------------------------------------------------------------------------
"""

"""
Ejercicio 1:
Crea una función llamada calcular_area_circulo que tome el radio de un círculo como parámetro y devuelva el área del círculo. La fórmula para calcular el área de un círculo es:
area = pi * radio^2
pi = 3.14159
"""
#Escribe aqui tu codigo:

"""
Ejercicio 2:
Escribe una función llamada celsius_a_fahrenheit que tome una temperatura en grados Celsius y la convierta a Fahrenheit. Usa la fórmula:
F = C * 9/5 + 32
a diferencia del mismo ejercicio en variables, aca el usuario debe ingresar manualmente los grados celsius
"""
#Escribe aqui tu codigo: