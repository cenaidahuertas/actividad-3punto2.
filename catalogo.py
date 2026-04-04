
from obraArte import ObraArte

class Catalogo:
    def __init__(self, id, nombre) -> None:
        self.id = id
        self.nombre = nombre
    
    # Lista donde se guardan todas las obras
    
        self.obras = []
    
    # - propiedades -──────────────────────────────────
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, nuevo_id):
        if isinstance(nuevo_id, int) and nuevo_id > 0:
            self._id = nuevo_id
        else:
            raise ValueError("El ID del catálogo debe ser un número entero positivo.")
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre.strip()
        else:
            raise ValueError("El nombre del catálogo debe ser una cadena de texto no vacía.")

    # - métodos -──────────────────────────────────

    def registrar_obra(self, obra):
        if isinstance(obra, ObraArte):
            self.obras.append(obra)
        else:
            raise ValueError("Solo se pueden registrar objetos de tipo ObraArte.")
    
    def buscar_obra (self, id_obra):
        for obra in self.obras:
            if obra.id_obra == id_obra:
                return obra
        return None  # Si no se encuentra la obra, devuelve None    

    def listar_obras(self):
        """Lista todas las obras del catálogo."""
        if not self.obras:
            print(f"El catálogo '{self.nombre}' no tiene obras registradas.")
            return []

        print(f"Obras en el catálogo '{self.nombre}':")
        for obra in self.obras:
            print(f"  - {obra.titulo} | Autor: {obra.autor} | Estado: {obra.estado}")

        return self.obras
    

# - representación -──────────────────────────────────

    def __str__(self):
        return f"Catálogo: {self.nombre} (ID: {self.id}) - Total obras: {len(self.obras)}"
    