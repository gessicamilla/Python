import os

os.system("clear")
os.system("rm -r dados_info")
os.mkdir("dados_info")
os.chdir("dados_info")
ar = open("texto.txt","x")
ar.write("Lavender Hazel")
ar.close()
print(os.getcwd())
print("Diretório criado, aberto e com arquivo")