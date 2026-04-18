from math import radians, sin, cos, tan
numero = float(input("Digite o valor do Ângulo: "))
radiano = radians(numero)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)
print(f"O valor digitado foi {numero:.0f}°, e valor de SENO é {seno:.2f}, o valor de COSSENO é {cosseno:.2f} e o valor do TANGENTE é {tangente:.2f}")
