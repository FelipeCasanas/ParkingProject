
# Trabajo final (Fundamentos de programacion imperativa)
# Samuel Díaz Monedero cod: 2357726
# Felipe Casañas Castro cod: 2357679
# Parqueadero 


# Aca se encuentra los vectores y matrices que necesita el programa
# Tambien el menu principal que ve el usuario
def home():
    tablaTarifasAutos = ["Automovil", -1]
    tablaTarifasMotos = ["Motocicleta", -1]
    contadorFactura = 1

    registroVehiculos = [["Factura", "Placa", "Tipo Vehiculo", "Hora Ingreso", "Hora Salida", "Total Minutos", "Nombre", "Total a pagar"],]


    # Se crea variable y se inicia bucle que continua mientras valido = false
    # Se valida que numero ingresado este entre el rango. Si lo es, valido = true y pasa al metodo indicado por opcion.
    # Si no, se repite el bucle
    valido = False

    while valido == False:
        print("\nMenú Principal")
        print("1. tarifas")
        print("2. Ingresar vehiculo")
        print("3. Buscar vehiculo")
        print("4. Mostrar registros")
        print("5. Salida de vehiculo")
        print("6. Buscar factura")
        print("7. Cuadre de caja")
        print("8. Salir")

        opcion = int(input("\nIngrese una opcion: "))
        if (opcion < 1 and opcion > 8):
            valido == False
            print("La opcion seleccionada no existe")
        else:
            valido == True

            if opcion == 1:
                operarTarifa(tablaTarifasAutos, tablaTarifasMotos)
            elif opcion == 2:
                nuevoIngreso = ingresarVehiculo(registroVehiculos, contadorFactura)
                registroVehiculos.append(nuevoIngreso)
            elif opcion == 3:
                buscarVehiculo(registroVehiculos)
            elif opcion == 4:
                mostrarRegistros(registroVehiculos)
            elif opcion == 5:
                tiempoTranscurrido = salidaVehiculo(registroVehiculos)
                registroVehiculos[tiempoTranscurrido[0]][4].append(tiempoTranscurrido[1])
                totalAPagar = cobrototal(registroVehiculos, tiempoTranscurrido[0], tablaTarifasAutos, tablaTarifasMotos)
                registroVehiculos[tiempoTranscurrido[0]][7].append(totalAPagar)
            elif opcion == 6:
                buscarFactura(registroVehiculos)
            elif opcion == 7:
                cuadreCaja(registroVehiculos)
            elif opcion == 8:
                # Se cierra el programa
                exit()


# Calcula el tiempo que pasa desde que entra hasta que sale el vehiculo
# Es usado en el metodo salidaVehiculo
def calcularTiempoTranscurrido(registroVehiculos):
    for i in range (len(registroVehiculos)):
        horaEntrada = registroVehiculos[i][4]//100
        minutoEntrada = registroVehiculos[i][4]%100
        horaSalida = registroVehiculos[i][3]//100
        minutoEntrada = registroVehiculos[i][3]%100 
        
        if registroVehiculos[i][2] < registroVehiculos [i][3]:
            minutos = minutoEntrada + (60-min)
            if horaSalida + 1 == horaEntrada:
                minutos = minutos
                retorno = minutos
            else:
                horasm = horaEntrada - horaSalida - 1
                horasm1 = horasm * 60
                retorno = horasm1 + minutos        
        return retorno


# Recibe tabla, indice fila que viene de metodo salidaVehiculo y ambas tablas de tarifas
# Se define total a pagar en 0 y valido en False
# Mientras valido sea False se ejecutara en bucle seleccione una opcion, si la opcion seleccionada es incorrecta
# Multiplica tarifa por numero de minutos y lo guarda en total a pagar
# Retorna total a pagar
def cobrototal(registroVehiculos, indiceFila, tablaTarifasAutos, tablaTarifasMotos):
    totalAPagar = 0
    valido = False

    while valido == False:
        if registroVehiculos[indiceFila][2] == "Automovil":
            totalAPagar = tablaTarifasAutos[1] * registroVehiculos[indiceFila][4]
            valido = True
        elif registroVehiculos[indiceFila][2] == "Motocicleta":
            totalAPagar = tablaTarifasMotos[1] * registroVehiculos[indiceFila][4]
            valido = True
        else:
            print("La opcion no existe")
            valido = False
    return totalAPagar


