class Produto:
    
    def __init__(self, nome_produto, preco_produto, qtd_produto ):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.qtd_produto = qtd_produto
        
        self.valor_total = round(preco_produto * qtd_produto)
        
        
    def mostrar_dados(self):
        print(f"""
Nome: {self.nome_produto}
Preço: {self.preco_produto}
Estoque: {self.qtd_produto}
 """)
        
    def aplicar_desconto(self):
        if desconto > (10%) :
            return false
            
        
    if __name__ == "__main__":
        
        produto1 = "Produto"("retentor", 60, 100)
        produto1.mostrar_dados()
        produto1.valor_total()
        produto1.aplicar_desconto()
        
        