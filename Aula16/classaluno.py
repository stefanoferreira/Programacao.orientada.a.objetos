class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome,
        self.__nota = nota

    def alterar_nota(self, nova_nota):
        if nova_nota > 0 :
            self.__nota += nova_nota
            print(f"Sua Nota é Válida!")
        
        elif nova_nota < 10 :
            print(f"Sua Nota é Válida!")
            
        else:
            print(f"Nota Inválida.")
            
    def mostrar_informacoes(self):
        print(f"""
    === INFORMAÇÕES DO ALUNO ===
    "Aluno" = {self.nome}
    "Nota" = {self.__nota} 
              """)

    @property
    def nota(self):
        return self.__nota
