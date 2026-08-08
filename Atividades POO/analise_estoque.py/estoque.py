class ProdutosEstoque:
    def __init__(self, nome_produto, est_at, est_me):
        self.nome_produto = nome_produto
        self.est_at = est_at
        self.est_me = est_me

    def analisar_estoque(self):
        if self.est_at < self.est_me:
            print(f"Seu Estoque Precisa ser Abastecido")
        
        elif self.est_at == self.est_me:
            print(f"Seu Estoque está OK!")
        
        else:
            return False 
        
    def calcular_diferenca(self):
        diferenca = self.est_me - self.est_at
        return diferenca
    
    def apresentar_informacoes(self):
        print("===== ANÁLISE DE ESTOQUE =====")
        print(f"Nome do Produto:{self.nome_produto}")
        print(f"Estoque atual:{self.est_at}")
        print(f"Meta estoque:{self.est_me}")
        print(f"Situação:{self.analisar_estoque()}")
        print(f"Diferença para a meta:{self.calcular_diferenca()}")
