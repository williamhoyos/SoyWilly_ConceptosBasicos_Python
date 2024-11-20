"""
Clase de un círculo
Crea una clase llamada Circulo que tenga:

Un atributo para el radio.
Métodos para calcular el área y la circunferencia del círculo.
"""
#Codigo:

import math
class circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return math.pi * self.radio**2
    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio
    
radio = float(input("meteme el radio: "))
forma = circulo(radio) 

print(forma.calcular_area())
print(forma.calcular_circunferencia())



"""
Clase de un estudiante
Crea una clase Estudiante que tenga:

Atributos para el nombre, la edad y las notas de 3 materias.
Métodos para:
Calcular el promedio de las notas.
Determinar si el estudiante aprobó (promedio ≥ 60).
"""
#codigo:
class estudiante:
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        self.nombre = nombre
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def calcular_promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

nombre = input("Diga su nombre: ")
edad = int(input("Diga su edad: "))
nota1 = int(input("Diga primera su nota: "))
nota2 = int(input("Diga segunda su nota: "))
nota3 = int(input("Diga tercera su nota: ")) 

estudiante1 = estudiante(nombre, edad, nota1, nota2, nota3)
promedio = estudiante1.calcular_promedio()

if promedio >= 60:
    print("Aprobado con: ", promedio)
else:
    print("Reprobo con: ", promedio)



"""
Clase de una cuenta bancaria
Crea una clase CuentaBancaria que permita:

Abrir una cuenta con un saldo inicial.
Métodos para depositar, retirar y consultar el saldo actual.
Asegúrate de que no se pueda retirar más de lo que hay en la cuenta.

imprima 
"""

#Codigo:
class cuenta:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, monto):
        self.saldo += monto
        return self.saldo
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return self.saldo
        else:
            print("Cuando fokin pagan")

cuenta1 = cuenta(5000)

deposito = int(input("cuanto billete vas a meter: "))
sacar = int(input("Cuanto billete vas a sacar: "))

nuevo_saldo = cuenta1.depositar(deposito)
saldo_actual = cuenta1.retirar(sacar)
print("su saldo luego de las acciones es: ", saldo_actual)


#
class cuenta:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, monto):
        self.saldo += monto
        return self.saldo
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return self.saldo
        else:
            print("Cuando fokin pagan")

cuenta1 = cuenta(5000)
while True:

    print("1.Retiros")
    print("2.Depositos")
    print("3.Consultas")
    print("4.Salir")
    opcion = int(input("Que vas a hacer: "))
    if opcion == 1:
        retiro = int(input("cuanto billete vas a retirar: "))
        cuenta1.retirar(retiro)

    elif opcion == 2:
        deposito = int(input("cuanto billete vas a depositar: "))
        cuenta1.depositar(deposito)

    elif opcion == 3:
        print("tu saldo actual es: ", cuenta1.saldo)

    elif opcion == 4:
        break

    else:
        print("mete un numero de la lista bobo")
