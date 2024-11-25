#------------------------------------------------------------------------------#

# Librerias

from datetime import datetime

#------------------------------------------------------------------------------#

# Listas

clientesRegistrados = []
administradoresRegistrados = []
cajerosRegistrados = []


#------------------------------------------------------------------------------#

# Clases

class Usuario:
    def __init__(self, idUsuario, nombre, nombreUsuario, contraseña):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.nombreUsuario = nombreUsuario
        self.contraseña = contraseña
        self.estado = "Activo"

class Administrador(Usuario):
    def __init__(self, idUsuario, nombre, nombreUsuario, contraseña):
        super().__init__(idUsuario, nombre, nombreUsuario, contraseña)
    
    def gestionarClientes(self):
        print("Función para gestionar clientes...")

    def gestionarCajeros(self):
        print("Función para gestionar cajeros...")

class Cliente(Usuario):
    def __init__(self, idUsuario, nombre, nombreUsuario, contraseña, cuenta):
        super().__init__(idUsuario, nombre, nombreUsuario, contraseña)
        self.cuenta = cuenta

    def realizarOperacion(self, tipo, monto):
        print(f"Realizando operación: {tipo} por un monto de {monto}...")


class Cuenta:
    def __init__(self, id_cuenta, saldo=0):
        self.id_cuenta = id_cuenta
        self.saldo = saldo
        self.movimientos = []  # Lista de movimientos asociados a la cuenta

    def depositar(self, monto):
        self.saldo += monto
        self.registrarMovimiento("Depósito", monto)

    def retirar(self, monto):
        if monto > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= monto
        self.registrarMovimiento("Retiro", monto)
        return True

    def registrarMovimiento(self, tipo, monto):
        movimiento = Movimiento(tipo, monto, datetime.now())
        self.movimientos.append(movimiento)

class Movimiento:
    def __init__(self, tipo, monto, fecha_hora):
        self.tipo = tipo
        self.monto = monto
        self.fecha_hora = fecha_hora

    def __str__(self):
        return f"{self.fecha_hora} - {self.tipo}: {self.monto}"

class Cajero:
    def __init__(self, id_cajero, region):
        self.id_cajero = id_cajero
        self.region = region
        self.billetes = {200: 0, 100: 0, 50: 0, 20: 0}  # Denominaciones y cantidades

    def agregarBilletes(self, denominacion, cantidad):
        if denominacion in self.billetes:
            self.billetes[denominacion] += cantidad
        else:
            print(f"Denominación {denominacion} no válida.")

    def retirarBilletes(self, monto):
        print(f"Realizando desglose de {monto} en billetes...")

class Billete:
    def __init__(self, denominacion, cantidad):
        self.denominacion = denominacion
        self.cantidad = cantidad

#------------------------------------------------------------------------------#

# Menús y sub menús

