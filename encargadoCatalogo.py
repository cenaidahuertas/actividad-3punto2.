from catalogo import Catalogo
from obraArte import ObraArte
from usuario import Usuario

class EncargadoCatalogo(Usuario):

    def __init__(
        self,
        id_usuario,
        nombre,
        apellido,
        email,
        contrasena,
        catalogo) -> None:

        # Llamamos al constructor del padre (Usuario)
        super().__init__(id_usuario, nombre, apellido, email, contrasena, rol="encargado_catalogo")

        # Asignamos el catálogo
        self.catalogo = catalogo

    # --- propiedades ───────────────────────────────────
    @property
    def catalogo(self):
        return self._catalogo

    @catalogo.setter
    def catalogo(self, nuevo_catalogo):
        if isinstance(nuevo_catalogo, Catalogo):
            self._catalogo = nuevo_catalogo
        else:
            raise ValueError("El catálogo debe ser una instancia de Catalogo.")

    # --- métodos ───────────────────────────────────

    def registrar_obra(self, obra):
        """Agrega una obra nueva al catálogo."""
        self.catalogo.registrar_obra(obra)
        print(f"Obra '{obra.titulo}' registrada correctamente.")

    def editar_obra(self, id_obra, titulo=None, autor=None, periodo=None, estado=None):
        """Edita los datos de una obra. Solo modifica los campos que se pasen como argumento."""
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
        """Elimina una obra del catálogo según su ID."""
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
        """Muestra todas las obras que hay en una sala."""
        obras = sala.listar_obras()

        if not obras:
            print(f"La sala '{sala.nombre}' no tiene obras.")
            return []

        print(f"Obras en la sala '{sala.nombre}':")
        for obra in obras:
            print(f"  - {obra.titulo} ({obra.autor})")

        return obras

    # ── representación ───────────────────────────────────
    def __str__(self):
        return f"Encargado de Catálogo: {self.nombre} {self.apellido} (ID: {self.id_usuario})"

    def __repr__(self):
        return f"EncargadoCatalogo(id_usuario={self.id_usuario}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"