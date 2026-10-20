# Estructuras de datos — Centro de salud (N.º 33)

## Objetivo
Implementar y probar una lista enlazada, una pila y una cola. El reto individual asignado al n.º **33 (Centro de salud)** consiste en **buscar una solicitud por código en la lista enlazada**.

## Código completo
Guarda el siguiente código como `centro_salud.py` y ejecútalo con Python 3:

```python
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

        # Si la lista está vacía, el nuevo nodo será la cabeza.
        if self.cabeza is None:
            self.cabeza = nuevo
            return

        # Si ya hay elementos, recorrer hasta el último y enlazar el nuevo.
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

    def buscar_por_codigo(self, codigo):
        """Busca una solicitud por código sin modificar la lista."""
        actual = self.cabeza
        while actual is not None:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def contar(self):
        """Cuenta los nodos sin convertir la lista en una lista de Python."""
        cantidad = 0
        actual = self.cabeza
        while actual is not None:
            cantidad += 1
            actual = actual.siguiente
        return cantidad


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # El último elemento agregado queda en la cima (LIFO).
        self.items.append(elemento)

    def desapilar(self):
        # Una pila vacía no tiene elementos que retirar.
        if not self.items:
            return None
        return self.items.pop()

    def cima(self):
        """Consulta el último elemento sin retirarlo."""
        if not self.items:
            return None
        return self.items[-1]


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # El elemento nuevo se agrega al final de la cola.
        self.items.append(elemento)

    def desencolar(self):
        # Se retira el primer elemento agregado (FIFO).
        if not self.items:
            return None
        return self.items.pop(0)

    def frente(self):
        """Consulta el primer elemento sin retirarlo."""
        if not self.items:
            return None
        return self.items[0]


# Pruebas del caso asignado: Centro de salud (n.º 33).
if __name__ == "__main__":
    solicitudes = ListaEnlazada()
    solicitudes.agregar("SOL-001", "Consulta general")
    solicitudes.agregar("SOL-002", "Control médico")
    solicitudes.agregar("SOL-003", "Solicitud de laboratorio")

    print("=== Solicitudes registradas ===")
    solicitudes.mostrar()
    print("Cantidad de solicitudes:", solicitudes.contar())

    print("\n=== Búsqueda por código ===")
    codigo_buscado = "SOL-002"
    resultado = solicitudes.buscar_por_codigo(codigo_buscado)
    if resultado is not None:
        print(f"Solicitud encontrada: {resultado.codigo} - {resultado.descripcion}")
    else:
        print(f"No existe una solicitud con el código {codigo_buscado}.")

    # Prueba de búsqueda no encontrada.
    codigo_inexistente = "SOL-999"
    resultado = solicitudes.buscar_por_codigo(codigo_inexistente)
    if resultado is None:
        print(f"No existe una solicitud con el código {codigo_inexistente}.")

    print("\n=== Prueba de pila (LIFO) ===")
    historial = Pila()
    historial.apilar("Registrar solicitud")
    historial.apilar("Revisar solicitud")
    print("Cima:", historial.cima())
    print("Desapilado:", historial.desapilar())
    print("Desapilado:", historial.desapilar())
    print("Pila vacía:", historial.desapilar())

    print("\n=== Prueba de cola (FIFO) ===")
    atencion = Cola()
    atencion.encolar("Paciente A")
    atencion.encolar("Paciente B")
    atencion.encolar("Paciente C")
    print("Frente:", atencion.frente())
    print("Desencolado:", atencion.desencolar())
    print("Elementos restantes:", atencion.items)
    print("Desencolado:", atencion.desencolar())
    print("Desencolado:", atencion.desencolar())
    print("Cola vacía:", atencion.desencolar())
```

## ¿Cómo funciona el reto asignado?

El método `buscar_por_codigo(codigo)` comienza en `self.cabeza` y recorre los nodos uno por uno. Compara el código buscado con `actual.codigo`:

- Si coincide, devuelve el nodo encontrado.
- Si llega al final (`None`) sin coincidencias, devuelve `None`.
- No elimina ni cambia nodos, por lo que conserva los enlaces de la lista.

Ejemplo:

```python
resultado = solicitudes.buscar_por_codigo("SOL-002")
if resultado is not None:
    print(resultado.codigo, resultado.descripcion)
else:
    print("Solicitud no encontrada")
```

## Otras operaciones implementadas

- **Lista enlazada:** `agregar`, `mostrar`, `buscar_por_codigo` y `contar`.
- **Pila:** `apilar`, `desapilar` y `cima`. Sigue LIFO: el último en entrar es el primero en salir.
- **Cola:** `encolar`, `desencolar` y `frente`. Sigue FIFO: el primero en entrar es el primero en salir.
- **Casos vacíos:** `desapilar`, `desencolar`, `cima` y `frente` devuelven `None` cuando no hay elementos.

## Cómo ejecutar

1. Instala Python 3 si todavía no lo tienes.
2. Guarda el código en `centro_salud.py`.
3. Abre una terminal en la carpeta donde guardaste el archivo.
4. Ejecuta:

```bash
python centro_salud.py
```

## Resultado esperado de la búsqueda

La búsqueda de `SOL-002` debe mostrar:

```text
Solicitud encontrada: SOL-002 - Control médico
```

La búsqueda de `SOL-999` debe indicar que no existe una solicitud con ese código.
