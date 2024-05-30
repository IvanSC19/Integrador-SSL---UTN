# tadHosp.py
from tadPaciente import*

def crear_hospital():
    hosp=[]
    return hosp

def agregar_paciente(hospital, paciente):
    hospital.append(paciente)

def eliminar_paciente(hospital, paciente):
    hospital.remove(paciente)

def modificar_prioridad_paciente(hospital, paciente, nueva_prioridad):
    modif_prioridad(paciente, nueva_prioridad)

def recuperar_paciente(hospital, indice):
    elemento=hospital[indice-1]
    return elemento

def cantidad_pacientes(hospital):
    return len(hospital)

def listar_pacientes_prioridad(hospital):
    return [paciente for paciente in hospital if ver_prioridad(paciente) == "Alta"]
