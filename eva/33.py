class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        # controla el caso de pila vacía
        if len(self.items) == 0:
            return None
        return self.items.pop()


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        # controla el caso de cola vacía
        if len(self.items) == 0:
            return None
        return self.items.pop(0)


# ==========================================
# PRUEBAS: SISTEMA DE SOLICITUDES
# CENTRO DE SALUD - VERSION 33
# ==========================================

print("=== CENTRO DE SALUD ===")

# 1. Registrar solicitudes en la lista enlazada
solicitudes = ListaEnlazada()

solicitudes.agregar("S01", "Consulta medica general")
solicitudes.agregar("S02", "Control de enfermeria")
solicitudes.agregar("S03", "Atencion odontologica")

print("\n1. LISTA DE SOLICITUDES REGISTRADAS:")
solicitudes.mostrar()

+
# 3. Probar la cola (FIFO)
turnos = Cola()

turnos.encolar("S01 - Consulta medica general")
turnos.encolar("S02 - Control de enfermeria")
turnos.encolar("S03 - Atencion odontologica")

print("\n3. COLA: orden de atencion")
print("Primera solicitud atendida:", turnos.desencolar())
print("Segunda solicitud atendida:", turnos.desencolar())
print("Tercera solicitud atendida:", turnos.desencolar())

print("Cola vacia:", turnos.desencolar())

print("\nPruebas finalizadas correctamente.")