class Cesion:
    def __init__(self, id, obra, museo, importe, fecha_inicio, fecha_fin):
        self.id = id
        self.obra = obra
        self.museo = museo
        self.importe = importe
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "PENDIENTE"

    def iniciar_cesion(self):
        self.estado = "ACTIVA"
        self.obra.estado = "CEDIDA"
        self.obra.museo_cedido_actual = self.museo

    def finalizar(self):
        self.estado = "FINALIZADA"
        self.obra.estado = "EXHIBIDA"
        self.obra.museo_cedido_actual = None
        