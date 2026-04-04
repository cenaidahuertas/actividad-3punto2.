

class Sala:
    def __init__(
            self,
            nombre,
            ubicacion) -> None:
        self.nombre = nombre
        self.ubicacion = ubicacion
        # Lista de obras que están en esta sala
        self.obras = []

# - propiedades -──────────────────────────────────

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre.strip()
        else:
            raise ValueError("El nombre de la sala debe ser una cadena de texto no vacía.")
    
    @property
    def ubicacion(self):
        return self._ubicacion
    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        if isinstance(nueva_ubicacion, str) and nueva_ubicacion.strip():
            self._ubicacion = nueva_ubicacion.strip()
        else:
            raise ValueError("La ubicación de la sala debe ser una cadena de texto no vacía.")
    
# - métodos -──────────────────────────────────

    def asignar_obra(self, obra):
        """Asigna una obra a esta sala."""
        self.obras.append(obra)
        
    
    def retirar_obra(self, obra):
        """Retira una obra de esta sala."""
        if obra in self.obras:
            self.obras.remove(obra)
            print(f"Obra '{obra.titulo}' retirada de la sala '{self.nombre}'.")
        else:
            print(f"La obra '{obra.titulo}' no se encuentra en la sala '{self.nombre}'.")
    
    def listar_obras(self):
        """Lista todas las obras asignadas a esta sala."""
        if self.obras:
            print(f"Obras en la sala '{self.nombre}':")
            for obra in self.obras:
                print(f"- {obra.titulo} (ID: {obra.id_obra})")
        else:
            print(f"No hay obras asignadas a la sala '{self.nombre}'.")

    # ── representación ───────────────────────────────────
    def __str__(self):
        return f"Sala: {self.nombre} | Ubicación: {self.ubicacion} | Número de obras: {len(self.obras)}"
    
    def __repr__(self):
        return f"Sala(nombre='{self.nombre}', ubicacion='{self.ubicacion}')"
