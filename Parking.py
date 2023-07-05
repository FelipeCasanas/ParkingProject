
# Trabajo final (Fundamentos de programacion imperativa)
# Samuel Díaz Monedero cod: 2357726
# Felipe Casañas Castro cod: 2357679
# Parqueadero 


def modificarTarifas(tablaTarifasAutos, tablaTarifasMotos):
    repetir = True

    while repetir == True:
        tarifaAModificar = int(input("Que tarifa va a modificar?:\n\n1. Autos\n2. Motos\n3. Atras\n\n"))

        if tarifaAModificar == 1:
            if tablaTarifasAutos[1] == -1:
                print("La tarifa no ha sido definida previamente")
                repetir = True
            else:
                nuevaTarifaAuto = int(input("Ingrese la nueva tarifa para Autos: "))
                tablaTarifasAutos[1] = nuevaTarifaAuto
                print("Tarifa actualizada correctamente")
                repetir = False

        elif tarifaAModificar == 2:
            if tablaTarifasMotos[1] == -1:
                print("La tarifa no ha sido definida previamente")
                repetir = True
            else:
                nuevaTarifaMoto = int(input("Ingrese la nueva tarifa para Motos: "))
                tablaTarifasMotos[1] = nuevaTarifaMoto
                print("Tarifa actualizada correctamente")
                repetir = False

        elif tarifaAModificar == 3:
            operarTarifa(tablaTarifasAutos, tablaTarifasMotos)

        else:
            print("La opcion no existe, intentelo de nuevo")
            repetir = True


def operarTarifa(tablaTarifasAutos, tablaTarifasMotos):

    accionARealizar = int(input("Que accion desea realizar?: \n\n1. Ingresar tarifas\n2. Mostrar tarifas\n3. Modificar tarifas\n4. Atras\n\n"))
    if accionARealizar == 1:

        tarifaAIngresar = int(input("Que tarifa va a ingresar?: \n\n1. Ingresar tarifa automovil\n2. Ingresar tarifa moto\n3. Regresar a tarifas\n\n"))
        if tarifaAIngresar == 1:
            

            if tablaTarifasAutos[1] != -1:
                    print("La tarifa para autos ya fue establecida")
            else:
                valido = False
                    
                while valido == False:
                    nuevaTarifa = int(input("Ingresa el valor a cobrar por minuto para autos: "))

                    if nuevaTarifa < 0:
                        print("La tarifa debe ser igual o mayor a 0")
                        valido = False
                    else:
                        tablaTarifasAutos[1] = nuevaTarifa
                        valido = True
        
        elif tarifaAIngresar == 2:
        

            if tablaTarifasMotos[1] != -1:
                    print("La tarifa para motos ya fue establecida")
            else:
                valido = False
                    
                while valido == False:
                    nuevaTarifa = int(input("Ingresa el valor a cobrar por minuto para motos: "))

                    if nuevaTarifa < 0:
                        print("La tarifa debe ser igual o mayor a 0")
                        valido = False
                    else:
                        tablaTarifasMotos[1] = nuevaTarifa
                        valido = True
        
        elif tarifaAIngresar == 3:
            #PENDIENTE
            #Devuelve al menu anterior, Tarifa para que tipo de vehiculo
            print("Devuelve al menu anterior")


    elif accionARealizar == 2:
        tarifasEstablecidas = 0

        if tablaTarifasAutos[1] == -1:
            print("La tarifa para autos no se ha establecido")
        else:
            tarifasEstablecidas += 1
            
        if tablaTarifasMotos[1] == -1:
            print("La tarifa para motos no se ha establecido")
        else:
            tarifasEstablecidas += 1

        if tarifasEstablecidas == 2:
            print(f"Tarifas: \n1. Autos: {tablaTarifasAutos[1]}\n2. Motos: {tablaTarifasMotos[1]}")
            tarifasEstablecidas = 0


    elif accionARealizar == 3:
        modificarTarifas(tablaTarifasAutos, tablaTarifasMotos )

        # Pendiente modificar tarifas
    elif accionARealizar == 4:
        home()
    else:
        print("La opcion no existe")
        operarTarifa(tablaTarifasAutos, tablaTarifasMotos)


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
    tablaTarifasAutos = ["Autos", -1]
    tablaTarifasMotos = ["Motos", -1]

    # Se crea variable y se inicia bucle que continua mientras valido = false
    # Se valida que numero ingresado este entre el rango. Si lo es, valido = true y pasa al metodo indicado por opcion.
    # Si no, se repite el bucle
    valido = False

    while valido == False:
        opcion = int(input("\nIngrese una opcion: \n\n1. tarifas\n2. Ingresar vehiculo\n3. Buscar vehiculo\n4. Mostrar registros\n5. Salida de vehiculo\n6. Buscar factura\n7. Cuadre de caja\n8. Salir\n\n"))
        if (opcion < 1 and opcion > 8):
            valido == False
            print("La opcion seleccionada no existe")
        else:
            valido == True

            if opcion == 1:
                operarTarifa(tablaTarifasAutos, tablaTarifasMotos)
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


home()