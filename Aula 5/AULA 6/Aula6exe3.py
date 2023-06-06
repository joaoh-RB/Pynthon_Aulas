print ("Aula 6 Exercício 3");

idade= int(input("Digite a idade: "));

if idade < 1 or idade > 120 :
    print ("Digite uma idade válida");
    
elif idade < 16:
    print ("Não Eleitor");
   
elif idade >= 18 and idade <= 65:
    print ("Eleitor Obrigatório");
   
else:
    print ("Eleitor Facultativo");


