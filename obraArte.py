from datetime import date

class ObraArte:
    def __init__(self, id, titulo, autor, valor_economico, fecha_creacion, fecha_entrada, periodo):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.valor_economico = valor_economico
        self.fecha_creacion = fecha_creacion
        self.fecha_entrada = fecha_entrada
        self.periodo = periodo
        self.estado = "EXHIBIDA"
        self.restauraciones = []

    def necesita_restauracion(self):
        return (date.today() - self.fecha_entrada).days > 5 * 365






class Objeto(ObraArte):
    def __init__(self, *args, descripcion):
        super().__init__(*args)
        self.descripcion = descripcion