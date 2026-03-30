class Sala:
    def __init__(self, id, nombre, ubicacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.obras = []

    def asignarObra(self, obra):
        self.obras.append(obra)
        obra.sala_actual = self

    def retirarObra(self, obra):
        if obra in self.obras:
            self.obras.remove(obra)
            obra.sala_actual = None

    def listarObras(self):
        return self.obras


class Exposicion:
    def __init__(self, fecha_inicio, fecha_fin, sala):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.sala = sala

    def iniciarExposicion(self):
        return f"La exposicion de la sala {self.sala.nombre} ha iniciado."

    def finalizarExposicion(self):
        return f"La exposicion de la sala {self.sala.nombre} ha finalizado."

    def estaActiva(self, fecha_actual):
        return self.fecha_inicio <= fecha_actual <= self.fecha_fin
