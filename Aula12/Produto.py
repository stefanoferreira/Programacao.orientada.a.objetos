class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
        self.valor_total = (preco * qtd)

    def exibir_dados(self):
        print(f"""
====== INFORMAÇÕES DO PRODUTO ======
              
Nome = {self.nome}
Preço = {self.preco}
Estoque = {self.qtd}
            """)
        
    def calcular_vt(self):
        print(f"Valor Total em estoque R${self.valor_total}")
        
    
        
  
    