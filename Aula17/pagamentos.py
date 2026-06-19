class Financeiro:
    def __init__(self):
        print(f"METODOS DE PAGAMENTOS")
    


class PagamentoPix:
    def pagar(self, valor):
        self.valor = valor
        print(f"Pagamento via Pix realizado no valor de R$ {self.valor:.2f}.")
        
class PagamentoCartao:
     def pagar(self, valor):
        self.valor = valor
        print(f"Pagamento no Cartão aprovado no valor de R$ {self.valor:.2f}.")

class PagamentoBoleto:
     def pagar(self, valor):
        self.valor = valor
        print(f"Boleto gerado no valor de R$ {self.valor:.2f}. Aguardando pagamento.")
        
pagamentos = [PagamentoPix(), PagamentoCartao(), PagamentoBoleto()]

Financeiro()

for pagamento in pagamentos:
    pagamento.pagar(150)    
    
