class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(F"Depósito de R$ {valor:.2f}, realizado com suceso.")
            
        else:
            print(f"O valor do depósito deve ser maior que zero.")
            
    def sacar(self, valor):
        if valor <= 0:
            print(f"O valor do saque deve ser maiior que zero.")
        elif valor <= self.__saldo:
            print(f"Saque de R$ {valor:.2f}, realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
            
    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")