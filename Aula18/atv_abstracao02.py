from abc import ABC, abstractmethod

class Documento (ABC):
    @abstractmethod
    def imprimir(self):
        pass
    
class Contrato (Documento):
    def imprimir(self):
        return super().imprimir()
    
class Nota_Fiscal (Documento):
    def imprimir(self):
        return super().imprimir()
    
class Relatorio (Documento):
    def imprimir(self):
        return super().imprimir()
    
    