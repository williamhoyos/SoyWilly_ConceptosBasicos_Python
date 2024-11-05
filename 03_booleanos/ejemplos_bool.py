"""
Los booleanos son muy útiles para tomar decisiones en tu código. Puedes usarlos para hacer que una función devuelva True o False según si se cumple una condición o no.
También puedes usarlos para comparar valores, por ejemplo, saber si un número es mayor que otro, o si dos valores son iguales.
"""

edad = 20

if edad >= 18:
    print("Eres mayor de edad.")
elif edad > 13:
    print("Eres un adolescente.")
else:
    print("Eres un niño.")

"""
En python a diferencia de otros lenguajes no necesitas invocar if, leif, else para que el programa lo entienda como booleano (true o false)
"""

def es_par(numero):
    return numero % 2 == 0  # Devuelve True si el número es par, False si es impar

# Ejemplos de uso
print(es_par(4))  # Imprime: True
print(es_par(7))  # Imprime: False