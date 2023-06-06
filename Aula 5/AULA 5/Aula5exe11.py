print ("Aula 5 Exercício 11");
kg= int (input("Digite o peso do saco de ração: "));
p1= int (input("Qual a quantidade de ração para o primeiro gato:"));
p2= int (input("Qual a quantidade de ração para o segundo gato:"));
cons= (p1+p2)*5;
sobra= kg*1000-cons;
print("Restara de ração em 5 dias",sobra,("gramas"));