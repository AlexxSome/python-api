class Facturas:
    def __init__(self, id, paciente_id, descripcion, monto, fecha_emision):
        self.id = id
        self.paciente_id = paciente_id
        self.descripcion = descripcion
        self.monto = monto
        self.fecha_emision = fecha_emision