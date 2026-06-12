from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, marca, ano,qtd_portas ):
        super().__init__(modelo, marca, ano)
        self.qtd_portas = qtd_portas
        
    def mostrar_portas(self):
        print(f"portas: {self.qtd_portas}")
        
