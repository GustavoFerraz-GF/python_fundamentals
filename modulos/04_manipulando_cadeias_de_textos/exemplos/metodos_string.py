frase = "Curso em Vídeo Python" # 22 caracteres (incluindo espaços)

# =========================
# FATIAMENTO (SLICING)
# =========================

print(frase)
print(frase[9]) # Índice 9 → retorna um único caractere
print(frase[9:13]) # Do índice 9 até 12 (13 NÃO entra)
print(frase[9:14]) # Do índice 9 até 13
print(frase[9:21]) # Do índice 9 até 20
print(frase[9:21:2]) # Do índice 9 até 20, pulando de 2 em 2
print(frase[:5]) # Do início (0) até o índice 4
print(frase[15:]) # Do índice 15 até o final
print(frase[9::3]) # Do índice 9 até o final, pulando de 3 em 3

# =========================
# ANÁLISE DE STRING
# =========================

print(len(frase)) # Quantidade total de caracteres
print(frase.count("o")) # Conta quantas vezes "o" aparece
print(frase.count("o", 0, 13)) # Conta "o" entre índice 0 e 12
print(frase.find("deo")) # Retorna o índice onde começa "deo"
print(frase.find("Android")) # Retorna -1 se NÃO encontrar
print("Curso" in frase) # True se existir, False se não

# =========================
# TRANSFORMAÇÃO
# =========================

print(frase.replace("Python", "Android")) # Substitui texto
print(frase.upper()) # Tudo em MAIÚSCULO
print(frase.lower()) # Tudo em minúsculo
print(frase.capitalize()) # Primeira letra maiúscula, resto minúsculo

# =========================
# REMOÇÃO DE ESPAÇOS
# =========================

frase = "   Aprenda Python  "

print(frase.strip()) # Remove espaços das duas extremidades
print(frase.rstrip()) # Remove espaços da direita
print(frase.lstrip()) # Remove espaços da esquerda

# =========================
# DIVISÃO (SPLIT)
# =========================

frase = "Curso em Vídeo Python"

print(frase)
print(frase.split()) # Divide a string em lista usando espaço como separador

# =========================
# JUNÇÃO (JOIN)
# =========================

print("-".join(frase)) # Junta cada caractere com "-"

frase = "Curso em Vídeo Python"
palavras = frase.split()
print("-".join(palavras))

