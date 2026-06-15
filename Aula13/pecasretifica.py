class PecasRetifica:
   
  def __init__(self, nome, pc, pl):
      self.nome = nome,
      self.pc = pc,
      self.pl = pl

#Calcule o Valor do Lucro

  def preco_venda(self):
      preco_venda = self.pc * self.pl/100

#Retorne o Preço de Venda Somando custo + Lucro

  def apresentar_dados(self):
      print("=== PECAS PARA RETIFICA ===") 
      print("Peça: {self.nome}")
      print("Preço de custo: R${self.pc}")
      print("Percentual de Lucro:{self.pl}%")
      print("Preço de Venda: R${self.preco_venda}")


        