dias = int(input("Quantos dias alugados: "))
km_rodados = float(input("Quantos Km rodados? "))
custo_dias = dias * 60
custo_km = km_rodados * 0.15
total = custo_dias + custo_km
print(f"Custo por dias: R${custo_dias:.2f}")
print(f"Custo por Km: R${custo_km:.2f}")
print(f"Total a pagar: R${total:.2f}.")