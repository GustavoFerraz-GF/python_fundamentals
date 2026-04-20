'''import random
nome1 = input("Primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("uarto aluno: ")
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f"O aluno escolhido foi {escolhido}")'''

from random import choice
nome1 = input("Primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("Quarto aluno: ")
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print(f"O aluno escolhido foi {escolhido}")