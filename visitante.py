from usuario import Usuario

class Visitante(Usuario):
 
    def __init__(
            self,
            id_usuario,
            nombre,
            apellido,
            email,
            contrasena):
        
        # Llamamos al constructor del padre (Usuario)
        super().__init__(id_usuario, nombre, apellido, email, contrasena, rol="visitante")


    # - propiedades ─────────────────────────────────── 
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido   
    
    @property
    def email(self):
        return self._email
    
    @property
    def contrasena(self):
        return self._contrasena
    
    # - metodos ───────────────────────────────────

    def consultar_obra_en_sala(self, obra):
        obras = sala.listar_obras()

        if not obras:
            print(f"La sala '{sala.nombre}' no tiene obras disponibles.")
            return []

        print(f"Obras disponibles en la sala '{sala.nombre}':")
        for obra in obras:
            print(
                f"  - {obra.titulo} | "
                f"Autor: {obra.autor} | "
                f"Período: {obra.periodo}"
            )

        return obras
    
    # - representación ───────────────────────────────────
    def __str__(self):
        return f"Visitante: {self.nombre} {self.apellido} (Email: {self.email})"
    
    
