print ("Aula 5 Exercício 9");
hrtb= int (input("Digite horas trabalhadas: "));
salm= float (input("Digite o salario minimo: "));
vhr= salm/2;
salb= hrtb*vhr;
imp= salb*3/100;
salrec= salb-imp;
print ("Salario a receber: ", salrec, ("reais"));