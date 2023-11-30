import os

os.system("cls")
lst = os.listdir("c:/")
ps = 1
for i in lst:
    print(str(ps)+"º - "+i)
    ps+=1

esc = input("Digite o número correspondente a pasta que deseja ver: ")

match esc:
    case "1":
        print(os.listdir("c:/$Recycle.Bin"))
    case "2":
        print(os.listdir("c:/$WinREAgent"))
    case "3":
        print(os.listdir("c:/2379AC192CB6"))
    case "4":
        print(os.listdir("c:/Arquivos de Programas"))
    case "5":
        print(os.listdir("c:/Documents and Settings"))
    case "6":
        print(os.listdir("c:/DumpStack.log"))
    case "7":
        print(os.listdir("c:/DumpStack.log.tmp"))
    case "8":
        print(os.listdir("c:/eclipse"))
    case "9":
        print(os.listdir("c:/HashiCorp"))
    case "10":
        print(os.listdir("c:/hiperfil.sys"))
    case "11":
       print(os.listdir("c:/Intel"))
    case "12":
        print(os.listdir("c:/npm"))
    case _:
        print(os.listdir("Diretório não localizado"))