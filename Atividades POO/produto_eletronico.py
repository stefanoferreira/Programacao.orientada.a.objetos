class ProdutoEletronico:
    def __init__(self, nome, pc, pl):
        self.nome = nome
        self.pc = pc
        self.pl = pl
    
    def calcular_preco_venda(self):
        lucro = self.pc * self.pl/100
    
    def calcular_preco_venda(self):
        return self.pc * (1+self.pl/100)
            
    
    def apresentar_informacoes(self):
        print(f"=== PRODUTOS ELETRÔNICOS ===")
        print(f"Produto:{self.nome}")
        print(f"Preço de Custo:R${self.pc:.2f}")
        print(f"Percentual de Lucro:{self.pl}%")
        print(f"Preço de Venda:R${self.calcular_preco_venda():.2f}")
    
    