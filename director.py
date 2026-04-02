from usuario import Usuario

class Director(Usuario):
    class EncargadoCatalogo(Usuario):
        pass

    def __init__(
        self,
        id_usuario,
        nombre,
        apellido,
        email,
        contrasena,) -> None:

        # Llamamos al constructor del padre (Usuario)
        super().__init__(id_usuario, nombre, apellido, email, contrasena, rol="director")

        self.cesiones = []
        
    # - id_usuario ───────────────────────────────────
    @property
    def id_usuario(self):
        return self._id_usuario

    # - nombre ───────────────────────────────────
    @property
    def nombre(self):
        return self._nombre

    # - apellido ───────────────────────────────────
    @property
    def apellido(self):
        return self._apellido

    # - email ───────────────────────────────────
    @property
    def email(self):
        return self._email  

    # - contrasena ───────────────────────────────────
    @property
    def contrasena(self):
        return self._contrasena

    #- rol ───────────────────────────────────
    @property
    def rol(self):
        return self._rol

    # - metodos ───────────────────────────────────
    def gestionar_cesiones(self, cesion):
        self.cesiones.append(cesion)
        print(f"Cesión '{cesion}' gestionada correctamente.")

    def calcular_valor(self):
        total = 0
        for cesion in self.cesiones:
            total += cesion.obra.valor_economico
        print(f"Valor total de obras en cesión: ${total}")
        return total

    #- ver catalogo ───────────────────────────────────
    def ver_catalogo(self, catalogo):
        obras = catalogo.listar_obras()

        if not obras:
            print("El catálogo no tiene obras registradas.")
            return

        print("Obras en el catálogo:")
        for obra in obras:
            print(f"  - {obra.titulo} | Autor: {obra.autor} | Estado: {obra.estado}")

    #- revisar cesiones ───────────────────────────────────
    def ver_cesiones_activas(self):
        if not self.cesiones:
            print("No hay cesiones activas.")
            return

        print("Cesiones activas:")
        for cesion in self.cesiones:
            print(f"  - Obra: {cesion.obra.titulo} | Cesionario: {cesion.cesionario.nombre} | Fecha de inicio: {cesion.fecha_inicio}")


# - representaciones ───────────────────────────────────
    def __str__(self):
        return f"Director: {self.nombre} {self.apellido} (ID: {self.id_usuario})"
    
    def __repr__(self):
        return f"Director(id_usuario={self.id_usuario}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"
    
    