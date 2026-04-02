class Escultura():
    def __init__(self, *args, material, estilo):
        super().__init__(*args)
        self.material = material
        self.estilo = estilo
