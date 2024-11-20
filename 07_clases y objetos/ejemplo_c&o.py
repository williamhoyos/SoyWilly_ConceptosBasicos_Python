class Cuenta:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
    def saludar_al_usuario(self, mensaje):
        return f"{mensaje} malparido {self.usuario}"
    
    
usuario = Cuenta("Willyrex", "pene123")
mensaje = usuario.saludar_al_usuario("Hola, ")
print(mensaje)