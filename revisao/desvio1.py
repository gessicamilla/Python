# Este programa obtem o nome do aluno e a nota média
# Se o aluno tiver uma nota média acima ou igual a 6 estará Aprovado; caso contrário Reprovado
nome = input("Digite o nome do aluno: ")
media = input("Digite a nota média do aluno: ")
media = float(media)

if(media>=6):
    print("Aprovado")
else:
    print("Reprovado")