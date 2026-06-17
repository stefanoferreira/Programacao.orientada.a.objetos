from classcontabancaria import ContaBancaria

from classaluno import Aluno

aluno1 = Aluno("José", 8)
aluno1.alterar_nota(5)
aluno1.mostrar_informacoes()

conta1 = ContaBancaria("Ana", 100)
conta1.mostrar_saldo()

conta1.depositar(200)
conta1.mostrar_saldo()

conta1.sacar(150)
conta1.mostrar_saldo()