def modificarTarifas(tablaTarifasAutos, tablaTarifasMotos):
    repetir = True

    # Pregunta a usuario que tarifa va a modificar, y valida si la tarifa ya ha sido definida por el metodo "operarTarifa", 
    # Si no ha sido definida dara un mensaje indicando eso y no dejara modificar la tarifa
    # Si ya fue definida dejara modificar la tarifa actual en la categoria de vehiculo seleccionada
    while repetir == True:
        print("\nModificar Tarifas")
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
    print("\nTarifas")
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
        print("\nSeleccione el vehiculo a asignar tarifas")
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
            tarifasEstablecidas = 0
            repetir = True
            
            while repetir == True:
                volver = input(f"Tarifas: \n1. Autos: {tablaTarifasAutos[1]}\n2. Motos: {tablaTarifasMotos[1]}\n3. Regresar a menu principal\n")
                if volver == 3:
                    operarTarifa(tablaTarifasAutos, tablaTarifasMotos)
                    repetir == False
                else:
                    print("No es posible ejecutar ese comando")
                    repetir == True

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
        tipoVehiculo = int(input("Ingrese el tipo de vehículo:\n1. Automóvil\n2. Motocicleta\n3. Volver\nOpcion: "))
        
        if tipoVehiculo == 1:
            tipoVehiculo = "Automovil"           
            valido = False

            while valido == False:
                placa = input("Ingrese la placa del auto en formato: AAA111: ")

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

                            # PENDIENTE
                            # Se crea bucle que busque en placa y pregunta si el vehiculo existe en la base de datos
                            # Si existe, valida que hora de salida sea diferente a -1
                            # Si hora de salida diferente a -1 se puede ingresar el vehiculo
                            # Si no, imprime mensaje que el vehiculo se encuentra en el parqueadero y no se puede volver a ingresar
                    
                    except:
                        print("El tipo de dato ingresado no es valido")

                else:
                    print("El formato de la placa ingresado es invalido")      
                    valido = False

            validar = True

        elif tipoVehiculo == 2:
            tipoVehiculo = "Motocicleta"

            valido = False
            while valido == False:
                placa = input("Ingrese la placa del auto en formato AAA11A: ")

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

                            # PENDIENTE
                            # Se crea bucle que busque en placa y pregunta si el vehiculo existe en la base de datos
                            # Si existe, valida que hora de salida sea diferente a -1
                            # Si hora de salida diferente a -1 se puede ingresar el vehiculo y termian el bucle
                            # Si no, imprime mensaje que el vehiculo se encuentra en el parqueadero y no se puede volver a ingresar

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

        elif tipoVehiculo == 3:
            home()
        else:
            print("La opcion no existe")
            validar = False
        
        # Se pide ingresar la hora de entrada del vehiculo en formato 24 horas
        # Se extrae las horas y minutos y se valida que no sobrepasen las 24 horas
        # Se añade la hora completa al arreglo "nuevoIngreso"
        validando = False
        while validando == False:
            horaEntrada = int(input("Ingrese la hora de ingreso en formato de 24 horas HHMM: "))

            if horaEntrada >= 0 and horaEntrada < 10000:
                horas = horaEntrada//100
                min = horaEntrada%100

                if horas > 23:
                    print("Las horas no pueden superar las 23 Horas")
                    validando = False
                else:
                    if min > 59:
                        print("Los minutos no pueden superar los 59 Minutos")
                        validando = False
                    else:
                        nuevoIngreso.append(horaEntrada)
                        nuevoIngreso.append(-1)
                        validando = True
            else:
                print("La hora no cumple con el formato HHMM")
                ingresarVehiculo(registroVehiculos, contadorFactura)

    # Se pide nombre del cliente y se añade a "nuevoIngreso" 
    nombre = input("Ingrese el nombre del cliente: ")
    nuevoIngreso.append(nombre) 
    nuevoIngreso.append(0)
    nuevoIngreso.append(0)
    contadorFactura += 1
    return nuevoIngreso


def buscarVehiculo(registroVehiculos):
    validar = False
    while validar == False:
        print("Buscar vehiculo: ")
        print("1. Buscar motos")
        print("2. Buscar automoviles")
        print("3. Regresar al menu principal")
        buscarTipoVehiculo = int(input())

        if buscarTipoVehiculo == 1:
            numeroPlaca = input("Ingrese la placa de la moto: \n")
            vehiculoEncontrado = False

            for i in range(1, len(registroVehiculos)):
                if registroVehiculos[i][2] == "Motocicleta":
                        if numeroPlaca == registroVehiculos[i][1]:
                            print("Factura No: ", registroVehiculos[i][0])
                            print("Placa: ", registroVehiculos[i][1])
                            print("Tipo vehiculo: ", registroVehiculos[i][2])
                            print("Hora de Ingreso: ", registroVehiculos[i][3])
                            print("Hora de Salida: ", registroVehiculos[i][4])
                            print("Nombre: ", registroVehiculos[i][6])
                            print("Numero minutos: ", registroVehiculos[i][5])
                            print("Total: ", registroVehiculos[i][7])
                            print("")
                            vehiculoEncontrado = True

            if vehiculoEncontrado == False:
                print("Vehículo no encontrado\n")
            vehiculoEncontrado = False

        elif buscarTipoVehiculo == 2:
            numeroPlaca = input("Ingrese la placa del auto: \n")
            vehiculoEncontrado = False

            for i in range(1, len(registroVehiculos)):
                if registroVehiculos[i][2] == "Automovil":
                        if numeroPlaca == registroVehiculos[i][1]:
                            print("Factura No: ", registroVehiculos[i][0])
                            print("Placa: ", registroVehiculos[i][1])
                            print("Tipo vehiculo: ", registroVehiculos[i][2])
                            print("Hora de Ingreso: ", registroVehiculos[i][3])
                            print("Hora de Salida: ", registroVehiculos[i][4])
                            print("Nombre: ", registroVehiculos[i][5])
                            print("Numero minutos: ", registroVehiculos[i][6])
                            print("Total: ", registroVehiculos[i][7])
                            print("")
                            vehiculoEncontrado = True

            if vehiculoEncontrado == False:
                print("Vehículo no encontrado")
            vehiculoEncontrado = False
                    
        elif buscarTipoVehiculo == 3:
            home()
            validar == True
        else:
            print("La opcion no existe, intentelo de nuevo")


