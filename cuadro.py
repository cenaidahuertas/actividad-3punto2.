from obraArte import ObraArte

class Cuadro(ObraArte):

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
        tecnica,
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

        # Atributos propios de Cuadro
        self.tecnica = tecnica  # Ejemplo: "óleo", "acuarela", "fresco"
        self.estilo = estilo    # Ejemplo: "impresionista", "barroco", "cubista"

    # ── representación ───────────────────────────────────
    def __str__(self):
        return (
            f"Cuadro: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"Técnica: {self.tecnica} | "
            f"Estilo: {self.estilo} | "
            f"Estado: {self.estado}"
        )