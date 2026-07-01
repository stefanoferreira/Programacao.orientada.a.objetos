from abc import ABC, abstractmethod

class Veiculo (ABC):
    @abstractmethod
    def mover_distancia(self):
        pass
    
class Carro (Veiculo):
    def mover(self):
        print(f"O Carro percorreu 50km de distância.")
        

class Moto (Veiculo):
    def mover(self):
        print(f"A Moto percoreu 70km de distância.")
        

class Bicicleta (Veiculo):
    def mover(self):
        print(f"A Bicicleta percorreu 40km de distância.")
        

veiculos = [
    Carro (),
    Moto (),
    Bicicleta ()
]

for veiculo in veiculos:
    veiculo.mover() 