# Completo, pendiente de documentacion
def mostrarRegistros(registroVehiculos):
    validar = False
    while validar == False:
        print("1. Mostrar todos los automóviles.")
        print("2. Mostrar todas las motocicletas.")
        print("3. Regresar al menú principal.")
        mostrarRegistros = int(input("Ingrese una opcion: "))

        if mostrarRegistros == 1:
            print("\nTipo de busqueda: AUTOMOVIL")
            for fila in range(1, len(registroVehiculos)):
                if registroVehiculos[fila][2] == "Automovil":
                    print(registroVehiculos[fila][0], end="    ")
                    print(registroVehiculos[fila][1], end="    ")
                    print(registroVehiculos[fila][3], end="    ")
                    print(registroVehiculos[fila][4], end="    ")
                    print(registroVehiculos[fila][5], end="    ")
                    print(registroVehiculos[fila][7], end="    ")
                    print()
                    validar = True
        
        elif mostrarRegistros == 2:
            print("\nTipo de busqueda: MOTOCICLETA")
            for fila in range(1, len(registroVehiculos)):
                if registroVehiculos[fila][2] == "Motocicleta":
                    print(registroVehiculos[fila][0], end="    ")
                    print(registroVehiculos[fila][1], end="    ")
                    print(registroVehiculos[fila][3], end="    ")
                    print(registroVehiculos[fila][4], end="    ")
                    print(registroVehiculos[fila][5], end="    ")
                    print(registroVehiculos[fila][7], end="    ")
                    print()
                    validar = True

        elif mostrarRegistros == 3:
            validar = True
        
        else:
            print("La opcion ingresada no existe")
            validar = False
   

# Se crea variable coincidencia
# Se pide al usuario que ingrese el tipo de vehiculo
# Se pide al usuario que ingrese la placa del vehiculo
# Se hace bucle que recorra la tabla
# Se busca el tipo de vehiculo
# Se busca la placa del vehiculo en la tabla donde tipo de vehiculo coincide
# Si placa es igual a placaIngresada y hora salida es -1 
# Se pide al usuario la hora de salida del vehiculo
# Se le asigna la hora de salida 
# Incrementa coincidencia en 1
# Si coincidencia < 1 imprime el vehiculo no se encuentra en el parqueadero
def salidaVehiculo(registroVehiculos):
        
        #PENDIENTE

        # Se calcula el tiempo transcurrido desde la entrada hasta la salida del vehiculo
        # Se retorna indice de la coincidencia y tiempo transcurrido (En minutos)

        tiempoTranscurrido = []
        # tiempoTranscurrido.append(filas)
        tiempoTranscurrido.append(calcularTiempoTranscurrido(registroVehiculos))
        return tiempoTranscurrido


def buscarFactura(registroVehiculos):
    numeroFactura = int(input("Ingrese el numero de factura: "))
    print("")

    for i in range(1, len(registroVehiculos)):
        if registroVehiculos[i][0] == numeroFactura:
            for mostrarRegistro in range(0, 8):
                print(registroVehiculos[0][mostrarRegistro], end = ": ")
                print(registroVehiculos[i][mostrarRegistro])

    print("")

def cuadreCaja(registroVehiculos):
    totalVehiculos = 0; totalAutos = 0; totalMotos = 0

    for i in range(1, len(registroVehiculos)):
        if registroVehiculos[i][4] != -1:
            totalVehiculos += 1
            # ingresosTotales += registroVehiculos[i][7]
    print("Total de vehiculos: ", totalVehiculos)

    for i in range(1, len(registroVehiculos)):
        if registroVehiculos[i][2] == "Automovil":
            if registroVehiculos[i][4] != -1:
                totalAutos += 1
                # ingresosTotales += registroVehiculos[i][7]
    print("Total de automoviles: ", totalAutos)
        
    for i in range(1, len(registroVehiculos)):
        if registroVehiculos[i][2] == "Motocicleta":
            if registroVehiculos[i][4] != -1:
                totalMotos += 1
                # ingresosTotales += registroVehiculos[i][7]
    print("Total de motos: ", totalMotos)

home()