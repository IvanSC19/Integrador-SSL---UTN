from tadPaciente import*
from datetime import*
from tadHosp import*
from tadCola import*
from base_datos import*

import os

hosp=crear_hospital()
carga_pacientes(hosp)

def modificarPrioridad():
    nomPac = input("Introducir nombre del paciente a modificar prioridad: ")
    encontrado = i = 0
    while i <= cantidad_pacientes(hosp) and encontrado == 0:
        paciente = recuperar_paciente(hosp, i)
        if ver_nom(paciente) == nomPac:
            prioridad_nueva = input(" Ingrese la nueva prioridad: ")
            modificar_prioridad_paciente(hosp, paciente, prioridad_nueva)
            print("La prioridad fue cargada correctamente. ")
            encontrado = 1
            os.system("pause")
            os.system("cls")
        else:
            i+=1
    if encontrado == 0:
        print('-', '\nEl nombre', nomPac,  'no existe, intentelo nuevamente\n', '-')
        resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
        if(resp=="s"):
            return modificarPrioridad()
		
def modificarConsulta():
    nomPac = input("Introducir nombre del paciente a modificar tipo de consulta")
    encontrado = i = 0
    while i <= cantidad_pacientes(hosp) and encontrado == 0:
        paciente = recuperar_paciente(hosp, i)
        if ver_nom(paciente) == nomPac:
           consulta_nueva = input(" Nueva consulta: ")
           modif_consulta(paciente, consulta_nueva)
           os.system("cls")
           print("Modificacion exitosa")
           encontrado = 1
           os.system("pause")
           os.system("cls")
        else:
            i+=1
    if encontrado == 0:
        print('-', '\nEl nombre', nomPac,  'no existe, intentelo nuevamente\n', '-')
        resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
        if(resp=="s"):
            return modificarConsulta()

def modificarEdad():
    nomPac = input("Introducir nombre del paciente a modificar edad")
    encontrado = i = 0
    while i <= cantidad_pacientes(hosp) and encontrado == 0:
        paciente = recuperar_paciente(hosp, i)
        if ver_nom(paciente) == nomPac:
            edad_nueva = input(" Nueva edad: ")
            modif_edad(paciente, edad_nueva)
            os.system("cls")
            print("Modificacion exitosa")
            encontrado = 1
            os.system("pause")
            os.system("cls")
        else:
            i+=1
    if encontrado == 0:
        print('-', '\nEl nombre', nomPac,  'no existe, intentelo nuevamente\n', '-')
        resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
        if(resp=="s"):
            return modificarEdad()
		
def modificarFecha():
	nomPac = input("Ingrese nombre del paciente a modificar su fecha: ")
	encontrado = i = 0
	while i <= cantidad_pacientes(hosp) and encontrado == 0:
		paciente = recuperar_paciente(hosp, i)
		if ver_nom(paciente) == nomPac:
			print("Introducir nueva fecha: ")
			fecha_nueva = validacionFecha()
			modif_fecha(paciente, fecha_nueva)
			print("Introducir nueva hora: ")
			hora_nueva = validacionHora()
			modif_hora(paciente, hora_nueva)
			os.system("cls")
			print("Modificacion realizada con exito. ")
			encontrado = 1
			os.system("pause")
			os.system("cls")
		else:
			i+=1
	if encontrado == 0:
		print('-', '\nEl nombre', nomPac,  'no existe, intentelo nuevamente\n', '-')
		resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
		if(resp=="s"):
			return modificarFecha()
		

def modificacionPaciente(hosp):
	os.system("cls")
	if cantidad_pacientes(hosp)==0:
		print("No hay pacientes para modificar")
		os.system("pauses")
		os.system("cls")
	else:
		menu = 0
		while menu != 6:
			print("---Modificar Pacientes---")
			print("-Opcion 1: Modificar Nombre de paciente")
			print("-Opcion 2: Modificar tipo de consulta")
			print("-Opcion 3: Modificar edad")
			print("-Opcion 4: Modificar Prioridad del paciente")
			print("-Opcion 5: Modificar Fecha de cliente")
			print("-Opcion 6: Salir")
			print("-----------------------------------------")
			menu = input("-Digite su opcion del menu: ")
			menu = validar_numero(menu)

			if menu == 1:
				nomPac = input("Introducir nombre del paciente a modificar su nombre")
				encontrado = libre = i = 0
				while i <= cantidad_pacientes(hosp) and encontrado == 0:
					paciente = recuperar_paciente(hosp, i)
					if ver_nom(paciente) == nomPac:
						nuevoNom = input("Nombre nuevo: ")
						while libre == 0:
							while i <= cantidad_pacientes(hosp) and encontrado == 0:
								paciente_busc = recuperar_paciente(hosp, i)
								if ver_nom(paciente_busc) == nuevoNom:
									print("El nombre ya existe en la lista ")
									encontrado = 1
								else:
									i+=1
							if encontrado == 1:
								nuevoNom = input("Ingrese un nuevo nombre para el cliente")
								encontrado = i = 0
							elif encontrado == 0:
								libre = 1
						modif_nom(paciente, nuevoNom)
						os.system("cls")
						print("Modificacion exitosa")
						encontrado = 1
						os.system("pause")
						os.system("cls")
					else:
						i+=1
				if encontrado == 0:
					os.system("cls")
					print(" No se encontraron pacientes con el nombre ", nomPac)	
					os.system("pause")
					os.system("cls")
			

			elif menu == 2:
				modificarConsulta()


			elif menu == 3:
				modificarEdad()
				
			elif menu == 4:
				modificarPrioridad()

			elif menu == 5:
				modificarFecha()
			
			elif menu == 6:
				os.system("cls")
				break
			else:
				print("")
				os.system("cls")
				input("No ha pulsado ninguna opción correcta, intentelo de nuevo")

        

