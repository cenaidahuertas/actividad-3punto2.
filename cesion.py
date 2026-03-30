class Cesion:
    def __init__(self, id, obra, museo, fecha_inicio, fecha_fin, importe):
        self.id = id
        self.obra = obra
        self.museo = museo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.importe = importe
        self.estado = "ACTIVA"

    def finalizar(self):
        self.estado = "FINALIZADA"
        