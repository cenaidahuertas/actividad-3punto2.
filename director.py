"""
Módulo: director.py
Representa al Director del museo.
"""

from usuario import Usuario


class Director(Usuario):
    def __init__(self, id_usuario, nombre, apellido, email, contrasena):
        super().__init__(id_usuario, nombre, apellido, email, contrasena, rol="director")
        self.cesiones = []

    def gestionar_cesion(self, cesion):
        self.cesiones.append(cesion)
        print(f"Cesión de '{cesion.obra.titulo}' gestionada correctamente.")

    def calcular_valor_total(self):
        total = sum(cesion.obra.valor_economico for cesion in self.cesiones)
        print(f"Valor total de obras en cesión: COP {total:,}")
        return total

    def ver_catalogo(self, catalogo):
        catalogo.listar_obras()

    def ver_cesiones_activas(self):
        activas = [c for c in self.cesiones if c.estado == "activa"]
        if not activas:
            print("No hay cesiones activas.")
            return []
        print(f"Cesiones activas ({len(activas)}):")
        for cesion in activas:
            print(f"  - Obra: {cesion.obra.titulo} | Museo: {cesion.museo.nombre}")
        return activas

    def __str__(self):
        return f"Director: {self.nombre} {self.apellido} (ID: {self.id_usuario})"
