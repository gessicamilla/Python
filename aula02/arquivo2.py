import os
os.system("clear")

arq = open("./arquivos/dados.csv","a")
nome = input("Digite o seu Nome: ")
email = input("Digite o seu Email: ")
arq.write(nome+";"+email+"\n")
arq.close()