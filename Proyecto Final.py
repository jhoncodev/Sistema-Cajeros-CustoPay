#------------------------------------------------------------------------------#
# Librerias
from datetime import datetime
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
    def __init__(self, idCuenta, saldo=0):
        self.idCuenta = idCuenta
        self.saldo = saldo
        self.movimientos = []

    def depositar(self, monto, cajero_id):
        self.saldo += monto
        self.registrarMovimiento("Depósito", monto, cajero_id)

    def retirar(self, monto, cajero_id):
        if monto > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= monto
        self.registrarMovimiento("Retiro", -monto, cajero_id)
        return True

    def registrarMovimiento(self, tipo, monto, cajero_id):
        movimiento = Movimiento(tipo, monto, cajero_id)
        self.movimientos.append(movimiento)

class Movimiento:
    def __init__(self, tipo, monto, cajero):
        self.tipo = tipo
        self.monto = monto
        self.cajero = cajero
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.fecha} - {self.tipo}: {self.monto} (Cajero: {self.cajero})"

class Cajero:
    def __init__(self, idCajero, region):
        self.idCajero = idCajero
        self.region = region
        self.billetes = {200: 0, 100: 0, 50: 0, 20: 0}
        self.estado = "Activo"

    def agregarBilletes(self, denominacion, cantidad):
        if denominacion in self.billetes:
            self.billetes[denominacion] += cantidad
        else:
            print(f"Denominación {denominacion} no válida.")

    def cambiarEstado(self, nuevo_estado):
        if nuevo_estado in ["Activo", "Mantenimiento"]:
            self.estado = nuevo_estado
            print(f"Cajero {self.idCajero} en región '{self.region}' actualizado a estado: {self.estado}.")
        else:
            print("Estado no válido. Use 'Activo' o 'Mantenimiento'.")

#------------------------------------------------------------------------------#
# Listas
clientesRegistrados = []
administradoresRegistrados = []
cajerosRegistrados = []
#------------------------------------------------------------------------------#

# Menús y sub menús

def menuPrincipal():
    
    while True:
        print("\n=== Sistema de cajeros multifuncionales CustoPay ===\n")
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
    listarClientes()
    nombre = input("\nIngrese el nombre del cliente a modificar: ")
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
    listarClientes()
    nombreUsuario = input("\nIngrese el nombre de usuario del cliente: ")
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
    listarClientes()
    nombreUsuario = input("\nIngrese el nombre de usuario del cliente: ")
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
    
    while True:
        nombre = input("Ingresar su nombre: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío. Inténtelo nuevamente.")
    
    while True:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        if not nombreUsuario:
            print("El nombre de usuario no puede estar vacío. Inténtelo nuevamente.")
        elif usuarioRegistrado(nombreUsuario):
            print("Nombre de usuario ya registrado en una cuenta. Ingrese otro nombre de usuario.")
        else:
            break
    
    while True:
        contraseña = input("Ingrese su contraseña: ").strip()
        if contraseña:
            break
        print("La contraseña no puede estar vacía. Inténtelo nuevamente.")
    
    try:
        idUsuario = len(clientesRegistrados) + 1
        saldoInicial = 0
        nuevaCuenta = Cuenta(f"CU{idUsuario}", saldoInicial)
        nuevoCliente = Cliente(idUsuario, nombre, nombreUsuario, contraseña, nuevaCuenta)
        clientesRegistrados.append(nuevoCliente)
        print(f"Cliente '{nombreUsuario}' registrado con éxito.")
    except Exception as e:
        print(f"Error al registrar el cliente: {e}")

def registrarAdministrador():
    print("\n=== Registro de Administrador ===")
    
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío. Inténtelo nuevamente.")
    
    while True:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        if not nombreUsuario:
            print("El nombre de usuario no puede estar vacío. Inténtelo nuevamente.")
        elif usuarioRegistrado(nombreUsuario):
            print("Nombre de usuario ya registrado en una cuenta. Ingrese otro nombre de usuario.")
        else:
            break
    
    while True:
        contraseña = input("Ingrese su contraseña: ").strip()
        if contraseña:
            break
        print("La contraseña no puede estar vacía. Inténtelo nuevamente.")
    
    try:
        idUsuario = len(administradoresRegistrados) + 1
        nuevoAdmin = Administrador(idUsuario, nombre, nombreUsuario, contraseña)
        administradoresRegistrados.append(nuevoAdmin)
        print(f"Administrador '{nombre}' registrado con éxito.")
    except Exception as e:
        print(f"Error al registrar el administrador: {e}")

