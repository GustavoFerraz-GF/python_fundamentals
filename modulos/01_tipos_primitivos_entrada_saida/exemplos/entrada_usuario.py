#Int = 7, -4, 0, 9875
#Float = 4.5, 0.076, -15.223, 7.0
#Bool = True, False
#Str = "Olá", "7.5", " "

#print("A soma vale", s)
#print("A soma vale{s}".format(s))

'''numero1 = int(input("Digite um valor: "))
print(type(numero1))'''

numero1 = (int(input("Digite um número: ")))
numero2 = int(input("Digite mais um número "))
soma = numero1 + numero2
#print("A soma entre ", numero1, "e", numero2, "vale", soma)
print("A soma entre {} e {} vale {}".format(numero1, numero2, soma))