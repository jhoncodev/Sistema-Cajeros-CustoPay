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

class Cliente(Usuario):
    def __init__(self, idUsuario, nombre, nombreUsuario, contraseña, cuenta):
        super().__init__(idUsuario, nombre, nombreUsuario, contraseña)
        self.cuenta = cuenta

class Cuenta:
    def __init__(self, idCuenta, saldo=0):
        self.idCuenta = idCuenta
        self.saldo = saldo
        self.movimientos = []

    def depositar(self, monto, tipo):
        self.saldo += monto
        self.registrarMovimiento(monto, tipo)

    def retirar(self, monto, tipo, registrar=True):
        if monto > self.saldo:
            return False
        self.saldo -= monto
        if registrar:    
            self.registrarMovimiento(-monto, tipo)
        return True

    def registrarMovimiento(self, monto, tipo, detalle=None):
        movimiento = Movimiento(monto, tipo, detalle)
        self.movimientos.append(movimiento)

class Movimiento:
    def __init__(self, monto, tipo, detalle=None):
        self.monto = monto
        self.tipo = tipo
        self.detalle = detalle or "Sin detalles"
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.fecha} - {self.tipo}: {self.monto} (Cajero: {self.cajero}) {self.detalle}"

class Cajero:
    def __init__(self, idCajero, region):
        self.idCajero = idCajero
        self.region = region
        self.billetes = {200: 0, 100: 0, 50: 0, 20: 0}
        self.estado = "Activo"
            
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

