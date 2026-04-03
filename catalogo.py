class Catalogo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.obras = []

    def agregarObra(self, obra):
        self.obras.append(obra)

    def buscarObra(self, titulo):
        for obra in self.obras:
            if obra.titulo == titulo:
                return obra
        return None

    def listarObras(self):
        return self.obras

    def FechaDeExposicion(self, exposicion):
        return f"Inicio: {exposicion.fecha_inicio} | Fin: {exposicion.fecha_fin}"

    def listar_obras_por_sala(self, nombre_sala):
        return [o for o in self.obras if o.sala_actual and o.sala_actual.nombre == nombre_sala]