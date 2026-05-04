'''numero = str(input("Digite um número: ")).zfill(4)
print(f"Unidade: {numero[-1]}")
print(f"Dezena: {numero[-2]}")
print(f"Centena: {numero[-3]}")
print(f"Milhar: {numero[-4]}")'''

numero = int(input("Digite um número: "))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")

'''numero = int(input("Informe um número: "))
n = str(numero)
print(f"Analisando o número {numero}.")
print(f"Unidade {n[3]}")
print(f"Dezena {n[2]}")
print(f"Centena {n[1]}")
print(f"Unidade {n[0]}")'''