def gestionarClientes():
    while True:
        print("\n=== Gestión de Clientes ===")
        print("[1]. Agregar Cliente")
        print("[2]. Modificar Cliente")
        print("[3]. Cambiar Estado de Cuenta")
        print("[4]. Consultar Cliente")
        print("[5]. Listar Clientes")
        print("[6]. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarCliente()
        elif opcion == "2":
            modificarCliente()
        elif opcion == "3":
            cambiarEstadoCliente()
        elif opcion == "4":
            consultarCliente()
        elif opcion == "5":
            listarClientes()
        elif opcion == "6":
            return
        else:
            print("Opción inválida. Intente nuevamente.")

def modificarCliente():
    print("\n=== Modificar Cliente ===")
    nombre = input("Ingrese el nombre del cliente a modificar: ")
    for cliente in clientesRegistrados:
        if cliente.nombre == nombre:
            nuevoNombreUsuario = input("Ingrese el nuevo nombre de usuario (deje vacío para no cambiar): ")
            nuevaContraseña = input("Ingrese la nueva contraseña (deje vacío para no cambiar): ")

            if nuevoNombreUsuario:
                cliente.nombreUsuario = nuevoNombreUsuario
            if nuevaContraseña:
                cliente.contraseña = nuevaContraseña

            print("Cliente modificado con éxito.")
            return
    print(f"Cliente con nombre '{nombre}' no encontrado.")

def cambiarEstadoCliente():
    print("\n=== Cambiar Estado de Cuenta del Cliente ===")
    nombreUsuario = input("Ingrese el nombre de usuario del cliente: ")
    for cliente in clientesRegistrados:
        if cliente.nombreUsuario == nombreUsuario:
            nuevoEstado = input("¿Activar o Dar de baja? (A/D): ").upper()
            if nuevoEstado == "A":
                cliente.estado = "Activo"
                print(f"Cuenta del cliente '{nombreUsuario}' activada.")
            elif nuevoEstado == "D":
                cliente.estado = "Baja"
                print(f"Cuenta del cliente '{nombreUsuario}' dada de baja.")
            else:
                print("Opción inválida.")
            return
    print(f"Cliente con nombre de usuario '{nombreUsuario}' no encontrado.")

def consultarCliente():
    print("\n=== Consultar Cliente ===")
    nombreUsuario = input("Ingrese el nombre de usuario del cliente: ")
    for cliente in clientesRegistrados:
        if cliente.nombreUsuario == nombreUsuario:
            print(f"ID: {cliente.idUsuario}")
            print(f"Nombre: {cliente.nombre}")
            print(f"Nombre de usuario: {cliente.nombreUsuario}")
            print(f"Saldo: {cliente.cuenta.saldo}")
            print(f"Estado: {cliente.estado}")
            return
    print(f"Cliente con nombre de usuario '{nombreUsuario}' no encontrado.")

def listarClientes():
    print("\n=== Listar Clientes ===")
    if not clientesRegistrados:
        print("No hay clientes registrados.")
        return
    for cliente in clientesRegistrados:
        print(f"ID: {cliente.idUsuario} | Nombre: {cliente.nombre} | Usuario: {cliente.nombreUsuario} | Estado: {cliente.estado}")


def registrarCliente():
    print("\n=== Registro de Cliente ===")
    nombre = input("Ingresar el nombre: ")
    nombreUsuario = input("Ingrese el nombre de usuario: ")
    
    if usuarioRegistrado(nombreUsuario):
        print("Nombre de usuario ya registrado en una cuenta, ingresar otro nombre de usuario")
        return
        
    contraseña = input("Ingrese la contraseña: ")
    idUsuario = len(clientesRegistrados) + 1
    saldoInicial = 0
    nuevaCuenta = Cuenta(f"CU{idUsuario}", saldoInicial)
    nuevoCliente = Cliente(idUsuario, nombre, nombreUsuario, contraseña, nuevaCuenta)
    clientesRegistrados.append(nuevoCliente)
    print(f"Cliente '{nombreUsuario}' registrado con éxito.")

def registrarAdministrador():
    print("\n=== Registro de Administrador ===")
    nombreUsuario = input("Ingrese el nombre usuario: ")
    
    if usuarioRegistrado(nombreUsuario):
        print("Nombre de usuario ya registrado en una cuenta, ingresar otro nombre de usuario")
        return
    
    contraseña = input("Ingrese la contraseña: ")
    idUsuario = len(administradoresRegistrados) + 1
    nuevoAdmin = Administrador(idUsuario, nombreUsuario, contraseña)
    administradoresRegistrados.append(nuevoAdmin)
    print(f"Administrador '{nombreUsuario}' registrado con éxito.")

def usuarioRegistrado(nombreUsuario):
    for cliente in clientesRegistrados:
        if cliente.nombreUsuario == nombreUsuario:
            return True
        
    for administrador in administradoresRegistrados:
        if administrador.nombreUsuario == nombreUsuario:
            return True
    return False
    
def gestionarAdministrador():
    while True:
        print("\n=== Opciones de Administrador ===")
        print("1. Gestionar Clientes")
        print("2. Gestionar Cajeros")
        print("3. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionarClientes()
        elif opcion == "2":
            gestionarCajeros()
        elif opcion == "3":
            return
        else:
            print("Opción inválida. Intente nuevamente.")
            

def menuAdministrador():
    while True:
        print("\n=== Menú Administrador ===\n")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Volver atrás\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciarSesionAdministrador()
        elif opcion == "2":
            registrarAdministrador()
        elif opcion == "3":
            return
        else:
            print("Opción inválida. Intente nuevamente.")

def menuPrincipal():
    while True:
        print("\n=== Sistema de cajeros multfuncionales CustoPay ===\n")
        print("[1]. Administrador")
        print("[2]. Cliente")
        print("[3]. Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menuAdministrador()
        elif opcion == "2":
            menuCliente()
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            

def gestionarCajeros():
    print("\nFunción para gestionar cajeros...")

    
def iniciarSesionAdministrador():
    print("\n=== Inicio de Sesión Administrador ===")
    nombre = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    for admin in administradoresRegistrados:
        if admin.nombre == nombre and admin.contraseña == contraseña:
            print(f"¡Bienvenido, {nombre}!")
            gestionarAdministrador()
            return
    print("Credenciales incorrectas. Intente nuevamente.")

def menuCliente():
    while True:
        print("\n=== Menú Cliente ===\n")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Volver atrás\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciarSesionCliente()
        elif opcion == "2":
            registrarCliente()
        elif opcion == "3":
            return
        else:
            print("Opción inválida. Intente nuevamente.")

def clienteCajeros():
    while True:
        print("\n=== Seleccione Región===")
        print("1. Cajamarca")
        print("2. Lima")
        print("3. Loreto")
        print("4. Cuzco")
        print("5. Tacna")
        print("6. Piura")
        print("7. Regresar")
        opcion = input("Seleccione una región: ")

        if opcion in ["1", "2", "3", "4", "5", "6"]:
            operacionesCliente(opcion)
        elif opcion == "7":
            return
        else:
            print("Opción inválida. Intente nuevamente.")


def iniciarSesionCliente():
    print("\n=== Inicio de Sesión Cliente ===")
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    for cliente in clientesRegistrados:
        if cliente.nombreUsuario == nombreUsuario and cliente.contraseña == contraseña:
            if cliente.estado == "Baja":
                print("La cuenta está inactiva. Contacte al administrador.")
                return
            print(f"¡Bienvenido, {cliente.nombre}!")
            clienteCajeros()
            return
    print("Credenciales incorrectas. Intente nuevamente.")

def operacionesCliente(region):
    print(f"\n=== Operaciones en Cajero de Región {region} ===")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Transferir")
    print("4. Pagar Servicios")
    print("5. Consultar Saldo")
    print("6. Consultar Movimientos")
    print("7. Volver atrás")
    opcion = input("Seleccione una operación: ")

    if opcion == "7":
        return
    else:
        print("Función en desarrollo...")

#------------------------------------------------------------------------------#

menuPrincipal()
