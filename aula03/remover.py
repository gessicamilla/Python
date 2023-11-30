import os

os.system("cls")
print("Temos dois arquivos: bloco_texto.txt e TV.txt")
print("Qual deles você deseja apagar?")
es = input("Digite: \n - 1 para bloco_texto.txt\n - 2 para TV.txt\n")

if es == "1":
    os.remove("bloco_texto.txt")
else:
    os.remove("TV.txt")
print("O arquivo foi apagado com sucesso!")
