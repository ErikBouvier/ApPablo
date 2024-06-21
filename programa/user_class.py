class Usuario:
    def __init__(self, nombre, email, contrasena, direccion):
        self.nombre = nombre
        self.contrasena = contrasena
        self.email = email
        self.direccion = direccion

    def buscar_articulo(self):
        nombre_mayus = self.nombre.capitalize()
        return f"¿{nombre_mayus} que deseas comprar?"

    def comprar_articulo(self, producto):
        nombre_mayus = self.nombre.capitalize()
        return f"El usuairo {nombre_mayus} a comprado un articulo {producto}"

    def __str__(self):
        return f"El usuario es: {self.nombre}, y su email es: {self.email}"


class UsuarioVip(Usuario):
    def __init__(self, nombre, email, contrasena, direccion, descuento=10):
        super().__init__(nombre, email, contrasena, direccion)
        self.descuento = descuento

    def __str__(self):
        return f"El usuario VIP es: {self.nombre}, su direccion es: {self.direccion}, y tiene un descuento {self.descuento} %"
