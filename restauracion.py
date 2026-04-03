class Restauracion:
    def __init__(self, id, tipo, fecha_inicio, motivo):
        self.id = id
        self.tipo = tipo
        self.fecha_inicio = fecha_inicio
        self.motivo = motivo
        self.fecha_fin = None

    def finalizar(self, fecha_fin):
        self.fecha_fin = fecha_fin