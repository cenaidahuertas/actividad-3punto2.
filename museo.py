class Museo:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.salas = []
        self.obras = []
        self.cesiones = []
        self.museos_colaboradores = []
        self.solicitudes_cesion = []

    def agregar_sala(self, sala):
        self.salas.append(sala)

    def recibir_obra(self, obra):
        self.obras.append(obra)

    def agregar_museo_colaborador(self, nombre):
        self.museos_colaboradores.append(nombre)

    def registrar_cesion(self, cesion):
        self.cesiones.append(cesion)

    def listar_obras_en_restauracion(self):
        return [o for o in self.obras if o.estado == "EN_RESTAURACION"]