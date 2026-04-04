

from usuario import Usuario


class RestauradorJefe(Usuario):
    def __init__(self, id_usuario, nombre, apellido, email, contrasena):
        super().__init__(id_usuario, nombre, apellido, email, contrasena, rol="restaurador_jefe")
        self.restauraciones = []

    def iniciar_restauracion(self, restauracion):
        restauracion.obra.estado = "en restauracion"
        restauracion.iniciar_restauracion()
        self.restauraciones.append(restauracion)
        print(f"Restauración de '{restauracion.obra.titulo}' iniciada correctamente.")

    def finalizar_restauracion(self, restauracion):
        if restauracion.estado != "en proceso":
            print(f"La restauración no está en proceso. Estado: '{restauracion.estado}'.")
            return
        restauracion.finalizar_restauracion()
        restauracion.obra.estado = "disponible"
        print(f"Restauración de '{restauracion.obra.titulo}' finalizada correctamente.")

    def consultar_historial(self):
        if not self.restauraciones:
            print("No hay restauraciones en el historial.")
            return []
        print(f"Historial de restauraciones de {self.nombre} {self.apellido}:")
        for r in self.restauraciones:
            print(f"  - Obra: {r.obra.titulo} | Tipo: {r.tipo} | Estado: {r.estado} | Inicio: {r.fecha_inicio} | Fin: {r.fecha_fin}")
        return self.restauraciones

    def __str__(self):
        return f"Restaurador Jefe: {self.nombre} {self.apellido} (ID: {self.id_usuario})"
