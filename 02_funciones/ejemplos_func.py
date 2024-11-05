"""
Una función es un conjunto de instrucciones que realiza una tarea específica, y puedes usarla cada vez que la necesites, en lugar de escribir los mismos pasos una y otra vez.
"""
#Ejemplo Función sin Parámetros:

def saludar():
    print("¡Hola! Bienvenido a la programación en Python.")

# Llamamos a la función
saludar()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejemplo 2: Función con Parámetros:

def saludar_persona(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a la programación en Python.")

# Llamamos a la función con un argumento
saludar_persona("Carlos")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejemplo 3: Función con Retorno:

def sumar(a, b):
    resultado = a + b
    return resultado

# Llamamos a la función y guardamos el valor retornado
suma = sumar(3, 5)

print("La suma es:", suma)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Explicación de input() y float()/int()/str()
En Python, input() permite capturar información del usuario como texto. Por defecto, el valor que se recibe de input() es siempre de tipo cadena de texto (str), aunque 
se ingrese un número. Para usar ese valor como un número en cálculos, se debe convertir a tipo entero (int) o decimal (float), dependiendo de si necesitas números sin decimales o 
con decimales.

datos_usuario = input("Ingrese un numero: ")

Ejemplo básico:
Supón que quieres pedir al usuario que ingrese su altura en metros para convertirla a centímetros. Usamos float() porque la altura puede incluir decimales.

"""
#Ejemplo SIN manejo de errores
def metros_a_centimetros(metros):
    return metros * 100

altura_metros = float(input("Ingresa tu altura en metros (ejemplo: 1.75): "))
altura_centimetros = metros_a_centimetros(altura_metros)
print(f"Tu altura en centímetros es: {altura_centimetros} cm")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejemplo CON manejo de errores / Try y except ValueError
def metros_a_centimetros(metros):
    return metros * 100

try:
    # Pedimos al usuario que ingrese su altura en metros

    altura_metros = float(input("Ingresa tu altura en metros (ejemplo: 1.75): "))
    altura_centimetros = metros_a_centimetros(altura_metros)
    print(f"Tu altura en centímetros es: {altura_centimetros} cm")
    
except ValueError:
    print("Por favor, ingresa un número válido.")