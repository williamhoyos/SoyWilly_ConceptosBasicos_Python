#ejercicio 1:
def calcular_area_circulo (radio):
    #area = math.pi * (radio ** 2) --- respuesta pro
    pi = 3.14159
    area = pi * radio**2
    return area

ElArea = calcular_area_circulo(7)
print(ElArea)

#ejercicio 2:
def celsius_a_fahrenheit (grados_celsius):
    fahrenheit = grados_celsius * 9/5 + 32
    return fahrenheit
try:

    resultado =  int(input("Ingresa los grados celsius: "))
    grados_fahrenheit = celsius_a_fahrenheit(resultado)
    print(f"Los grados fahrenheit son: {grados_fahrenheit}")

except ValueError:
    print("Por favor, ingresa un número entero.")