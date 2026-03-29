largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
tinta = area / 2
print(f"Sua parede tem a dimensão de {largura:.1f}x{altura:.1f} e sua área é de {area:.1f}m²,")
print(f"Para pintar essa parede, você precisará de {tinta:.1f} litros de tinta.")