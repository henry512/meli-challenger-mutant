class DNASequenceException(Exception):
    def __init__(self):
        super().__init__(self, "ADN no valido")


class DNASequenceValuesException(Exception):
    def __init__(self):
        super().__init__(self, "Valores de ADN no validos")