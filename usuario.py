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

    def calcular_valor_total(self, obras):
        total = 0
        for obra in obras:
            total += obra.valor_economico
        return total

    def gestionar_cesion(self, museo, cesion):
        museo.registrar_cesion(cesion)
        cesion.iniciar_cesion()

    def ver_catalogo(self, catalogo):
        return catalogo.listar_obras()


class RestauradorJefe(Usuario):
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

class Visitante(Usuario):
    def __init__(self, id, nombre, clave):
        super().__init__(id, nombre, "visitante", clave)

    def consultar_obras_por_sala(self, catalogo, nombre_sala):
        return catalogo.listar_obras_por_sala(nombre_sala)

    def consultar_fechas_exposicion(self, exposicion):
        return f"Inicio: {exposicion.fecha_inicio} | Fin: {exposicion.fecha_fin}"
