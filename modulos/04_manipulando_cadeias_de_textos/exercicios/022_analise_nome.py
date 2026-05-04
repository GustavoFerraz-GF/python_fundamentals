# Gustavo Ferraz da Conceição

nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print(f"Nome MAIÚSCULO é {nome.upper()}")
print(f"Nome minúsculo é {nome.lower()}")
print(f"Seu nome tem ao todo? {len(nome) - nome.count(' ')} letras")
#print(f"Seu primeiro nome é {nome} e ele tem {nome.find(' ')}")
separa = nome.split()
print(f"Seu primeiro nome é {(separa[0])} e ele tem {len(separa[0])} letras")