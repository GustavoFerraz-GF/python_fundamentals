'''cateto_oposto = float(input("Comprimento do cateto oposto: "))
catteto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = (cateto_oposto ** 2 + catteto_adjacente ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hipotenusa:.2f}.")'''

'''import math
cateto_oposto = float(input("Comprimento do cateto oposto: "))
catteto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, catteto_adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f}.")'''

from math import hypot
cateto_oposto = float(input("Comprimento do cateto oposto: "))
catteto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(cateto_oposto, catteto_adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f}.")

'''from math import sqrt
cateto_oposto = float(input("Digite o primeiro número: "))
cateto_adjacente = float(input("Digite o segundo número: "))
hipotenusa = sqrt(cateto_adjacente ** 2 + cateto_oposto ** 2)
print(f"O Cateto Oposto é {cateto_oposto:.2f}, o Cateto Adjacente é {cateto_adjacente:.2f} e a Hipotenusa é {hipotenusa:.2f}")'''