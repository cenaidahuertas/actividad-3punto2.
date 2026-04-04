"""
Módulo: objeto.py
Representa un objeto de arte genérico en el museo.
"""

from obraArte import ObraArte


class Objeto(ObraArte):

    def __init__(self, id_obra, titulo, autor, periodo, valor_economico,
                 fecha_creacion, fecha_entrada, descripcion, estado):

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

    def __str__(self):
        return (
            f"Objeto: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"Período: {self.periodo} | "
            f"Descripción: {self.descripcion} | "
            f"Estado: {self.estado}"
        )
