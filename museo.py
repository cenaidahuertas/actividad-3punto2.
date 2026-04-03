
class Museo:
    def __init__(
            self,
            nombre,
            direccion): -> None

        # Datos básicos del museo
        self.nombre = nombre
        self.direccion = direccion
    
    # lista de obras que tiene el museo 
        self.obras_recibidas = []
    
    # lista de cesiones solicitadas por museo 

        self.censiones: []
    
    # - propiedades -──────────────────────────────────

    @property
    