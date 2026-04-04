"""
Módulo: encargadoCatalogo.py
Representa al encargado que gestiona las obras del catálogo del museo.
"""

from usuario import Usuario


class EncargadoCatalogo(Usuario):

    def __init__(self, id_usuario, nombre, apellido, email, contrasena, catalogo):
        super().__init__(id_usuario, nombre, apellido, email, contrasena, rol="encargado_catalogo")
        self.catalogo = catalogo

    def registrar_obra(self, obra):
        """Agrega una obra nueva al catálogo."""
        self.catalogo.registrar_obra(obra)
        print(f"Obra '{obra.titulo}' registrada correctamente.")

    def editar_obra(self, id_obra, titulo=None, autor=None, periodo=None, estado=None):
        """Edita los datos de una obra."""
        obra = self.catalogo.buscar_obra(id_obra)
        if obra is None:
            print(f"No se encontró ninguna obra con ID {id_obra}.")
            return
        if titulo is not None:
            obra.titulo = titulo
        if autor is not None:
            obra.autor = autor
        if periodo is not None:
            obra.periodo = periodo
        if estado is not None:
            obra.estado = estado
        print(f"Obra ID {id_obra} actualizada correctamente.")

    def eliminar_obra(self, id_obra):
        """Elimina una obra del catálogo."""
        obra = self.catalogo.buscar_obra(id_obra)
        if obra is None:
            print(f"No se encontró ninguna obra con ID {id_obra}.")
            return
        self.catalogo.obras.remove(obra)
        print(f"Obra '{obra.titulo}' eliminada del catálogo.")

    def clasificar_obra(self, id_obra, periodo):
        """Asigna un período artístico a una obra."""
        obra = self.catalogo.buscar_obra(id_obra)
        if obra is None:
            print(f"No se encontró ninguna obra con ID {id_obra}.")
            return
        obra.periodo = periodo
        print(f"Obra '{obra.titulo}' clasificada en el período '{periodo}'.")

    def asignar_sala(self, id_obra, sala):
        """Asigna una obra a una sala del museo."""
        obra = self.catalogo.buscar_obra(id_obra)
        if obra is None:
            print(f"No se encontró ninguna obra con ID {id_obra}.")
            return
        sala.asignar_obra(obra)
        print(f"Obra '{obra.titulo}' asignada a la sala '{sala.nombre}'.")

    def listar_obras_por_sala(self, sala):
        """Muestra todas las obras de una sala."""
        return sala.listar_obras()

    def __str__(self):
        return f"EncargadoCatalogo: {self.nombre} {self.apellido} (ID: {self.id_usuario})"
