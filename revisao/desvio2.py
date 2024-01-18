# Este programa exibe uma mensagem para os motoristas que estão com seu veículo em dia de rodízio
final_placa = input("Digite o número final da placa do su carro: ")

if(final_placa == "1" or final_placa == "2"):
    print("Seu carro está no dia de rodízio - Segunda-Feira")

elif(final_placa == "3" or final_placa == "4"):
    print("Seu carro está no dia de rodízio - Terça-Feira")

elif(final_placa == "5" or final_placa == "6"):
    print("Seu carro está no dia de rodízio - Quarta-Feira")

elif(final_placa == "7" or final_placa == "8"):
    print("Seu carro está no dia de rodízio - Quinta-Feira")

elif(final_placa == "9" or final_placa == "0"):
    print("Seu carro está no dia de rodízio - Sexta-Feira")

else:
    print("Final de placa incorreto")