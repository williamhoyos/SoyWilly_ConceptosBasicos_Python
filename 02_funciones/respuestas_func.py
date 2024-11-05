#Ejercicio 1:
def horas_a_minutos(horas):
    minutos = horas * 60
    return minutos
llamado = horas_a_minutos(2)
print(llamado)

#ejercicio 2:
def calcular_area_circulo (radio):
    pi = 3.14159            
    area = pi * radio**2 #Opcion pro: area = math.pi * (radio ** 2) 
    return area

ElArea = calcular_area_circulo(7)
print(ElArea)

#Ejercicio 3:
def multiplica(a, b):
    resultado = a * b
    return resultado
llamado = multiplica(3, 4)
print(llamado)

#ejercicio 4:
def celsius_a_fahrenheit (grados_celsius):
    fahrenheit = grados_celsius * 9/5 + 32
    return fahrenheit
try:

    grados_celsius=  int(input("Ingresa los grados celsius: "))
    conversion = celsius_a_fahrenheit(grados_celsius)
    print(f"Los grados fahrenheit son: {conversion}")

except ValueError:
    print("Por favor, ingresa un número entero.")