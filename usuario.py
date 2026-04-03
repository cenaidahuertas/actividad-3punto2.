class Usuario:
    def __init__(self, id, nombre, rol, clave):
        self.id = id
        self.nombre = nombre
        self.rol = rol
        self.clave = clave

    def autenticar(self, clave):
        return self.clave == clave

    def mostrar_datos(self):
        return f"Usuario: {self.nombre} | Rol: {self.rol}"


class Director(Usuario):
    def __init__(self, id, nombre, clave):
        super().__init__(id, nombre, "director", clave)

    def calcularValorTotal(self, obras):
        total = 0
        for obra in obras:
            total += obra.valor_economico
        return total

    def gestionarCesion(self, museo, cesion):
        museo.registrar_cesion(cesion)
        cesion.iniciar_cesion()

    def verObrasEnRestauracion(self, museo):
        return [o for o in museo.obras if o.estado == "EN_RESTAURACION"]

    def verObrasCedidas(self, museo):
        return [o for o in museo.obras if o.estado == "CEDIDA"]


class RestauradorJefe(Usuario):
    def __init__(self, id, nombre, clave):
        super().__init__(id, nombre, "restaurador jefe", clave)

    def revisarRestauraciones(self, obras, fecha_actual):
        pendientes = []
        for obra in obras:
            if obra.necesita_restauracion() or obra.necesita_restauracion_programada(fecha_actual):
                pendientes.append(obra)
        return pendientes

    def decidir_envio_restauracion(self, obra, decision, restauracion):
        if decision:
            obra.enviarARestauracion(restauracion)
            return f"Obra '{obra.titulo}' enviada a restauracion."
        return f"Obra '{obra.titulo}' no enviada a restauracion."

    def finalizarRestauracion(self, obra, fecha_fin):
        if obra.restauraciones:
            obra.restauraciones[-1].finalizar(fecha_fin)
            obra.finalizar_restauracion(fecha_fin)

    def consultarHistorial(self, obra):
        historial = sorted(obra.restauraciones, key=lambda item: item.fecha_inicio)
        return historial


class Visitante(Usuario):
    def __init__(self, id, nombre, clave):
        super().__init__(id, nombre, "visitante", clave)

    def consultarObrasPorSala(self, catalogo, nombre_sala):
        return catalogo.listar_obras_por_sala(nombre_sala)
