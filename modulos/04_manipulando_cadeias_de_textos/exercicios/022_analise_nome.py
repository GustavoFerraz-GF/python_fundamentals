# Gustavo Ferraz da Conceição

nome = input("Digite seu nome completo: ")
print(f"Nome MAIÚSCULO: {nome.upper()}")
print(f"Nome minúsculo: {nome.lower()}")

palavra = nome.split()
letras = "".join(palavra)
print(f"Quantidade letras ao todo? {len(letras)}")
print(f"Quantidade de letras no 1º nome: {len(palavra[0])}")