
# Trabajo final (Fundamentos de programacion imperativa)
# Samuel Díaz Monedero cod: 2357726
# Felipe Casañas Castro cod: 2357679
# Parqueadero 


# Aca se encuentra los vectores y matrices que necesita el programa
# Tambien el menu principal que ve el usuario
def home():
    tablaTarifasAutos = ["Autos", -1]
    tablaTarifasMotos = ["Motos", -1]
    contadorFactura = 0
    registroVehiculos = [["Factura", "Placa", "Tipo Vehiculo", "Hora Ingreso", "Hora Salida", "Total Minutos", "Nombre", "Cobro"]]

    # Se crea variable y se inicia bucle que continua mientras valido = false
    # Se valida que numero ingresado este entre el rango. Si lo es, valido = true y pasa al metodo indicado por opcion.
    # Si no, se repite el bucle
    valido = False

    while valido == False:
        print("Menú Principal")
        print("1. tarifas")
        print("2. Ingresar vehiculo")
        print("3. Buscar vehiculo")
        print("4. Mostrar registros")
        print("5. Salida de vehiculo")
        print("6. Buscar factura")
        print("7. Cuadre de caja")
        print("8. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if (opcion < 1 and opcion > 8):
            valido == False
            print("La opcion seleccionada no existe")
        else:
            valido == True

            if opcion == 1:
                operarTarifa(tablaTarifasAutos, tablaTarifasMotos)
            elif opcion == 2:
                ingresarVehiculo(registroVehiculos, contadorFactura)
                contadorFactura += 1
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


def modificarTarifas(tablaTarifasAutos, tablaTarifasMotos):
    repetir = True

    # Pregunta a usuario que tarifa va a modificar, y valida si la tarifa ya ha sido definida por el metodo "operarTarifa", 
    # Si no ha sido definida dara un mensaje indicando eso y no dejara modificar la tarifa
    # Si ya fue definida dejara modificar la tarifa actual en la categoria de vehiculo seleccionada
    while repetir == True:
        print("Modificar Tarifas")
        print("1. Modificar Tarifa Automóvil")
        print("2. Modificar Tarifa Motocicleta")
        print("3. Regresar al subMenú Tarifas")
        tarifaAModificar = int(input("Ingrese una opcion: "))
        if tarifaAModificar == 1:
            if tablaTarifasAutos[1] == -1:
                print("La tarifa no ha sido definida previamente")
                repetir = True
            else:
                nuevaTarifaAuto = int(input("Ingrese la nueva tarifa para Automóvil: "))
                tablaTarifasAutos[1] = nuevaTarifaAuto
                print("Tarifa actualizada correctamente")
                repetir = False

        elif tarifaAModificar == 2:
            if tablaTarifasMotos[1] == -1:
                print("La tarifa no ha sido definida previamente")
                repetir = True
            else:
                nuevaTarifaMoto = int(input("Ingrese la nueva tarifa para Motocicleta: "))
                tablaTarifasMotos[1] = nuevaTarifaMoto
                print("Tarifa actualizada correctamente")
                repetir = False

        elif tarifaAModificar == 3:
            operarTarifa(tablaTarifasAutos, tablaTarifasMotos)

        else:
            print("La opcion seleccionada no existe")
            repetir = True


# Condicionales anidados para permitir el desplazamiento por la interfaz de tarifas del programa y en cada categoria tiene sus respectivas funciones
def operarTarifa(tablaTarifasAutos, tablaTarifasMotos):
    print("Tarifas")
    print("1. Ingresar tarifas")
    print("2. Mostrar tarifas")
    print("3. Modificar tarifas")
    print("4.  Regresar al Menú principal")
    accionARealizar = int(input("Ingrese una opcion: "))
    #Seccion de ingresar tarifas, aqui se ingresa el primer valor de tarifas al programa
    if accionARealizar == 1:

        # Se verifica si en la tabla ya fue definida la tarifa, si no ha sido definida entonces se ejecuta el if. 
        # Sino, se ejecuta el else y pide al usuario que establezca el valor de la tarifa
        # Tambien valida que la tarifa sea igual o mayor a 0
        # Esto aplica para opcion 1 y 2, opcion 3 solo nos devuelve al menu tarifas
        print("Ingresar Tarifas")
        print("1. Ingresar Tarifa de Automóvil")
        print("2. Ingresar Tarifa de Motocicleta")
        print("3. Regresar al subMenú Tarifas")
        tarifaAIngresar = int(input("Ingrese una opcion: "))
        if tarifaAIngresar == 1:
            
            if tablaTarifasAutos[1] != -1:
                    print("La tarifa para Automóvil ya fue establecida")
            else:
                valido = False
                    
                while valido == False:
                    nuevaTarifa = int(input("Ingresa el valor a cobrar por minuto para automóviles: "))

                    if nuevaTarifa < 0:
                        print("La tarifa debe ser igual o mayor a 0")
                        valido = False
                    else:
                        tablaTarifasAutos[1] = nuevaTarifa
                        valido = True

        elif tarifaAIngresar == 2:
        
            if tablaTarifasMotos[1] != -1:
                    print("La tarifa para Motocicleta ya fue establecida")
            else:
                valido = False
                    
                while valido == False:
                    nuevaTarifa = int(input("Ingresa el valor a cobrar por minuto para motocicletas: "))

                    if nuevaTarifa < 0:
                        print("La tarifa debe ser igual o mayor a 0")
                        valido = False
                    else:
                        tablaTarifasMotos[1] = nuevaTarifa
                        valido = True
        
        elif tarifaAIngresar == 3:
            operarTarifa()
            print("Regresa al subMenú Tarifas")

    # Seccion mostrar tarifas. primero, valida que ambas tarifas hayan sido definidas 
    # Usa un contador que debe ser igual a 2 para que muestre las tarifas.
    # Si alguna de ellas no ha sido defenida y lo imprimira
    # El usuario debera de definir ambos campos para que le muestre las tarifas
    elif accionARealizar == 2:
        tarifasEstablecidas = 0

        if tablaTarifasAutos[1] == -1:
            print("La tarifa para Automóvil no se ha establecido")
        else:
            tarifasEstablecidas += 1
            
        if tablaTarifasMotos[1] == -1:
            print("La tarifa para Motocicleta no se ha establecido")
        else:
            tarifasEstablecidas += 1

        if tarifasEstablecidas == 2:
            print(f"Tarifas: \n1. Autos: {tablaTarifasAutos[1]}\n2. Motos: {tablaTarifasMotos[1]}")
            tarifasEstablecidas = 0

    # Seccion modificar tarifas, nos envia al metodo modificarTarifas
    # El metodo recibe 2 parametros que son las 2 tablas de tarifas (tablaTarifasAutos, tablaTarifasMotos)
    elif accionARealizar == 3:
        modificarTarifas(tablaTarifasAutos, tablaTarifasMotos)

    # Seccion para volver al menu anterior
    # Llama al metodo home que nos devuelve al menu principal
    elif accionARealizar == 4:
        home()

    # Se ejecuta esta opcion en caso de que el usuario escoja una opcion que no existe
    else:
        print("La opcion seleccionada no existe")
        operarTarifa(tablaTarifasAutos, tablaTarifasMotos)


# Registra los vehiculos que entran
# Se crea arreglo que se llena con lso datos requeridos
# Se pide ingresar el tipo de vehiculo, luego en base a eso se determina el formato de la placa y se pide al usuario
# Se comprueba que la placa ingresada cumpla con el formato
def ingresarVehiculo(registroVehiculos, contadorFactura):
    nuevoIngreso = []
    validar = False
    while validar == False:
        tipoVehiculo = input("Ingrese el tipo de vehículo:\n\na: Automóvil\nm: Motocicleta\n")

        if tipoVehiculo == "a":
            tipoVehiculo = "Automovil"
                
            valido = False
            while valido == False:
                placa = input("Ingrese la placa del auto en formato: AAA111: \n")

                # Se valida que placa tenga 6 caracteres
                # Se separa entre letras y numeros para tarbajarlas mas facilmente
                # Se valida que el numero de la placa este entre 000 y 999
                # Se emplea try except en caso de que ingresen tipos de datos incorrectos
                if len(placa) == 6:
                    try:
                        letrasPlaca = placa[0] + placa[1] + placa[2]
                        numeroPlaca = placa[3] + placa[4] + placa[5]
                        placaCompleta = letrasPlaca + numeroPlaca
                        numeroPlaca = int(numeroPlaca)

                        if numeroPlaca >= 0 and numeroPlaca < 1000:
                            nuevoIngreso.append(contadorFactura)
                            nuevoIngreso.append(placaCompleta)
                            nuevoIngreso.append(tipoVehiculo)
                            valido = True
                    
                    except:
                        print("El tipo de dato ingresado no es valido")

                else:
                    print("El formato de la placa ingresado es invalido")      
                    valido = False

            validar = True

        elif tipoVehiculo == "m":
            tipoVehiculo = "Motocicleta"

            valido = False
            while valido == False:
                placa = input("Ingrese la placa del auto en formato: AAA11A: \n")

                # Se valida que placa tenga 6 caracteres
                # Se separa entre letras y numeros para tarbajarlas mas facilmente
                # Se valida que el numero de la placa este entre 00 y 99
                # Se emplea try except en caso de que ingresen tipos de datos incorrectos
                if len(placa) == 6:
                    try:
                        letrasPlaca = placa[0] + placa[1] + placa[2]
                        numeroPlaca = placa[3] + placa[4]
                        ultimaLetra = placa[5]
                        placaCompleta = letrasPlaca + numeroPlaca + ultimaLetra
                        numeroPlaca = int(numeroPlaca)

                        if numeroPlaca >= 0 and numeroPlaca < 100:
                            nuevoIngreso.append(contadorFactura)
                            nuevoIngreso.append(placaCompleta)
                            nuevoIngreso.append(tipoVehiculo)
                            valido = True
                    
                    except:
                        print("El tipo de dato ingresado no es valido")

                else:
                    print("El formato de la placa ingresado es invalido")      
                    valido = False

            validar = True 
        else:
            print("El tipo de vehiculo no existe")
            validar = False
        
        # Se pide ingresar la hora de entrada del vehiculo en formato 24 horas
        # Se extrae las horas y minutos y se valida que no sobrepasen las 24 horas
        # Se añade la hora completa al arreglo "nuevoIngreso"
        validando = False
        while validando == False:
            horaEntrada = int(input("Ingrese la hora de ingreso en formato de 24 horas: hhmm\n"))
            horas=horaEntrada//100
            min=horaEntrada%100

            if horas > 23:
                print("Las horas no pueden superar las 23 Horas")
                validando = False
            else:
                if min > 59:
                    print("Los minutos no pueden superar los 59 Minutos")
                    validando = False
                else:
                    nuevoIngreso.append(horaEntrada)
                    validando = True

    # Se pide nombre del cliente y se añade a "nuevoIngreso" 
    nombre = input("Ingrese el nombre del cliente:\n").lower
    nuevoIngreso.append(nombre) 

    # for i in range(0, len(nuevoIngreso)):
    #     print(nuevoIngreso[i])

    # registroVehiculos
    

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


home()