def validar_numero(numero): #Funcion recursiva que valida si el valor es un numerico, en el caso que no lo sea se llama asi misma hasta que ingrese un valor numerico
    try:
        return int(numero)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        numero = input("-Ingrese número válido: ")
        return validar_numero(numero)

#Las utilizamos para el enunciado E
def validacionFecha():
	while True:
		try:
			print('Ingrese la fecha (dd/mm/yyyy): ')
			dia=input('Dia: ')
			mes=input('Mes: ')
			anio=input('Anio: ')
			if ((int(anio)>1999)):
				fecha=date(int(anio), int(mes), int(dia))
				return fecha
			else:
				print('-','\nNo es una fecha valida, ingresela nuevamente\n','-')
		except(ValueError):
			print('-','\nNo es una fecha valida, ingresela nuevamente\n','-')
			return validacionFecha()


def validacionHora():
	while True:
		try:
			print('Ingrese la hora (hh:mm): ')
			h=input('Hora: ')
			m=input('Minutos: ')
			s=0
			hora=time(int(h), int(m), int(s))
			return hora
		except(ValueError):
			print('-','\nNo es una hora valida, ingresela nuevamente\n','-')
			return validacionHora()
		

#Utilizada para enunciado A: eliminar paciente por nombre
def validarNombre():
	nombre=input("Nombre: ")
	i=1
	while i<cantidad_pacientes(hosp):
		paciente=recuperar_paciente(hosp, i)
		if((ver_nom(paciente))==(nombre)):
			print('-','\nYa existe el nombre ingresado, intentelo nuevamente\n','-')
			return validarNombre()
		else:
			i+=1
	return nombre

#Enunciado A
def ingresarPaciente():
	resp=input('Quiere ingresar un paciente? s/n: ')
	while (resp=='s'):
		os.system("cls")
		print('Ingrese datos del paciente: ')
		nom=validarNombre()
		consulta=input('consulta: ')
		edad=input('edad: ')
		prioridad=input('Prioridad: ')
		fecha=validacionFecha()
		hora=validacionHora()
		paciente=crear_paciente()
		cargarPaciente(paciente, nom, consulta, edad, prioridad, fecha, hora)
		agregar_paciente(hosp, paciente)
		print('-'*29,'\nPaciente cargado correctamente\n','-'*29)
		resp=input('Desea ingresar otro paciente? s/n: ')
					

	
