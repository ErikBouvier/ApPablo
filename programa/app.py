from user_class import Usuario, UsuarioVip
from catalogo import catalogo
# declaro una variable usuarios donde se almacenaran los usuarios con su contraseña:
usuarios = []

# defino una variable global, con el nombre usuario_logueado, para usar en la funcion login y logout:
usuario_logueado = None


# defino la funcion registrar_usuario, para que se registre con nombre y contraseña:


def registro_usuarios(nombre, email, contrasena, direccion, vip=False):
    if not any(u.nombre == nombre for u in usuarios):
        if vip:
            usuario = UsuarioVip(nombre, email, contrasena, direccion)
        else:
            usuario = Usuario(nombre, email, contrasena, direccion)
        usuarios.append(usuario)
        print("Usuario registrado con exito.")
    else:
        print("El usuario ya esta registrado.")

# defino la funcion mostrar_usuario, para mostrar todos los usuairos registrados:


def mostrar_usuarios():
    if not usuarios:
        print("Aun no hay usuarios registrados. \n")
        return
    for usuario in usuarios:
        print(usuario)


# defino una funcion para validar la contraseña del usuario en el momento de loguearse, con una sentencia try-except KeyError:

def validar_contrasena(nombre, contrasena):
    try:
        for usuario in usuarios:
            if usuario.nombre == nombre:
                if usuario.contrasena == contrasena:
                    return True
                else:
                    return False
        return False
    except KeyError:
        print("Ha ocurrido un error inesperado. \n")
        return None


# defino la funcion para loguearse:

def login():
    global usuario_logueado
    if usuario_logueado:
        print("Existe un usuario logueado. Cierre sesion para ingresar con otro usuairo. ")
        return
    usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if validar_contrasena(usuario, contrasena):
        print(f"{usuario} loqueado/a exitosamente 😃 \n")
        usuario_logueado = next(u for u in usuarios if u.nombre == usuario)
    else:
        print("Contraseña incorrecta. Intente nuevamente. \n")

# Funcion para borrar usuario


def borrar_usuario():
    global usuario_logueado
    if not usuario_logueado:
        print("Debe ingresar para borrar un usuraio. ")
        return
    nombre = input("Ingrese el nombre de usuario que desea borrar: ")
    for usuario in usuarios.copy():
        if usuario.nombre == nombre:
            usuarios.remove(usuario)
            print(f"Usuario {usuario.nombre} borrado con exito. ")
            if nombre == usuario_logueado:
                usuario_logueado = None
        else:
            print(f"El usuario {usuario} no esta registrado. ")

# defino una funcion que muestra articulos de un catalogo solo si el usuario esta logueado


def buscar_articulo():
    global usuario_logueado
    if usuario_logueado:
        print(usuario_logueado.buscar_articulo())
        print("Catalogo de articulos: ")
        for i, articulo in enumerate(catalogo, start=1):
            print(f"{i}. Nombre: {articulo["nombre"]}, Precio: U$S{articulo["precio"]}")
    else:
        print("Debe estar logueado para buscar ariculos. ")

# Defino una funcion para comprar articulos del catalogo solo si el usuario esta logueado

def comprar_articulo(nombre_articulo):
    global usuario_logueado
    if not usuario_logueado:
        print("Debe ingresar para realizar la compra. \n")
        return False
    for articulo in catalogo:
        if articulo["nombre"].lower() == nombre_articulo.lower():
            if not articulo.get("comprado", False):
                articulo["comprado"] = True
                print(f"{usuario_logueado.comprar_articulo(nombre_articulo)}")
                return True
            else:
                print(f"{nombre_articulo} ya esta marcado domo comprado.")
                return False
    print(f"No se encontro el {nombre_articulo} en el catalogo.")
    return False

# Defino una funcion para desloguearse

def logout():
    global usuario_logueado
    if usuario_logueado:
        print(
            f"Usuario {usuario_logueado.nombre} deslogueado exitosamente. \n")
        usuario_logueado = None
    else:
        print("No hay usuarios logueados. ")


# defino una funcion menu para ejecutar todo el programa por consola, a la cual le aplico la sentencia try-except, por si ocurre
# una excepcion:


def menu():
    try:
        while True:
            print("Menú:")
            print("1 - Resgistrar nuevo usuario.")
            print("2 - Registrar usuairo VIP.")
            print("3 - Mostrar usuarios registrados.")
            print("4 - Login.")
            print("5 - Borrar usuario.")
            print("6 - Buscar articulo.")
            print("7 - Comprar articulo.")
            print("8 - Logout.")
            print("9 - Salir.")
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                nombre = input("Ingrese su nombre de usuario: ")
                contrasena = input("ingrese su contraseña: ")
                email = input("Ingrese su direccion de correo electronico: ")
                direccion = input("ingrese su direccion: ")
                registro_usuarios(nombre, email, contrasena,  direccion)
            elif opcion == "2":
                nombre = input("Ingrese su nombre de usuario: ")
                contrasena = input("ingrese su contraseña: ")
                email = input("Ingrese su direccion de correo electronico: ")
                direccion = input("Ingrese su direccion: ")
                registro_usuarios(nombre, email, contrasena, direccion, vip=True)
            elif opcion == "3":
                mostrar_usuarios()
            elif opcion == "4":
                login()
            elif opcion == "5":
                borrar_usuario()
            elif opcion == "6":
                buscar_articulo()
            elif opcion == "7":
                nombre_articulo = input(
                    "Ingresa el articulo que deseas comprar: ")
                comprar_exitoso = comprar_articulo(nombre_articulo)
                if comprar_exitoso:
                    print(f"Has comprado {nombre_articulo} con exito!.")
            elif opcion == "8":
                logout()
            elif opcion == "9":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion incorrecta. Por favor ingrese una opcion valida. \n")
    except Exception as e:
        print("Ha ocurrido un error", type(e).__name__)

# hago la llamada a la funcion menu():


menu()
