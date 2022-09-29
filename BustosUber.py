import datetime
fecha_actual = datetime.datetime.now()
print(fecha_actual.strftime('%d/%m/%y %H:%M:%S \n'))
print("Hola bienvenido a UBER, vamos a comenzar con unas consultas para empezar.\n ")
consulta1 = int(input("Presione 1 para REGISTRARSE(CAMPO OBLIGATORIO):"))
while (consulta1 > 1 or consulta1 < 1):
    consulta1 = int(input("ERROR, ingrese numero adecuado. "))
if (consulta1 == 1):
    nombre = input(("Ingrese su nombre: "))
    apellido = input(("Ingrese su apellido: "))
    rut = input(("Ingrese su RUT: "))
    Fecha_nac = input(("Ingrese su fecha de nacimiento: "))
    telefono = int(input(("Ingrese su telefono: ")))
    Correo = input(("Ingrese su correo electronico: "))
    consulta1 = 0
    consulta1 = int(input("\n Usted se ha registrado con exito.\n \n Presione:\n 1.Para TERMINAR. \n 2.Presione 2 para COMENZAR CARRERA.\n "))
    while (consulta1 > 2 or consulta1 < 1):
        consulta1 = int(input("ERROR, ingrese nuevamente el numero. "))
    if (consulta1 == 1):
            print("Usted a SALIDO de la aplicacion.")
    if (consulta1 == 2):
            print("\n Usted a comenzado una carrera.\n") 
            print("Bienvenido Don", nombre, apellido, "\n")
            latitud = float(input("Inserte coordenadas 'x' de destinacion: "))
            print("Latitud de(x): ", latitud, "\n")
            longitud = float(input("Inserte coordenas 'y' de destinacion: "))
            print("Longitud de(y): ", longitud, "\n")
            boton = int(input("Presione segun la accion que desea realizar:\n 1.ENCENDER VEHICULO \n 2.APAGAR VEHICULO\n"))
            if (boton == 1):
                print("\n Acaba de ENCENDER el vehiculo. \n")
            if (boton == 2):
                print("Acaba de APAGAR el vehiculo")
if (boton == 1):
    print("Bienvenido a la navegacion por UBER. \n")
    print("Nuestra tarifa es de 64 pesos por cada METRO RECORRIDO. \n")
    print("LEER ATENTAMENTE Y TENER PRECAUCION EN CADA ACCION QUE REALIZA.\n")
accion = int(input("'Entrara al sistema de acciones de vehiculo'. PRESIONE:\n 1.PARA ACEPTAR\n 2.PARA RECHAZAR \n"))
if (accion == 1):
    km=0  
    boton2=0 
    M=0
    distancia=0
    tarifa=0
    X = 0
    Y= 0
    while (X != longitud) or (Y != latitud): 
        print("Usted esta en el eje X (",X,") de (",longitud,")")  
        print("Escoga una opcion. \n")
        print("1.ACELERAR 10KM/H(2.7M/S)")
        print("2.GIRAR.")
        print("3.SEGUIR AVANZANDO.", "(",distancia,")", "Metros")
        print("4.DETENER Y APAGAR VEHICULO.")
        boton2 = int(input("¿Que accion desea realizar?\n"))
        if (boton2 == 1):
           km=(km+10)
           M=(M+2.7)
           distancia=(km*M)
           tarifa=(64*distancia)
           print("\n acaba de ACELERAR 10 KM/H. su VELOCIDAD PASO A:", km,"KM/H",M,"M/S \n")
        if (boton2 == 2):
            boton2 = 0
            print("Se realizo UN GIRO. \n")
            while (boton2 != 2) and (boton2 !=4):
                    print("Usted esta en el eje Y (",Y,") de (",latitud,")" )
                    print("Escoga una opcion. \n")
                    print("1.ACELERAR 10KM/H(2.7M/S)")
                    print("2.GIRAR")
                    print("3.SEGUIR AVANZANDO.", "(",distancia,")", "Metros")
                    print("4.DETENER Y APAGAR VEHICULO.")
                    boton2 = int(input("¿Que accion desea realizar?\n"))
                    if (boton2 == 1):
                        km=(km+10)
                        M=(M+2.7)
                        distancia=(km*M)
                        tarifa=(64*distancia)
                        print("\n acaba de ACELERAR 10 KM/H. su VELOCIDAD PASO A:", km,"KM/H",M,"M/S \n")
                    if (boton2 == 3):
                        print("Presiono SEGUIR AVANZANDO. \n")
                        distancia=distancia+(km*M)
                        tarifa=tarifa+(64*distancia)
                        Y = distancia
                    if (boton2 == 4):
                        km=0
                        M=0
                        print("se DETENDRA Y APAGARA el vehiculo.")
                    Y = 0 if Y < 0 else latitud if Y > latitud else Y
        if (boton2 == 3):
            print("Presiono SEGUIR AVANZANDO. \n")
            distancia=distancia+(km*M)
            tarifa=tarifa+(64*distancia)
            X = distancia
        if (boton2 == 4):
            km=0
            M=0
            print("se DETENDRA Y APAGARA el vehiculo.")
        X = 0 if X < 0 else longitud if X > longitud else X
    print("HA LLEGADO A SU DESTINO, ESPERO UN MOMENTO.")
    print("Que tenga un buen dia.\n")
    print("Coordenadas: ", "x",latitud, "y", longitud)
    print("DISTANCIA recorrida:", distancia)
    print("TARIFA:", tarifa)
    print("Velocidad ACTUAL es de:", km,"KM/H", M,"M/S")
if (accion == 2):
    print("Usted a salido del sistema de aaciones del vehiculo. \n FIN")  