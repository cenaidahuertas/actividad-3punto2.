class RestauradorJefe():
    def __init__(self, id, nombre, clave):
        super().__init__(id, nombre, "restaurador jefe", clave)

    def iniciar_restauracion(self, obra, restauracion):
        obra.enviar_a_restauracion(restauracion)

    def finalizar_restauracion(self, obra, fecha_fin):
        if obra.restauraciones:
            obra.restauraciones[-1].finalizar(fecha_fin)
            obra.finalizar_restauracion(fecha_fin)

    def consultar_historial(self, obra):
        historial = sorted(obra.restauraciones, key=lambda item: item.fecha_inicio)
        return historial

    def revisar_restauraciones_programadas(self, obras, fecha_actual):
        pendientes = []
        for obra in obras:
            if obra.necesita_restauracion() or obra.necesita_restauracion_programada(fecha_actual):
                pendientes.append(obra)
        return pendientes

    def ver_catalogo(self, catalogo):
        return catalogo.listar_obras()
    