
class Visitante():
    def __init__(self, id, nombre, clave):
        super().__init__(id, nombre, "visitante", clave)

    def consultar_obras_por_sala(self, catalogo, nombre_sala):
        return catalogo.listar_obras_por_sala(nombre_sala)

    def consultar_fechas_exposicion(self, exposicion):
        return f"Inicio: {exposicion.fecha_inicio} | Fin: {exposicion.fecha_fin}"
