from random import choice
nome1 = input("Digite o nome do Primeiro aluno: ")
nome2 = input("Digite o nome do Segundo aluno: ")
nome3 = input("Digite o nome do Terceiro aluno: ")
nome4 = input("Digite o nome do Quarto aluno: ")
sorteio = choice([nome1, nome2, nome3, nome4])
print(f"O nome sorteado foi {sorteio}")