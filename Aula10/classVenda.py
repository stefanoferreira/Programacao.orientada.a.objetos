#Representar a venda de 1 tipo de produto


class Venda():
    def __init__(self, nome_produto, preco_produto, qtd_produto, nome_vendedor,
                 nome_loja):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.qtd_produto = qtd_produto
        self.nome_vendedor = nome_vendedor
        self.nome_loja = nome_loja
        
        
        self.total_venda = round(preco_produto * qtd_produto,2)

    
    def mostrar_informacoes (self):
        print(f"""
Nome: {self.nome_produto}
Quantidade: {self.qtd_produto}
total: R$ {self.total_venda:2f}
""")
    
    def alterar_qtd(self, nova_qtd):
        if nova_qtd > 0:
            self.qtd_produto = nova_qtd
            
            self.atualizar_total()
            
            return True
        
        else:
            print("Tentativa de alterar quantidade com números inválidos!")
            return False
        
    def alterar_preco(self, novo_preco):
            if novo_preco > 0:
                
                self.preco_produto = novo_preco
                
                self.atualizar_total()
                return True
            
            else:
                print("Tentativa de alterar o preço com nùmero inválido!")
                return False
            
    def atualizar_total(self):
                
                self.total_venda = round(self.qtd_produto * self.preco_produto, 2)
                
if __name__ == "__main__":
        
    venda_teste = Venda("TV 52' LG SMART", 2000, 1, "Vinicius", "Magazine Luiza")
        
    venda_teste.alterar_preco(2000*0.9)                
        
    venda_teste.mostrar_informacoes()