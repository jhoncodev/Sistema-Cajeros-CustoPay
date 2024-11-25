def menuPrincipal():
    while True:
        print("\n=== Cajero multifuncional CustoPay ===\n")
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

# Menu del Administrador
def menuAdministrador():
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionarAdministrador()
        elif opcion == "2":
            registrarAdministrador()
        elif opcion == "3":
            return
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

def registrarAdministrador():
    print("\nFunción para registrar un administrador...")

# Menu del Cliente
def menuCliente():
    while True:
        print("\n=== Menú Cliente ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clienteCajeros()
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

# Funcionalidades del Cliente
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
    print("\nFunción para registrar un cliente...")

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
