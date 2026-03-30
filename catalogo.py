class Catalogo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.obras = []

    def agregar_obra(self, obra):
        self.obras.append(obra)

    def buscar_obra(self, titulo):
        return [o for o in self.obras if o.titulo == titulo]

    def listar_obras(self):
        return self.obras