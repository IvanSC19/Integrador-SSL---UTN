import tadHosp
from tadHosp import *
import tadPaciente
from tadPaciente import *
from datetime import *

def carga_pacientes(hosp):
    pacientes = []
    datos_pacientes = [
        ("Pedro", "clinica", 23, "baja", date(2000, 12, 12), time(int(12), int(55), int(00))),
        ("Esteban", "oftalmologo", 20, "media", date(2000, 12, 12), time(int(13), int(35), int(00))),
        ("Juan", "urologo", 26, "media", date(2000, 12, 12), time(int(14), int(10), int(00))),
        ("Alejo", "cirujia", 28, "baja", date(2000, 12, 12), time(int(15), int(30), int(00))),
        ("Tomas", "clinica", 40, "media", date(2000, 12, 12), time(int(16), int(30), int(00))),
        ("Alberto", "neurologia", 53, "baja", date(2000, 12, 12), time(int(17), int(30), int(00))),
        ("Ivan", "pediatra", 12, "media", date(2000, 12, 12), time(int(18), int(30), int(00))),
    ]

    for datos in datos_pacientes:
        paciente = crear_paciente()
        paciente = cargarPaciente(paciente, *datos)
        pacientes.append(paciente)

    for paciente in pacientes:
        agregar_paciente(hosp, paciente)

