from obraArte import ObraArte

class Escultura(ObraArte):
    
    def __init__(
        self,
        id_obra,
        titulo,
        autor,
        periodo,
        valor_economico,
        fecha_creacion,
        fecha_entrada,
        descripcion,
        estado,
        material,
        estilo
) -> None:
    
    # Llamamos al constructor del padre (ObraArte)
        super().__init__(
        id_obra,
        titulo,
        autor,
        periodo,
        valor_economico,
        fecha_creacion,
        fecha_entrada,
        descripcion,
        estado
    )

        # Atributos propios de Escultura
        self.material = material  # Ejemplo: "mármol", "bronce", "madera"
        self.estilo = estilo      # Ejemplo: "realista", "abstracto", "clásico"
    
    # ── representación ───────────────────────────────────
    def __str__(self):
        return f"Escultura(ID: {self.id_obra}, Título: '{self.titulo}', Autor: {self.autor}, Periodo: {self.periodo}, Valor: ${self.valor_economico}, Creación: {self.fecha_creacion}, Entrada: {self.fecha_entrada}, Material: {self.material}, Estilo: {self.estilo}, Estado: {self.estado})"
    