#Enunciado A: eliminar por nombre	
def eliminarUnPaciente():
	k=0
	i=0
	tam=cantidad_pacientes(hosp)
	if(tam!=0):
		nomPacElim=input('Ingrese el nombre del paciente a eliminar: ')
		while k<cantidad_pacientes(hosp):
			paciente=recuperar_paciente(hosp, k)
			if(ver_nom(paciente)==nomPacElim):
				eliminar_paciente(hosp, paciente)
				
				print('-','\nPaciente eliminado con exito\n', '-')
				i+=1
			else:
				k+=1
		if(i==0):
			print('-', '\nEl nombre ',nomPacElim ,'no existe, intentelo nuevamente\n', '-')
			resp=input('\nDesea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
			
			if(resp=='s'):
				return eliminarUnPaciente()
	else:
		print('-','\nNo hay pacientes cargados\n','-')			


#Enunciado B: lista de pacientes
def listarPacientes():
	tam=cantidad_pacientes(hosp)
	print ("Listado de pacientes del hospital: \n")
	if (tam==0):
		print('-','\nNo hay pacientes cargados\n','-')
	for k in range (tam):
		paciente=recuperar_paciente(hosp, k)
		
		print('-','paciente numero:',k+1,'-', '\nNombre:',ver_nom(paciente),
		'\nConsulta:',ver_consulta(paciente),'\nEdad:',ver_edad(paciente),'\nPrioridad:',
	    ver_prioridad(paciente),'\nFecha:', ver_fecha(paciente),'\nHora:', ver_hora(paciente),
		'\n','-')
	os.system("pause")
	
#Enunciado C: modificar urgencia de pacientes en un rango etario dado, a prioridad Alta
def modificarPacienteAlta():
	i=0
	tam=cantidad_pacientes(hosp)
	if(tam!=0):
		min=int(input(" Ingrese edad minima para modificar urgencia: "))
		max=int(input(" Ingrese edad maxima para modificar urgencia: "))
		for k in range (tam):
			paciente=recuperar_paciente(hosp, k)
			edad=ver_edad(paciente)
			if(min <= edad <= max):
				modif_prioridad(paciente, "Alta")
				print("\n Modificacion exitosa.\n ")
				i+=1
		if(i==0):
			print('-'*49,'\nNo hay pacientes en el rango ingresado, intentelo nuevamente\n', '-'*48)
			resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
			
			if(resp=='s'):
				return modificarPacienteAlta()
	else:
		print('-','\nNo hay pacientes cargados\n','-')		

#Enunciado D: eliminar pacientes por consulta
def eliminarSegunConsulta():
	k=0
	i=0
	if(cantidad_pacientes(hosp)!=0):
		consulta=input('Ingrese la consulta del paciente a eliminar: ')
		while k<cantidad_pacientes(hosp):
			paciente=recuperar_paciente(hosp, k)
			if(ver_consulta(paciente)==consulta):
				eliminar_paciente(hosp, paciente)

				print('-','\nPaciente eliminado con exito\n', '-')
				i+=1
			else:
				k+=1
		if(i==0):
			print('-', '\nLa consulta ', consulta, 'no existe, intentelo nuevamente\n', '-')
			resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
			
			if(resp=='s'):
				return eliminarSegunConsulta()
	else:
		print('-','\nNo hay pacientes cargados\n','-')	


#Enunciado E: lista con pacientes registrados en intervalo horario dado
def pacientesRangoEdad():
	i=0
	j=0
	tam=cantidad_pacientes(hosp)
	if(tam!=0):
		cola=crear_cola()
		print('Primer hora:')
		h01=validacionHora()
		print('Segunda hora: ')
		h02=validacionHora()	
		for k in range(tam):
			paciente=recuperar_paciente(hosp, k)
			if((ver_hora(paciente)<(h02))&(ver_hora(paciente)>(h01))):
				encolar(cola, paciente)
				print('-', '\nLa lista de pacientes entre las horas', h01, 'y',h02,'fue creada con exito\n', '-' )
				i+=1
		while not esta_vacia(cola):
			j+=1
			print('Lista de Pacientes: \n')
			paciente=desencolar(cola)
			print('-','paciente numero:',j,'-', '\nNombre:',ver_nom(paciente), '\nConsulta:',ver_consulta(paciente),'\nEdad:',ver_edad(paciente),'\nPrioridad:',
				  ver_prioridad(paciente),'\nFecha:', ver_fecha(paciente),'\nHora:', ver_hora(paciente),'\n','-')
			print("Para ver el siguiente paciente de la lista...")
			os.system("pause")

		if(i==0):
			
			print('-','\nNo existen pacientes entre las horas', h01, 'y', h02,'intentelo nuevamente\n', '-')
			resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario volvera al menu--: ')
			
			if(resp=='s'):
				return pacientesRangoEdad()
	else:
		print('-','\nNo hay pacientes cargados\n','-')

def listar_pacientes_prioridad_alta():
    pacientes_prioridad_alta = listar_pacientes_prioridad(hosp)
    if len(pacientes_prioridad_alta) == 0:
        print("No hay pacientes con prioridad alta.")
    else:
        print("Lista de pacientes con prioridad alta:")
        for paciente in pacientes_prioridad_alta:
            print('Nombre:', ver_nom(paciente), 'Consulta:', ver_consulta(paciente), 'Edad:', ver_edad(paciente),
                  'Fecha:', ver_fecha(paciente), 'Hora:', ver_hora(paciente))
    os.system("pause")
		


#MENU
while True:

	# Mostramos el menu
	print ("Selecciona una opción")
	print ("\t1- Agregar paciente")
	print ("\t2- Eliminar el paciente")
	print ("\t3- Listado de pacientes")
	print ("\t4- Dado un rango de edad, modificar la prioridad de los pacientes a alta")
	print ("\t5- Eliminar todos los pacientes cuya consulta sea igual a la ingresada")
	print ("\t6- Generar una lista con aquellos pacientes registrados entre dos horas dadas")
	print ("\t7 - Modificar propiedades de los pacientes")
	print("\t8 - Listar pacientes con prioridad alta")
	print ("\t0- salir")

	# solicitamos una opción al usuario
	opcionMenu = input("Seleccione una opcion: ")
 	
	if opcionMenu=="1":
		ingresarPaciente()
		
	elif opcionMenu=="2":
		eliminarUnPaciente()

	elif opcionMenu=="3":
		listarPacientes()

	elif opcionMenu=="4":
		modificarPacienteAlta()

	elif opcionMenu=="5":
		eliminarSegunConsulta()

	elif opcionMenu=="6":
		pacientesRangoEdad()

	elif opcionMenu=="7":
		modificacionPaciente(hosp)
		
	elif opcionMenu=="8":
		listar_pacientes_prioridad_alta()
		
	elif opcionMenu == "0":
		os.system("cls")
		print("\n¡Gracias por usar nuestro programa!\n")
		break
	
	else:
		print("")
		os.system("cls")
		input("No ha pulsado ninguna opción correcta, intentelo de nuevo")
	