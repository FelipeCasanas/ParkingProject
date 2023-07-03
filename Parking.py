tablaTarifas = []
vehiculos = []


def tarifas():
    opcion = int(input(
        "Que accion desea realizar?: \n\n1. Ingresar tarifas\n2. Mostrar tarifas\n3. Modificar tarifas\n4. Atras"))
    if opcion == 1:
        accionTarifa = int(input("Que tarifa va a ingresar?: \n\n1. Ingresar tarifa automovil\n2. Ingresar tarifa moto\n3. Regresar a tarifas"))

        if accionTarifa == 1:
            print()
            # Pendiente
        elif accionTarifa == 2:
            print()
            # Pendiente
        elif accionTarifa == 3:
            print()
            # Pendiente

    elif opcion == 2:
        print()
        # Pendiente mostrar tarifa
    elif opcion == 3:
        print()
        # Pendiente modificar tarifas
    elif opcion == 4:
        home()
    else:
        print("La opcion no existe")
        tarifas()


def ingresarVehiculo():
    print("")


def buscarVehiculo():
    print("")


def mostrarRegistros():
    print("")


def salidaVehiculo():
    print("")


def buscarFactura():
    print("")


def cuadreCaja():
    print("")


def home():

    # Se crea variable y se inicia bucle que continua mientras valido = false
    # Se valida que numero ingresado este entre el rango. Si lo es, valido = true y pasa al metodo indicado por opcion.
    # Si no, se repite el bucle
    valido = False

    while valido == False:
        opcion = int(input("Ingrese una opcion: \n\n1. tarifas\n2. Ingresar vehiculo\n3. Buscar vehiculo\n4. Mostrar registros\n5. Salida de vehiculo\n6. Buscar factura\n7. Cuadre de caja\n8. Salir"))
        if (opcion < 1 and opcion > 8):
            valido == False
        else:
            valido == True

            if opcion == 1:
                tarifas()
            elif opcion == 2:
                ingresarVehiculo()
            elif opcion == 3:
                buscarVehiculo()
            elif opcion == 4:
                mostrarRegistros()
            elif opcion == 5:
                salidaVehiculo()
            elif opcion == 6:
                buscarFactura()
            elif opcion == 7:
                cuadreCaja()
            elif opcion == 8:
                # Se cierra el programa
                exit()
