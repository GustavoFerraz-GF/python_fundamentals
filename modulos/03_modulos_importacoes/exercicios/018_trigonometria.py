'''from math import radians, sin, cos, tan
angulo = float(input("Digite o Ângulo que você deseja: "))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)
print(f"O ângulo de {angulo} tem o SENO de {seno}.")
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno}.")
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente}.")'''

'''import math
angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {seno}.")
cosseno = math.cos(math.radians(angulo))
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno}.")
tangente = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente}.")'''

from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {seno}.")
cosseno = cos(radians(angulo))
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno}.")
tangente = tan(radians(angulo))
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente}.")