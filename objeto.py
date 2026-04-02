class Objeto():
    def __init__(self, *args, descripcion):
        super().__init__(*args)
        self.descripcion = descripcion

        