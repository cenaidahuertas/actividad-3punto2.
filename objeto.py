from obraArte import ObraArte

class Objeto(ObraArte):

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
        estado
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
        estado
    )

        # Atributo propio de Objeto
        self.descripcion = descripcion
    
    # ── representación ───────────────────────────────────
    def __str__(self):
        return (
            f"Objeto: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"Período: {self.periodo} | "
            f"Descripción: {self.descripcion} | "
            f"Estado: {self.estado}"
        )