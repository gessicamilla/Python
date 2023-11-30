import os

os.system("cls")
print("Temos dois arquivos: bloco_texto.txt e texto.txt")
print("Qual deles você deseja apagar?")
es = input("Digite: \n - 1 para bloco_texto.txt\n - 2 para texto.txt\n")
p = input("Você realmente deseja apagar o arquivo?[s:n]")

if p == "s":
    if es == "1":
        os.remove("bloco_texto.txt")
    else:
        os.remove("texto.txt")
    print("O arquivo foi apagado com sucesso!")
else:
    print("Operação cancelada")