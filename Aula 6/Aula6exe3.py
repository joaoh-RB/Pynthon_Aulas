print ("Aula 6 Exercício 3");
idade= int (input("Digite a idade: "));
if (idade<0) or (idade>110):
    print("Idade Invalida");
elif (idade<16):
    print("Não-eleitor");
elif (idade>=18) and (idade<=65):
    print("Eleitor obrigatório");
else:
    print("Eleitor facultativo");