from ClassAluno import Aluno
from ClassLivros import Livros

aluno1 = Aluno("Joaquim", 32, 1, [7, 8, 8.5, 9], "A")

aluno2 = Aluno("Manoel", 35, 2, [8, 8, 9, 9,], "B")

aluno3 = Aluno("Carlos", 28, 3, [7.5, 8, 9.5, 9], "C")
print(
      aluno1.nome,
      aluno1.idade,
      aluno1.matricula,
      aluno1.notas,
      aluno1.turma
      )

print(
    aluno2.nome,
    aluno2.idade,
    aluno2.matricula,
    aluno2.notas,
    aluno2.turma
    )

print(
    aluno3.nome,
    aluno3.idade,
    aluno3.matricula,
    aluno3.notas,
    aluno3.turma
    )


livro1 = Livros("Gatilhos Mentais","Gustavo Ferreira","Livre")