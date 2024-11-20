"""
Ejercicio 1: Simulación de Login

Crea un programa que haga lo siguiente:

Define una clase llamada Cuenta con los atributos usuario y contraseña.
Agrega un método en la clase llamado validar_login que reciba un nombre de usuario y contraseña como parámetros, y valide si coinciden con los datos almacenados.
El programa debe:
Pedir al usuario que ingrese su nombre de usuario y contraseña.
Validar si las credenciales son correctas.
Mostrar un mensaje que indique si el login fue exitoso o fallido.
"""
#Codigo:
"""
class login:
    def __init__ (self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def validacion(self, digite_usuario, digite_contraseña):
        if (self.usuario == digite_usuario) and (self.contraseña == digite_contraseña):
            return "Los datos son correctos"

        elif (self.usuario != digite_usuario) and (self.contraseña != digite_contraseña):
            return "El usuario y la contraseña son incorrectos"

        elif self.usuario != digite_usuario:
            return "EL usuario es incorrecto"
        else:
            return "La contraseña es incorrecta"

#creacion de cuenta
nombre = input("crea un usuario: ")
clave = input("Crea una contraseña: ")
usuario1 = login(nombre, clave)

#inicio de sesion
print("Inicio de sesion")
login_usuario = input("Usuario: ")
login_contraseña = input("Contraseña: ")

#validacion de datos
cuenta = usuario1.validacion(login_usuario, login_contraseña)
print(cuenta)
"""

"""
Ejercicio: Simulador de Inventario de Tienda
Crea un programa que permita gestionar un inventario utilizando una clase. Debe tener las siguientes funcionalidades:

Clase Inventario:

Tiene un diccionario donde las claves son nombres de productos y los valores son las cantidades de cada producto.
Métodos para:
Añadir productos al inventario.
Eliminar productos del inventario.
Actualizar la cantidad de un producto existente.
Consultar el inventario completo.
Interacción con el usuario:

El programa debe permitir:
Añadir un producto nuevo.
Eliminar un producto existente.
Actualizar la cantidad de un producto existente.
Mostrar todo el inventario.
Salir del programa.

Requisitos:
Usa bucles, condiciones, métodos y diccionarios.
Maneja entradas no válidas (por ejemplo, intentar eliminar un producto que no existe o ingresar cantidades negativas).
Crea un menú interactivo para el usuario.
"""
#Codigo:
