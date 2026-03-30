class Periodo:
    def __init__(self, id, nombre, fecha_inicio, fecha_fin):
        self.id = id
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def pertenece_periodo(self, fecha):
        return self.fecha_inicio <= fecha <= self.fecha_fin