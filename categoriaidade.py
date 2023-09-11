# Obtém a idade do nadador
idad = int(input("Digite a idade do nadador: "))

# Determina a categoria com base na idade
if 5 <= idad <= 7:
    categoria = "Infantil"
elif 8 <= idad <= 10:
    categoria = "Juvenil"
elif 11 <= idad <= 15:
    categoria = "Adolescente"
elif 16 <= idad <= 30:
    categoria = "Adulto"
else:
    categoria = "Sênior"

# Exibe a categoria do nadador
print(f"O nadador de {idad} anos pertence à categoria {categoria}.")
