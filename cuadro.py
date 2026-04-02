class Cuadro():
    def __init__(self, *args, tecnica, estilo):
        super().__init__(*args)
        self.tecnica = tecnica
        self.estilo = estilo