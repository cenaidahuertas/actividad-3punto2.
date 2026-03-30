from datetime import date

class Restauracion:
    def __init__(self, obra, tipo):
        self.obra = obra
        self.tipo = tipo
        self.fecha_inicio = date.today()
        self.fecha_fin = None

    def iniciar(self):
        self.obra.estado = "EN_RESTAURACION"
        self.obra.restauraciones.append(self)

    def finalizar(self):
        self.fecha_fin = date.today()
        self.obra.estado = "EXHIBIDA"