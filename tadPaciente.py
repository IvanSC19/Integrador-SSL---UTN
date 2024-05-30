# tadPaciente.py

def crear_paciente():
    #Crea un paciente vacio
	paciente=['','',0,'',0,0]
	return paciente

def cargarPaciente(paciente, nom, consulta, edad, prioridad, fecha, hora):
	#Carga los datos del ppaciente con su nombre, consulta, edad, prioridad y fecha
	#y hora
	paciente[0]=nom
	paciente[1]=consulta
	paciente[2]=edad
	paciente[3]=prioridad
	paciente[4]=fecha
	paciente[5]=hora
	return paciente


def ver_nom(paciente):
    return paciente[0]

def ver_prioridad(paciente):
    return paciente[3]

# Otros métodos como ver_consulta, ver_edad, ver_fecha, ver_hora
def ver_consulta(paciente):
    return paciente[1]

def ver_edad(paciente):
    return paciente[2]

def ver_fecha(paciente):
    return paciente[4]

def ver_hora(paciente):
    return paciente[5]

def modif_nom(paciente, nuevoNom):
	#Modifica el nombre del paciente
	paciente[0]=nuevoNom

def modif_consulta(paciente, nuevaConsulta):
	#Modifica la consulta del paciente
	paciente[1]=nuevaConsulta

def modif_edad(paciente, nuevaEdad):
	#Modifica la edad del paciente
	paciente[2]=nuevaEdad

def modif_prioridad(paciente, nuevaPrioridad):
	#Modifica la prioridad del paciente
	paciente[3]=nuevaPrioridad

def modif_fecha(paciente, nuevaFecha):
	#Modifica la fecha del paciente
	paciente[4]=nuevaFecha

def modif_hora(paciente, nuevaHora):
	#Modifica la hora del paciente
	paciente[5]=nuevaHora