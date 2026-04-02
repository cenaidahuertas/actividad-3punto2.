class Director():
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