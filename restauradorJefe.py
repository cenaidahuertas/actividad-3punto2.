from usuario import Usuario

class RestauradorJefe(Usuario):
    def __init__(
            self,
            id_usuario,
            nombre,
            apellido,
            email,
            contrasena) -> None:

        # Llamamos al constructor del padre (Usuario)
        super().__init__(id_usuario, nombre, apellido, email, contrasena, rol="restaurador_jefe")

        # Lista con todas las restauraciones que ha gestionado
        self.restauraciones = []

    #- propiedades ───────────────────────────────────
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

    def iniciar_restauracion(self, restauracion):
        # Cambiamos el estado de la obra
        restauracion.obra.estado = "en restauracion"

        # Iniciamos la restauración
        restauracion.iniciar_restauracion()

        # La guardamos en nuestro historial
        self.restauraciones.append(restauracion)

        print(f"Restauración de '{restauracion.obra.titulo}' iniciada correctamente.")


    def finalizar_restauracion(self, restauracion):
        # Cambiamos el estado de la obra
        restauracion.obra.estado = "restaurada"

        # Finalizamos la restauración
        restauracion.finalizar_restauracion()

        print(f"Restauración de '{restauracion.obra.titulo}' finalizada correctamente.")
    
    def consultar_historial_restauraciones(self):
        print(f"Historial de restauraciones gestionadas por {self.nombre} {self.apellido}:")
        for restauracion in self.restauraciones:
            print(f"  - Obra: {restauracion.obra.titulo} | Estado: {restauracion.obra.estado} | Fecha de inicio: {restauracion.fecha_inicio} | Fecha de finalización: {restauracion.fecha_finalizacion}")
    
    #- representaciones ───────────────────────────────────
    def __str__(self):
        return f"Restaurador Jefe: {self.nombre} {self.apellido} (ID: {self.id_usuario})"
    
    def __repr__(self):
        return f"RestauradorJefe(id_usuario={self.id_usuario}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"
    
    
    