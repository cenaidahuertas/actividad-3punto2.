from datetime import date

class Restauracion:
    def __init__(self, obra, tipo, motivo):
        self.obra = obra
        self.tipo = tipo
        self.motivo = motivo
        self.fecha_inicio = None
        self.fecha_fin = None
        self.estado = "pendiente"

    # ── métodos ────────────────────────────────────────

    def iniciar_restauracion(self):
        """Inicia la restauración."""
        if self.estado != "pendiente":
            print(f"La restauración ya fue iniciada. Estado: '{self.estado}'.")
            return

        self.fecha_inicio = date.today()
        self.estado = "en proceso"
        print(f"Restauración de '{self.obra.titulo}' iniciada el {self.fecha_inicio}.")

    def finalizar_restauracion(self):
        """Finaliza la restauración."""
        if self.estado != "en proceso":
            print(f"La restauración no está en proceso. Estado: '{self.estado}'.")
            return

        self.fecha_fin = date.today()
        self.estado = "finalizada"
        print(f"Restauración de '{self.obra.titulo}' finalizada el {self.fecha_fin}.")

    def __str__(self):
        return (
            f"Restauracion: {self.obra.titulo} | "
            f"Tipo: {self.tipo} | "
            f"Motivo: {self.motivo} | "
            f"Estado: {self.estado} | "
            f"Inicio: {self.fecha_inicio} | "
            f"Fin: {self.fecha_fin}"
        )