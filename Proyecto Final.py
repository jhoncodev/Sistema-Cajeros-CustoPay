#------------------------------------------------------------------------------#

# Librerias

from datetime import datetime

#------------------------------------------------------------------------------#

# Listas

clientesRegistrados = []
administradoresRegistrados = []


#------------------------------------------------------------------------------#

# Clases

class Usuario:
    def __init__(self, idUsuario, nombreUsuario, contraseña):
        self.idUsuario = idUsuario
        self.nombreUsuario = nombreUsuario
        self.contraseña = contraseña

class Administrador(Usuario):
    def __init__(self, id_usuario, nombreUsuario, contraseña):
        super().__init__(id_usuario, nombreUsuario, contraseña)
    
    def gestionarClientes(self):
        print("Función para gestionar clientes...")

    def gestionarCajeros(self):
        print("Función para gestionar cajeros...")

class Cliente(Usuario):
    def __init__(self, id_usuario, nombreUsuario, contraseña, cuenta):
        super().__init__(id_usuario, nombreUsuario, contraseña)
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

def menuPrincipal():
    while True:
        print("\n=== Sistema de cajeros multfuncionales CustoPay ===\n")
        print("1. Administrador")
        print("2. Cliente")
        print("3. Salir\n")
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

def menuAdministrador():
    while True:
        print("\n=== Menú Administrador ===\n")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciarSesionAdministrador()
        elif opcion == "2":
            registrarAdministrador()
        elif opcion == "3":
            return
        else:
            print("Opción inválida. Intente nuevamente.")

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

def registrarAdministrador():
    print("\n=== Registro de Administrador ===")
    nombreUsuario = input("Ingrese el nombre usuario: ")

    registrado = usuarioRegistrado(nombreUsuario)
    
    if registrado:
        print("Nombre de usuario ya registrado en una cuenta, ingresar otro nombre de usuario")
        return
    
    contraseña = input("Ingrese la contraseña: ")
    idUsuario = len(administradoresRegistrados) + 1
    nuevoAdmin = Administrador(idUsuario, nombreUsuario, contraseña)
    administradoresRegistrados.append(nuevoAdmin)
    print(f"Administrador '{nombreUsuario}' registrado con éxito.")
    
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
        print("3. Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciarSesionCliente()
        elif opcion == "2":
            registrarCliente()
        elif opcion == "3":
            return
        else:
            print("Opción inválida. Intente nuevamente.")

def gestionarClientes():
    print("\nFunción para gestionar clientes...")

def gestionarCajeros():
    print("\nFunción para gestionar cajeros...")

def clienteCajeros():
    while True:
        print("\n=== Seleccione Región ===")
        print("1. Cajero Cajamarca")
        print("2. Cajero Lima")
        print("3. Cajero Loreto")
        print("4. Cajero Cuzco")
        print("5. Cajero Tacna")
        print("6. Cajero Piura")
        print("7. Regresar")
        opcion = input("Seleccione una región: ")

        if opcion in ["1", "2", "3", "4", "5", "6"]:
            operacionesCliente(opcion)
        elif opcion == "7":
            return
        else:
            print("Opción inválida. Intente nuevamente.")

def registrarCliente():
    print("\n=== Registro de Cliente ===")
    nombreUsuario = input("Ingrese el nombre de usuario: ")
    
    registrado = usuarioRegistrado(nombreUsuario)
    
    if registrado:
        print("Nombre de usuario ya registrado en una cuenta, ingresar otro nombre de usuario")
        return
        
    contraseña = input("Ingrese la contraseña: ")
    idUsuario = len(clientesRegistrados) + 1
    saldoInicial = 0
    nuevaCuenta = Cuenta(f"CU{idUsuario}", saldoInicial)
    nuevoCliente = Cliente(idUsuario, nombreUsuario, contraseña, nuevaCuenta)
    clientesRegistrados.append(nuevoCliente)
    print(f"Cliente '{nombreUsuario}' registrado con éxito.")

def iniciarSesionCliente():
    print("\n=== Inicio de Sesión Cliente ===")
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    for cliente in clientesRegistrados:
        if cliente.nombreUsuario == nombreUsuario and cliente.contraseña == contraseña:
            print(f"¡Bienvenido, {nombreUsuario}!")
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
