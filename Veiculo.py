
#  Classe para simular o valor monitorado, veículo, cuja complexidade, de forma geral, é constante, O(1)
class Veiculo:
    def __init__(self, placa, tipo, id):
        self.placa = placa
        self.tipo = tipo
        self.id = id

    def __str__(self):
        return f"Veículo: Placa={self.placa}, Tipo={self.tipo}, Id = {self.id}"