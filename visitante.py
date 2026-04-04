
from usuario import Usuario


class Visitante(Usuario):
    def __init__(self, id_usuario, nombre, apellido, email, contrasena):
        super().__init__(id_usuario, nombre, apellido, email, contrasena, rol="visitante")

    def consultar_obras_por_sala(self, sala):
        obras = sala.listar_obras()

        if not obras:
            print(f"La sala '{sala.nombre}' no tiene obras disponibles.")
            return []

        print(f"Obras disponibles en la sala '{sala.nombre}':")
        for obra in obras:
            print(f"  - {obra.titulo} | Autor: {obra.autor} | Período: {obra.periodo}")

        return obras

    def __str__(self):
        return f"Visitante: {self.nombre} {self.apellido} (Email: {self.email})"
