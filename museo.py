
class Museo:
    def __init__(
            self,
            nombre,
            direccion) -> None:

        # Datos básicos del museo
        self.nombre = nombre
        self.direccion = direccion 
    
        # lista de obras que tiene el museo 
        self.obras_recibidas = []
    
        # lista de cesiones solicitadas por museo 
        self.censiones = []

    # propiedades ________________________
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, valor):
        self._direccion = valor

    @property
    def obras_recibidas(self):
        return self._obras_recibidas

    @obras_recibidas.setter
    def obras_recibidas(self, valor):
        self._obras_recibidas = valor

    @property
    def censiones(self):
        return self._censiones

    @censiones.setter
    def censiones(self, valor):
        self._censiones = valor

# métodos ___________________________

def recibir_obra(self, obra):
    """ Registra una obra que llega al museo por cesión ."""
    self.obras_recibidas.append(obra)
    print(f"Museo '{self.nombre}' recibió la obra '{obra.titulo}' correctamente.")

def devolver_obra(self, obra):
    """ Registra la devolución de una obra al museo ."""
    if obra in self.obras_recibidas:
        self.obras_recibidas.remove(obra)
        print(f"Museo '{self.nombre}' devolvió la obra '{obra.titulo}' correctamente.")
    else:
        print(f"La obra '{obra.titulo}' no se encuentra en el museo '{self.nombre}'.")

def solicitar_cesion(self, cesion):
    """ Registra una solicitud de cesión por parte del museo ."""
    self.censiones.append(cesion)
    print(f"Museo '{self.nombre}' solicitó la cesión de la obra '{cesion.obra.titulo}' correctamente.")

# - representación del museo __________________________

def __str__(self):
        return f"Museo: {self.nombre}, Dirección: {self.direccion}, Obras Recibidas: {len(self.obras_recibidas)}, Cesiones Solicitadas: {len(self.censiones)}"

