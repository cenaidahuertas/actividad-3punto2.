from abc import ABC, abstractmethod
from datetime import date

class ObraArte(ABC):
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
        
        # datos basicos comunes a todas las obras
        self.id_obra = id_obra
        self.titulo = titulo
        self.autor = autor
        self.periodo = periodo
        self.valor_economico = valor_economico
        self.fecha_creacion = fecha_creacion
        self.fecha_entrada = fecha_entrada
        self.descripcion = descripcion
        self.estado = estado  # Ejemplo: "en exhibición", "en restauración", "cedida", "en almacenamiento"

    # - propiedades -──────────────────────────────────

    @property
    def id_obra(self):
        return self._id_obra
    @id_obra.setter
    def id_obra(self, nuevo_id):
        if isinstance(nuevo_id, int) and nuevo_id > 0:
            self._id_obra = nuevo_id
        else:
            raise ValueError("El ID de la obra debe ser un número entero positivo.")
        
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and nuevo_titulo.strip():
            self._titulo = nuevo_titulo.strip()
        else:
            raise ValueError("El título debe ser una cadena de texto no vacía.")
        
    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, nuevo_autor):
        if isinstance(nuevo_autor, str) and nuevo_autor.strip():
            self._autor = nuevo_autor.strip()
        else:
            raise ValueError("El autor debe ser una cadena de texto no vacía.")
    
    @property
    def periodo(self):
        return self._periodo        
    @periodo.setter
    def periodo(self, nuevo_periodo):
        if isinstance(nuevo_periodo, str) and nuevo_periodo.strip():
            self._periodo = nuevo_periodo.strip()
        else:
            raise ValueError("El período debe ser una cadena de texto no vacía.")
    
    @property
    def valor_economico(self):
        return self._valor_economico
    @valor_economico.setter
    def valor_economico(self, nuevo_valor):    
        if isinstance(nuevo_valor, (int, float)) and nuevo_valor >= 0:
            self._valor_economico = nuevo_valor
        else:
            raise ValueError("El valor económico debe ser un número no negativo.")
    
    @property
    def fecha_creacion(self):
        return self._fecha_creacion
    @fecha_creacion.setter
    def fecha_creacion(self, nueva_fecha):      
        if isinstance(nueva_fecha, date):
            self._fecha_creacion = nueva_fecha
        else:
            raise ValueError("La fecha de creación debe ser un objeto date.")
    
    @property
    def fecha_entrada(self):
        return self._fecha_entrada  
    @fecha_entrada.setter
    def fecha_entrada(self, nueva_fecha):
        if isinstance(nueva_fecha, date):
            self._fecha_entrada = nueva_fecha
        else:
            raise ValueError("La fecha de entrada debe ser un objeto date.")
    
    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        if isinstance(nueva_descripcion, str) and nueva_descripcion.strip():
            self._descripcion = nueva_descripcion.strip()
        else:
            raise ValueError("La descripción debe ser una cadena de texto no vacía.")
    
    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, nuevo_estado):
        if isinstance(nuevo_estado, str) and nuevo_estado.strip():
            self._estado = nuevo_estado.strip()
        else:
            raise ValueError("El estado debe ser una cadena de texto no vacía.")
    
    # ── metodos_──────────────────────────────────

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado de la obra."""
        self.estado = nuevo_estado
        print(f"Obra '{self.titulo}': estado cambiado de '{nuevo_estado}'.")

    def necesita_restauracion(self):
        """Determina si la obra necesita restauración según su estado."""
        return self.estado.lower() in ["en restauración", "dañada", "en mal estado"]
    
    def ceder(self, nuevo_estado="cedida"):
        """Marca la obra como cedida."""
        self.estado = nuevo_estado
        print(f"Obra '{self.titulo}' ha sido cedida.")

    # ─ representación ───────────────────────────────────

    def __str__(self):
        return f"ObraArte(ID: {self.id_obra}, Título: '{self.titulo}', Autor: {self.autor}, Periodo: {self.periodo}, Valor: ${self.valor_economico}, Creación: {self.fecha_creacion}, Entrada: {self.fecha_entrada}, Descripción: {self.descripcion}, Estado: {self.estado})"
    
    def __repr__(self):
        return f"ObraArte(ID: {self.id_obra}, Título: '{self.titulo}', Autor: {self.autor})"
    

    







