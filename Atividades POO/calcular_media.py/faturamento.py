class FaturamentoSemestral:
    def __init__(self, nome_empresa, mes1, mes2, mes3, mes4, mes5, mes6):
        self.nome_empresa = nome_empresa
        self.mes1 = mes1
        self.mes2 = mes2
        self.mes3 = mes3
        self.mes4 = mes4
        self.mes5 = mes5
        self.mes6 = mes6

    def calcular_faturamento(self):
        faturamento = self.mes1 + self.mes2 + self.mes3 + self.mes4 + self.mes5 + self.mes6
        return faturamento
    
    def calcular_media(self):
        total = self.calcular_faturamento()
        media = total / 6
        return media
    
    def exibir_resultados(self):
        print("==== RELATÓRIO DA EMPRESA ====")
        print(f"Empresa:{self.nome_empresa}")
        print("---------------------------")
        print(f"Faturamento Mês 1: R${self.mes1:.2f}")
        print(f"Faturamento Mês 2: R${self.mes2:.2f}")
        print(f"Faturamento Mês 3: R${self.mes3:.2f}")
        print(f"Faturamento Mês 4: R${self.mes4:.2f}")
        print(f"Faturamento Mês 5: R${self.mes5:.2f}")
        print(f"Faturamento Mês 6: R${self.mes6:.2f}")
        print("=======================================")
        print(f"Faturamento Total:R${self.calcular_faturamento()}")
        print(f"Média Mensal:R${self.calcular_media()}")
        