def usuarioRegistrado(nombreUsuario):
    for cliente in clientesRegistrados:
        if cliente.nombreUsuario == nombreUsuario:
            return True
        
    for administrador in administradoresRegistrados:
        if administrador.nombreUsuario == nombreUsuario:
            return True
    return False
    
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

def gestionarCajeros():
    while True:
        print("\n=== Gestión de Cajeros ===")
        print("[1]. Agregar Cajero")
        print("[2]. Modificar Cajero")
        print("[3]. Cambiar Estado del Cajero")
        print("[4]. Consultar Cajero")
        print("[5]. Listar Cajeros")
        print("[6]. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregarCajero()
        elif opcion == "2":
            modificarCajero()
        elif opcion == "3":
            cambiarEstadoCajero()
        elif opcion == "4":
            consultarCajero()
        elif opcion == "5":
            listarCajeros()
        elif opcion == "6":
            return
        else:
            print("Opción inválida. Intente nuevamente.")

def agregarCajero():
    print("\n=== Agregar Cajero ===")
    mostrarRegiones()
    opcionRegion = input("Seleccione una región para el nuevo cajero: ")
    
    regiones = {
        "1": "Cajamarca",
        "2": "Lima",
        "3": "Loreto",
        "4": "Cuzco",
        "5": "Tacna",
        "6": "Piura"
    }
    
    region = regiones.get(opcionRegion)
    if region:
        idCajero = len(cajerosRegistrados) + 1
        nuevoCajero = Cajero(idCajero, region)
        cajerosRegistrados.append(nuevoCajero)
        print(f"Cajero agregado con éxito: ID {idCajero}, Región {region}.")
    else:
        print("Opción inválida. Intente nuevamente.")

def modificarCajero():
    print("\n=== Modificar Cajero ===")

    if cajerosRegistrados:
        print("Seleccione el cajero que desea modificar:")
        for cajero in cajerosRegistrados:
            print(f"ID: {cajero.idCajero}, Región: {cajero.region}")
    
        try:
            opcion = int(input("Seleccione un cajero por número: "))
            if opcion < 1 or opcion > len(cajerosRegistrados):
                print("Opción inválida. Intente nuevamente.")
                return
            cajero = cajerosRegistrados[opcion - 1]
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
            return
    
    
        print("\n=== Regiones Disponibles ===")
        regiones = ["Cajamarca", "Lima", "Loreto", "Cuzco", "Tacna", "Piura"]
        for idx, region in enumerate(regiones, start=1):
            print(f"[{idx}]. {region}")
    
        try:
            opcionRegion = int(input(f"Seleccione la nueva región para el cajero {opcion}: "))
            if opcionRegion < 1 or opcionRegion > len(regiones):
                print("Opción inválida. Intente nuevamente.")
                return
            nuevaRegion = regiones[opcionRegion - 1]
            if nuevaRegion  == cajero.region:
                print("El cajero ya pertenece a esa región. No se realizaron cambios.")
            else:
                cajero.region = nuevaRegion 
                print(f"Cajero {cajero.idCajero} actualizado con nueva región: {nuevaRegion}.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
    else:
        print("No hay cajeros registrados")

def cambiarEstadoCajero():
    print("\n=== Cambiar Estado del Cajero ===")
    
    print("Cajeros disponibles:")
    for cajero in cajerosRegistrados:
        print(f"ID: {cajero.idCajero} | Región: {cajero.region} | Estado: {cajero.estado}")

    idCajero = input("\nIngrese el ID del cajero que desea gestionar: ").strip()
    for cajero in cajerosRegistrados:
        if str(cajero.idCajero) == idCajero:
            print(f"\nCajero seleccionado: ID {cajero.idCajero}, Región: {cajero.region}, Estado actual: {cajero.estado}")
            print("Seleccione el nuevo estado:")
            print("[1]. Activar")
            print("[2]. Colocar en Mantenimiento")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                if cajero.estado == "Activo":
                    print("El cajero ya está activo. No se realizaron cambios.")
                else:
                    cajero.estado = "Activo"
                    print(f"Cajero {cajero.idCajero} activado con éxito.")
            elif opcion == "2":
                if cajero.estado == "Mantenimiento":
                    print("El cajero ya está en mantenimiento. No se realizaron cambios.")
                else:
                    cajero.estado = "Mantenimiento"
                    print(f"Cajero {cajero.idCajero} colocado en mantenimiento con éxito.")
            else:
                print("Opción no válida. Intente nuevamente.")
            return
    print("ID de cajero no encontrado. Intente nuevamente.")

def consultarCajero():
    print("\n=== Consultar Cajero ===")
    print("Cajeros disponibles:")
    
    for cajero in cajerosRegistrados:
        print(f"ID: {cajero.idCajero} | Región: {cajero.region}")

    idCajero = input("\nIngrese el ID del cajero que desea consultar: ").strip()
    for cajero in cajerosRegistrados:
        if str(cajero.idCajero) == idCajero:
            
            print(f"\n=== Detalles del Cajero ID {cajero.idCajero} ===")
            print(f"ID: {cajero.idCajero}")
            print(f"Región: {cajero.region}")
            print(f"Estado: {cajero.estado}")
            print(f"Billetes: {cajero.billetes}")
            return
    print("ID de cajero no encontrado. Intente nuevamente.")

def listarCajeros():
    print("\n=== Listar Cajeros ===")
    if not cajerosRegistrados:
        print("No hay cajeros registrados.")
        return
    for cajero in cajerosRegistrados:
        print(f"ID: {cajero.idCajero} | Región: {cajero.region} | Estado: {cajero.estado} | Billetes: {cajero.billetes}")
        
def mostrarRegiones():
    print("\n=== Regiones Disponibles ===")
    print("[1]. Cajamarca")
    print("[2]. Lima")
    print("[3]. Loreto")
    print("[4]. Cuzco")
    print("[5]. Tacna")
    print("[6]. Piura")

def iniciarSesionAdministrador():
    print("\n=== Inicio de Sesión Administrador ===")
    
    while True:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        if nombreUsuario:
            break
        print("El nombre de usuario no puede estar vacío. Inténtelo nuevamente.")
    
    while True:
        contraseña = input("Ingrese su contraseña: ").strip()
        if contraseña:
            break
        print("La contraseña no puede estar vacía. Inténtelo nuevamente.")
    
    for admin in administradoresRegistrados:
        if admin.nombreUsuario == nombreUsuario and admin.contraseña == contraseña:
            print(f"¡Bienvenido, {admin.nombre}!")
            gestionarAdministrador()
            return
    print("Credenciales incorrectas. Intente nuevamente.")

def iniciarSesionCliente():
    print("\n=== Inicio de Sesión Cliente ===")
    
    while True:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        if nombreUsuario:
            break
        print("El nombre de usuario no puede estar vacío. Inténtelo nuevamente.")
    
    while True:
        contraseña = input("Ingrese su contraseña: ").strip()
        if contraseña:
            break
        print("La contraseña no puede estar vacía. Inténtelo nuevamente.")
    
    for cliente in clientesRegistrados:
        if cliente.nombreUsuario == nombreUsuario and cliente.contraseña == contraseña:
            if cliente.estado == "Baja":
                print("La cuenta está inactiva. Contacte al administrador.")
                return
            print(f"¡Bienvenido, {cliente.nombre}!")
            clienteCajeros(cliente)
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

def mostrarCajerosPorRegion(region):
    cajerosEnRegion = [cajero for cajero in cajerosRegistrados if cajero.region == region]
    if not cajerosEnRegion:
        print(f"No hay cajeros disponibles en la región {region}.")
        return None
    print(f"\n=== Cajeros Disponibles en Región: {region} ===")
    for cajero in cajerosEnRegion:
        print(f"ID: {cajero.idCajero} | Estado: {cajero.estado}")
    return cajerosEnRegion

def seleccionarCajeroEnRegion(cajerosEnRegion):
    idCajero = input("Ingrese el ID del cajero que desea utilizar: ")
    for cajero in cajerosEnRegion:
        if str(cajero.idCajero) == idCajero:
            if cajero.estado == "Activo":
                return cajero
            else:
                print("El cajero seleccionado está en mantenimiento. Intente con otro.")
                return None
    print("ID de cajero no válido. Intente nuevamente.")
    return None

def clienteCajeros(cliente):
    regiones = {
        "1": "Cajamarca",
        "2": "Lima",
        "3": "Loreto",
        "4": "Cuzco",
        "5": "Tacna",
        "6": "Piura"
    }

    while True:
        print("\n=== Seleccione Región Para Encontrar su Cajero ===")
        for clave, region in regiones.items():
            print(f"[{clave}]. {region}")
        print("[7]. Regresar")
        opcion = input("Seleccione una región: ")

        if opcion in regiones:
            region = regiones[opcion]
            cajerosEnRegion = mostrarCajerosPorRegion(region)
            if cajerosEnRegion:
                cajero = seleccionarCajeroEnRegion(cajerosEnRegion)
                if cajero:
                    operacionesCliente(cajero, cliente)
        elif opcion == "7":
            return
        else:
            print("Opción inválida. Intente nuevamente.")

def ordenarQuickSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        
        izquierda = [x for x in lista if x > pivote]
        centro = [x for x in lista if x == pivote]
        derecha = [x for x in lista if x < pivote]
        
        return ordenarQuickSort(izquierda) + centro + ordenarQuickSort(derecha)

def operacionesCliente(cajero, cliente):
    print(f"\n=== Operaciones en Cajero ID {cajero.idCajero} - Región: {cajero.region} ===")
    while True:
        print("1. Depositar")
        print("2. Retirar")
        print("3. Transferir")
        print("4. Pagar Servicios")
        print("5. Consultar Saldo")
        print("6. Consultar Movimientos")
        print("7. Volver atrás")
        opcion = input("Seleccione una operación: ")

        if opcion == "1":
            depositar(cajero, cliente)
            print()
        elif opcion == "2":
            print()
            retirar(cajero, cliente)
        elif opcion == "3":
            print("Aun no se desarrolla está función")
        elif opcion == "4":
            print("Aun no se desarrolla está función")
        elif opcion == "5":
            print("Aun no se desarrolla está función")
        elif opcion == "6":
            print("Aun no se desarrolla está función")
        elif opcion == "7":
            return
        else:
            print("Opción inválida. Intente nuevamente.")
            
def depositar(cajero, cliente):
    print("\n=== Depósito ===")
    try:
        monto = int(input("Ingrese el monto a depositar: "))
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return

        print("Ingrese el desglose de billetes:")
        desglose = {}

        for denominacion in sorted(cajero.billetes.keys(), reverse=True):
            cantidad = int(input(f"Cantidad de billetes de {denominacion}: "))
            if cantidad < 0:
                print("La cantidad de billetes no puede ser negativa.")
                return
            desglose[denominacion] = cantidad

        montoDesglose = sum(denominacion * cantidad for denominacion, cantidad in desglose.items())
        if montoDesglose != monto:
            print(f"El monto total del desglose ({montoDesglose}) no coincide con el monto ingresado ({monto}).")
            return

        cliente.cuenta.depositar(monto, cajero.idCajero)
        for billete, cantidad in desglose.items():
            cajero.billetes[billete] += cantidad
        print(f"Depósito exitoso. Nuevo saldo: {cliente.cuenta.saldo}")
        print(f"Desglose de billetes depositados: {desglose}")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")


def desgloseBilletesDinamico(monto, denominaciones, billetesDisponibles):
    denominaciones = sorted(denominaciones, reverse=True)
    desglose = {}
    montoActual = monto
    copiaBilletes = billetesDisponibles.copy()

    for denominacion in denominaciones:
        cantidadNecesaria = montoActual // denominacion
        cantidadDisponible = copiaBilletes[denominacion]
        cantidadAUsar = min(cantidadNecesaria, cantidadDisponible)

        if cantidadAUsar > 0:
            desglose[denominacion] = cantidadAUsar
            montoActual -= cantidadAUsar * denominacion

    if montoActual != 0:
        return None
    return desglose

def retirar(cajero, cliente):
    print("\n=== Retiro ===")
    try:
        monto = int(input("Ingrese el monto a retirar: "))
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return
        if monto > cliente.cuenta.saldo:
            print("Saldo insuficiente en la cuenta.")
            return

        desglose = desgloseBilletesDinamico(monto, list(cajero.billetes.keys()), cajero.billetes.copy())
        if not desglose:
            print("El cajero no tiene suficientes billetes para completar esta transacción.")
            return

        # Actualizamos el saldo del cliente y los billetes del cajero
        cliente.cuenta.retirar(monto, cajero.idCajero)
        for billete, cantidad in desglose.items():
            cajero.billetes[billete] -= cantidad
        print(f"Retiro exitoso. Nuevo saldo: {cliente.cuenta.saldo}")
        print(f"Desglose de billetes entregados: {desglose}")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")



#------------------------------------------------------------------------------#

menuPrincipal()
