# Variável de contagem
qtd = 0
for doguinho in range(1,201):
    if doguinho % 2 == 0:
        qtd = qtd + 1
print("A quantidade de números pares entre 1 e 200 é ")
print(qtd)