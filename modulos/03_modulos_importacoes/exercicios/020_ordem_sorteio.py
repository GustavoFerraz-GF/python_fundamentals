from random import shuffle
nome1 = input("Digite o nome do Primeiro aluno: ")
nome2 = input("Digite o nome do Segundo aluno: ")
nome3 = input("Digite o nome do Terceiro aluno: ")
nome4 = input("Digite o nome do Quarto aluno: ")
lista = ([nome1, nome2, nome3, nome4])
shuffle(lista)
print(f"A ordem sorteada foi {lista}")