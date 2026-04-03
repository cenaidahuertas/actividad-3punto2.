from datetime import date


class ObraArte:
    def __init__(self, id, titulo, autor, periodo, valor_economico, fecha_creacion, fecha_entrada, descripcion):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.periodo = periodo
        self.valor_economico = valor_economico
        self.fecha_creacion = fecha_creacion
        self.fecha_entrada = fecha_entrada
        self.descripcion = descripcion
        self.estado = "EXHIBIDA"
        self.restauraciones = []
        self.sala_actual = None
        self.museo_cedido_actual = None

    def necesita_restauracion(self):
        return (date.today() - self.fecha_entrada).days > 5 * 365

    def necesita_restauracion_programada(self, fecha_actual):
        return self.estado == "danada"

    def enviarARestauracion(self, restauracion):
        self.estado = "EN_RESTAURACION"
        self.restauraciones.append(restauracion)

    def finalizar_restauracion(self, fecha_fin):
        self.estado = "EXHIBIDA"

    def __str__(self):
        return f"{self.titulo} ({self.autor}) - {self.estado}"


class Cuadro(ObraArte):
    def __init__(self, *args, tecnica, estilo):
        super().__init__(*args)
        self.tecnica = tecnica
        self.estilo = estilo


class Escultura(ObraArte):
    def __init__(self, *args, material, estilo):
        super().__init__(*args)
        self.material = material
        self.estilo = estilo


class OtroObjeto(ObraArte):
    def __init__(self, *args, estado="EXHIBIDA", tipo_objeto):
        super().__init__(*args)
        self.estado = estado
        self.tipo_objeto = tipo_objeto