def menuAdministrador():
    while True:
        print("\n=== Menú Administrador ===\n")
        print("[1]. Iniciar sesión")
        print("[2]. Registrarse")
        print("[3]. Cambiar contraseña")
        print("[4]. Volver atrás\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciarSesionAdministrador()
        elif opcion == "2":
            registrarAdministrador()
        elif opcion == "3":
            cambiarContraseña(administradoresRegistrados)
        elif opcion == "4":
            return
        else:
            print("Opción inválida. Intente nuevamente.")
            
def cambiarContraseña(listaUsuarios):
    print("\n=== Cambiar Contraseña ===")

    while True:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        if nombreUsuario:
            break
        print("El nombre de usuario no puede estar vacío. Inténtelo nuevamente.")

    while True:
        contraseñaActual = input("Ingrese su contraseña actual: ").strip()
        if contraseñaActual:
            break
        print("La contraseña no puede estar vacía. Inténtelo nuevamente.")

    for usuario in listaUsuarios:
        if usuario.nombreUsuario == nombreUsuario and usuario.contraseña == contraseñaActual:
            while True:
                nuevaContraseña = input("Ingrese la nueva contraseña: ").strip()
                confirmarContraseña = input("Confirme la nueva contraseña: ").strip()

                if not nuevaContraseña:
                    print("La nueva contraseña no puede estar vacía. Inténtelo nuevamente.")
                elif nuevaContraseña != confirmarContraseña:
                    print("Las contraseñas no coinciden. Inténtelo nuevamente.")
                else:
                    usuario.contraseña = nuevaContraseña
                    print("Contraseña actualizada con éxito.")
                    return
    print("Credenciales incorrectas. Intente nuevamente.")

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
    
def gestionarAdministrador():
    while True:
        print("\n=== Opciones de Administrador ===")
        print("[1]. Gestionar Clientes")
        print("[2]. Gestionar Cajeros")
        print("[3]. Regresar")
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

def busquedaBinaria(lista, campo, valor):
    valor = valor.lower()
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        atributo = getattr(lista[medio], campo).lower()
        if atributo == valor:
            return medio
        elif atributo < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1 
 
def mostrarClientes():
    if not clientesRegistrados:
        print("No hay clientes registrados.")
        return False
    
    print(f"{'ID'.ljust(10)}{'Nombre'.ljust(20)}{'Usuario'.ljust(20)}{'Estado'.ljust(10)}")
    print("-" * 60)
    for cliente in clientesRegistrados:
        print(f"{str(cliente.idUsuario).ljust(10)}{cliente.nombre.ljust(20)}{cliente.nombreUsuario.ljust(20)}{cliente.estado.ljust(10)}")
    
    return True
    
def modificarCliente():
    print("\n=== Modificar Cliente ===")
    
    if not mostrarClientes():
        return

    clientesOrdenados = quickSort(clientesRegistrados, 'nombreUsuario')
    
    nombre = input("\nIngrese el nombre de usuario del cliente: ").strip()

    indice = busquedaBinaria(clientesOrdenados, 'nombreUsuario', nombre)
    if indice != -1:
        cliente = clientesOrdenados[indice]
        nuevoNombreUsuario = input("Ingrese el nuevo nombre de usuario (deje vacío para no cambiar): ")
        nuevaContraseña = input("Ingrese la nueva contraseña (deje vacío para no cambiar): ")

        if nuevoNombreUsuario:
            cliente.nombreUsuario = nuevoNombreUsuario
        if nuevaContraseña:
            cliente.contraseña = nuevaContraseña

        print("Cliente modificado con éxito.")
    else:
        print(f"Cliente con nombre '{nombre}' no encontrado.")

def cambiarEstadoCliente():
    print("\n=== Cambiar Estado de Cuenta del Cliente ===")
    
    if not mostrarClientes():
        return

    clientesOrdenados = quickSort(clientesRegistrados, 'nombreUsuario')
    
    nombreUsuario = input("\nIngrese el nombre de usuario del cliente: ").strip()

    indice = busquedaBinaria(clientesOrdenados, 'nombreUsuario', nombreUsuario)
    if indice != -1:
        cliente = clientesOrdenados[indice]
        nuevoEstado = input("¿Activar o Dar de baja? (A/D): ").upper()
        if nuevoEstado == "A":
            if cliente.estado == "Activo":
                print("La cuenta del cliente ya está activa, no se realizan cambios")
            else:
                cliente.estado = 'Activo'
                print(f"Cuenta del cliente '{nombreUsuario}' activada.")
        elif nuevoEstado == "D":
            if cliente.estado == "Baja":
                print("La cuenta del cliente ya está dada de baja, no se realizan cambios")
            else:
                cliente.estado = 'Baja'
                print(f"Cuenta del cliente '{nombreUsuario}' dada de baja.")
        else:
            print("Opción inválida.")
            return
    else:
        print(f"Cliente con nombre de usuario '{nombreUsuario}' no encontrado.")

def consultarCliente():
    print("\n=== Consultar Cliente ===")
    
    if not mostrarClientes():
        return

    clientesOrdenados = quickSort(clientesRegistrados, 'nombreUsuario')
        
    nombreUsuario = input("\nIngrese el nombre de usuario del cliente: ").strip()

    indice = busquedaBinaria(clientesOrdenados, 'nombreUsuario', nombreUsuario)
    if indice != -1:
        cliente = clientesOrdenados[indice]
        print(f"ID: {cliente.idUsuario}")
        print(f"Nombre: {cliente.nombre}")
        print(f"Nombre de usuario: {cliente.nombreUsuario}")
        print(f"Saldo: {cliente.cuenta.saldo}")
        print(f"Estado: {cliente.estado}")
    else:
        print(f"Cliente con nombre de usuario '{nombreUsuario}' no encontrado.")

def quickSort(listaDesordenada, campo):
    if len(listaDesordenada) <= 1:
        return listaDesordenada
    pivote = listaDesordenada[len(listaDesordenada) // 2] 
    izquierda = [cliente for cliente in listaDesordenada if getattr(cliente, campo) < getattr(pivote, campo)]
    medio = [cliente for cliente in listaDesordenada if getattr(cliente, campo) == getattr(pivote, campo)]
    derecha = [cliente for cliente in listaDesordenada if getattr(cliente, campo) > getattr(pivote, campo)]
    return quickSort(izquierda, campo) + medio + quickSort(derecha, campo)

def listarClientes():
    print("\n=== Listar Clientes ===")
    if not clientesRegistrados:
        print("No hay clientes registrados.")
        return
    
    print("¿Cómo deseas ordenar la lista de clientes?")
    print("1. Ordenar por nombre")
    print("2. Ordenar por ID")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        clientesOrdenados = quickSort(clientesRegistrados, 'nombre')
    elif opcion == '2':
        clientesOrdenados = quickSort(clientesRegistrados, 'idUsuario')
    else:
        print("Opción no válida.")
        return -1

    print(f"{'ID'.ljust(10)}{'Nombre'.ljust(20)}{'Usuario'.ljust(20)}{'Estado'.ljust(10)}")
    print("-" * 60)
    
    for cliente in clientesOrdenados:
        print(f"{str(cliente.idUsuario).ljust(10)}{cliente.nombre.ljust(20)}{cliente.nombreUsuario.ljust(20)}{cliente.estado.ljust(10)}")

def registrarCliente():
    print("\n=== Registro de Cliente ===")
    
    while True:
        nombre = input("Ingresar el nombre: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío. Inténtelo nuevamente.")
    
    while True:
        nombreUsuario = input("Ingrese el nombre de usuario: ").strip()
        if not nombreUsuario:
            print("El nombre de usuario no puede estar vacío. Inténtelo nuevamente.")
        elif usuarioRegistrado(nombreUsuario):
            print("Nombre de usuario ya registrado en una cuenta. Ingrese otro nombre de usuario.")
        else:
            break
    
    while True:
        contraseña = input("Ingrese la contraseña: ").strip()
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

def mostrarCajeros():
    if not cajerosRegistrados:
        print("No hay cajeros registrados.")
        return False

    print(f"{'ID'.ljust(10)}{'Región'.ljust(15)}")
    print("-" * 25)
    for cajero in cajerosRegistrados:
        print(f"{str(cajero.idCajero).ljust(10)}{cajero.region.ljust(15)}")
    return True

def modificarCajero():
    print("\n=== Modificar Cajero ===")
    
    if not mostrarCajeros():
        return
    
    try:
        opcion = int(input("\nSeleccione un cajero por su id: "))
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

def cambiarEstadoCajero():
    print("\n=== Cambiar Estado del Cajero ===")
    
    if not mostrarCajeros():
        return

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
    
    if not mostrarCajeros():
        return

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
    
    print("Ordenar por: (1) ID o (2) Región")
    opcion = input("Seleccione el criterio de orden (1 o 2): ")
    print("")
    if opcion == "1":
        campo = "idCajero"
    elif opcion == "2":
        campo = "region"
    else:
        print("Opción inválida. Mostrando orden por defecto (ID).")
        campo = "idCajero"
        
    cajerosOrdenados = quickSort(cajerosRegistrados, campo)
    
    print(f"{'ID'.ljust(10)}{'Región'.ljust(15)}{'Estado'.ljust(20)}{'Billetes'.ljust(10)}")
    print("-" * 80)
       
    for cajero in cajerosOrdenados:
           print(f"{str(cajero.idCajero).ljust(10)}{cajero.region.ljust(15)}{cajero.estado.ljust(20)}{str(cajero.billetes).ljust(10)}")
        
def mostrarRegiones():
    print("\n=== Regiones Disponibles ===")
    print("[1]. Cajamarca")
    print("[2]. Lima")
    print("[3]. Loreto")
    print("[4]. Cuzco")
    print("[5]. Tacna")
    print("[6]. Piura")

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
        print("[1]. Iniciar sesión")
        print("[2]. Registrarse")
        print("[3]. Cambiar contraseña")
        print("[4]. Volver atrás\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciarSesionCliente()
        elif opcion == "2":
            registrarCliente()
        elif opcion == "3":
            cambiarContraseña(clientesRegistrados)
        elif opcion == "4":
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

def operacionesCliente(cajero, cliente):
    
    while True:
        print(f"\n=== Operaciones en Cajero ID {cajero.idCajero} - Región: {cajero.region} ===")
        print("[1]. Depositar")
        print("[2]. Retirar")
        print("[3]. Transferir")
        print("[4]. Pagar Servicios")
        print("[5]. Consultar Saldo")
        print("[6]. Consultar Movimientos")
        print("[7]. Volver atrás")
        opcion = input("Seleccione una operación: ")

        if opcion == "1":
            print()
            depositar(cajero, cliente)
        elif opcion == "2":
            print()
            retirar(cajero, cliente)
        elif opcion == "3":
            print()
            transferir(cliente)
        elif opcion == "4":
            print()
            pagarServicios(cliente)
        elif opcion == "5":
            print()
            consultarSaldo(cliente)
        elif opcion == "6":
            print()
            consultarMovimientos(cliente)
        elif opcion == "7":
            return
        else:
            print("Opción inválida. Intente nuevamente.")

def mostrarDesglose(desglose):
    print(f"{'Billete'.ljust(10)}{'Cantidad'.rjust(10)}")
    print("-" * 20)
    for billete, cantidad in sorted(desglose.items(), reverse=True):
        print(f"{str(billete).ljust(5)}{str(cantidad).rjust(10)}")

def depositar(cajero, cliente):
    print("=== Depósito ===")
    try:
        monto = int(input("Ingrese el monto a depositar: "))
        if monto <= 0:
            print("\033[1;31mDepósito fallido, el monto debe ser mayor a 0\033[0m")
            return

        print("Ingrese el desglose de billetes:")
        desglose = {}

        for denominacion in sorted(cajero.billetes.keys(), reverse=True):
            cantidad = int(input(f"Cantidad de billetes de {denominacion}: "))
            if cantidad < 0:
                print("\033[1;31mDepósito fallido, la cantidad de billetes no puede ser negativa.\033[0m")
                return
            desglose[denominacion] = cantidad

        montoDesglose = sum(denominacion * cantidad for denominacion, cantidad in desglose.items())
        if montoDesglose != monto:
            print("\033[1;31mDepósito fallido, el monto total del desglose no coincide con el monto ingresado.\033[0m")
            return

        cliente.cuenta.depositar(monto, "Depósito")
        for billete, cantidad in desglose.items():
            cajero.billetes[billete] += cantidad

        print("\033[1;34mDepósito exitoso.\033[0m")
        
    except ValueError:
        print("\033[1;31mEntrada no válida, ingresar un número entero.\033[0m")

def retirar(cajero, cliente):
    print("=== Retiro ===")
    try:
        monto = int(input("Ingrese el monto a retirar: "))
        if monto <= 0:
            print("\033[1;31mRetiro fallido, el monto debe ser mayor a 0\033[0m")
            return
        if monto > cliente.cuenta.saldo:
            print("\033[1;31mRetiro fallido, saldo insuficiente en la cuenta\033[0m")
            return

        desglose = desgloseBilletesDinamico(monto, list(cajero.billetes.keys()), cajero.billetes.copy())
        if not desglose:
            print("\033[1;31mRetiro fallido, el cajero no tiene suficientes billetes\033[0m")
            return

        for billete, cantidad in desglose.items():
            if cajero.billetes[billete] < cantidad:
                print(f"\033[1;31mRetiro fallido, no hay suficientes billetes de {billete}.\033[0m")
                return

        if cliente.cuenta.retirar(monto, "Retiro"):
            for billete, cantidad in desglose.items():
                cajero.billetes[billete] -= cantidad

            print("\033[1;34mRetiro exitoso.\033[0m")
            print("Desglose de billetes retirados:")
            mostrarDesglose(desglose)
        else:
            print("\033[1;31mRetiro fallido, saldo insuficiente.\033[0m")
    except ValueError:
        print("\033[1;31mEntrada no válida, ingresar un número entero.\033[0m")

def transferir(cliente):
    print("=== Transferencia ===")
    try:
        nombreDestino = input("Ingrese el nombre de usuario del destinatario: ").strip()
        clienteDestino = next((c for c in clientesRegistrados if c.nombreUsuario.lower() == nombreDestino.lower()), None)

        if not clienteDestino:
            print("\033[1;31mTransferencia fallida, el usuario ingresado no existe.\033[0m")
            return

        if clienteDestino.idUsuario == cliente.idUsuario:
            print("\033[1;31mTransferencia fallida, no puedes transferir dinero a tu propia cuenta.\033[0m")
            return

        monto = int(input("Ingrese el monto a transferir: "))
        if monto <= 0:
            print("\033[1;31mTransferencia fallida, el monto debe ser mayor a 0.\033[0m")
            return

        if cliente.cuenta.retirar(monto, "Transferencia", registrar=False):
            clienteDestino.cuenta.depositar(monto, "Transferencia")
            cliente.cuenta.registrarMovimiento(-monto, "Transferencia")

            print("\033[1;34mTransferencia exitosa.\033[0m")
        else:
            print("\033[1;31mTransferencia fallida, saldo insuficiente en la cuenta.\033[0m")
    except ValueError:
        print("\033[1;31mEntrada no válida, ingresar un número entero.\033[0m")

def pagarServicios(cliente):
    print("=== Pago de Servicios ===")
    servicios = {
        "1": "Agua",
        "2": "Luz",
        "3": "Internet",
        "4": "Cable"
    }

    print("Seleccione el servicio a pagar:")
    for clave, servicio in servicios.items():
        print(f"[{clave}]. {servicio}")

    opcion = input("Seleccione una opción: ").strip()
    if opcion not in servicios:
        print("\033[1;31mPago fallido, opción inválida.\033[0m")
        return

    servicio = servicios[opcion]
    try:
        monto = int(input(f"Ingrese el monto a pagar para el servicio de {servicio}: "))
        if monto <= 0:
            print("\033[1;31mPago fallido, el monto debe ser mayor a 0.\033[0m")
            return

        if cliente.cuenta.retirar(monto, "Pago de Servicios", registrar=False):
            cliente.cuenta.registrarMovimiento(-monto, "Pago de Servicios")
            
            print(f"\033[1;34mPago exitoso del servicio de {servicio}.\033[0m")
            
        else:
            print("\033[1;31mPago fallido, saldo insuficiente en la cuenta.\033[0m")
    except ValueError:
        print("\033[1;31mEntrada no válida, ingresar un número entero.\033[0m")

def consultarSaldo(cliente):
    print("=== Consulta de Saldo ===")
    print(f"Saldo actual: {cliente.cuenta.saldo}")

def consultarMovimientos(cliente):
    print("=== Consulta de Movimientos ===")
    if not cliente.cuenta.movimientos:
        print("No hay movimientos registrados.")
        return

    print(f"{'Fecha'.ljust(20)} {'Hora'.ljust(20)} {'Tipo'.ljust(10)} {'Monto'.rjust(15)}")
    print("-" * 80)

    for movimiento in cliente.cuenta.movimientos:
        fecha, hora = movimiento.fecha.split(" ")
        tipo = movimiento.tipo
        monto = f"{movimiento.monto:.2f}"

        if movimiento.monto < 0: 
            monto = f"\033[1;31m{monto}\033[0m"
        else:
            monto = f"\033[1;34m{monto}\033[0m"

        print(f"{fecha.ljust(20)} {hora.ljust(20)} {tipo.ljust(20)} {monto.rjust(15)}")



#------------------------------------------------------------------------------#
#Ejecución
menuPrincipal()