# tadCola.py

def crear_cola():
    return []

def encolar(cola, item):
    cola.insert(0, item)

def desencolar(cola):
    if not esta_vacia(cola):
        return cola.pop()
    return None

def esta_vacia(cola):
    return len(cola) == 0

def tamano(cola):
    return len(cola)
