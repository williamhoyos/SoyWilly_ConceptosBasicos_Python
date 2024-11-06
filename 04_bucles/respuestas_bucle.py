#ejercicio 1:

def tabla(num):
    for numero in range(1, 11):
        resultado = num * numero
        print(f"{numero} x {num} = {resultado}")
    
num = int(input("Ingrese un numero del 1 al 10: "))
llamado = tabla(num)
print(llamado)

#Ejercicio 2:
def pedir_numero():
    suma = 0
    while True:
        num = int(input("Digite un numero positivo o negativo: "))
        if num < 0:
            break
        #else:
        suma += num
    print(suma)
pedir_numero()

#Ejercicio 3:
def funcion (a, b):
        return (a % 5 == 0) and (b % 5 == 0)

a = int(input("Digita un numero multiplo de 5: "))
b = int(input("Digita otro numero multiplo de 5: "))

resultado = funcion(a, b)
print("Ambos son multiplos?: ", resultado)

#Ejercicio 4: 
def funcion(edades):
    return edades >= 18
for i in range(5):
    edades = int(input("Ingresa una edad: "))
    if funcion(edades):
        print("Es mayor de edad: ")
    else:
        print("Es menor de edad")