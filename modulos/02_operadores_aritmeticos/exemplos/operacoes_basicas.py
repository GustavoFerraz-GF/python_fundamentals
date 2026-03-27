# Operadores

# + Adição, - Subtração, * Multiplicação, / Divisão, ** Potência, // Divisão inteira, % Resto da Divisão

# 5 +  2 == 7, 5 -  2 == 3, 5 *  2 == 10, 5 /  2 == 2.5, 5 ** 2 == 25, 5 // 2 == 2, 5 %  2 == 1

# Ordem de Precedência

# 1ª () - 2ª ** - 3ª *, /, //, % - 4ª +, - 

# 5 + 3 * 2 == 11
# 3 * 5 + 4 ** 2 == 31
# 3 * (5 + 4) ** 2 == 243

#nome = input("Qual é o seu nome? ")
#print("Prazer em te conhecer {}".fomart(nome))

# numero1 = int(input("Um valor: "))
# numero2 = int(input("Outro valor: "))
# print(f"A soma vale {numero1 + numero2}")

numero1 = int(input("Um valor: "))
numero2 = int(input("Outro valor: "))
soma = numero1 + numero2
multi = numero1 * numero2
divisão = numero1 / numero2
diviso_int = numero1 // numero2
potencia = numero1 ** numero2
print(f"A soma é {soma}, o produto é {multi} e a divisão é {divisão:.3f}", end=" ")
print(f"Divisão inteira {diviso_int} e potência {potencia}")