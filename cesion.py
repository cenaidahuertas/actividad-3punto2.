from datetime import datetime

import obraArte

class Cesion:
    def __init__(
        self,
        obra,
        museo,
        fecha_inicio,
        fecha_fin,
        importe) -> None:

        self.obra = obra
        self.museo = museo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.importe = importe
        self.estado = "EN CURSO"

    # - propiedades -──────────────────────────────────

    @property
    def obra(self):
        return self._obra
    @obra.setter
    def obra(self, nueva_obra):
        if isinstance(nueva_obra, obraArte):
            self._obra = nueva_obra
        else:
            raise ValueError("La cesión debe estar asociada a una obra de arte válida.")
        
    @property
    def museo(self):
        return self._museo
    @museo.setter
    def museo(self, nuevo_museo):
        if isinstance(nuevo_museo, Museo):
            self._museo = nuevo_museo
        else:
            raise ValueError("La cesión debe estar asociada a un museo válido.")
        
    @property
    def fecha_inicio(self):
        return self._fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        if isinstance(nueva_fecha_inicio, datetime):
            self._fecha_inicio = nueva_fecha_inicio
        else:
            raise ValueError("La fecha de inicio debe ser un objeto datetime válido.")
    
    @property
    def fecha_fin(self):
        return self._fecha_fin
    @fecha_fin.setter
    def fecha_fin(self, nueva_fecha_fin):
        if isinstance(nueva_fecha_fin, datetime):
            self._fecha_fin = nueva_fecha_fin
        else:
            raise ValueError("La fecha de fin debe ser un objeto datetime válido.")
    
    @property
    def importe(self):
        return self._importe
    @importe.setter
    def importe(self, nuevo_importe):
        if isinstance(nuevo_importe, (int, float)) and nuevo_importe >= 0:
            self._importe = nuevo_importe
        else:
            raise ValueError("El importe de la cesión debe ser un número no negativo.")
    
    # - métodos -──────────────────────────────────

    def iniciar_cesion(self):
        self.estado = "EN CURSO"

        self.estado = "activa"
        self.obra.estado = "EN CESIÓN"
        print(f"La cesión de la obra '{self.obra.titulo}' al museo '{self.museo.nombre}' ha comenzado.")
    
    def finalizar_cesion(self):
        self.estado = "FINALIZADA"
        self.obra.estado = "DISPONIBLE"
        print(f"La cesión de la obra '{self.obra.titulo}' al museo '{self.museo.nombre}' ha finalizado.")
    
# - representación -──────────────────────────────────

def __str__(self):
    return (
            f"Cesion: {self.obra.titulo} | "
            f"Museo: {self.museo.nombre} | "
            f"Desde: {self.fecha_inicio} hasta: {self.fecha_fin} | "
            f"Importe: ${self.importe} | "
            f"Estado: {self.estado}"
        ) 