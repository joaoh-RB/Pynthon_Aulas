print ("Aula 6 Exercício 4");
opcao= int (input('''Menu de Opções:\n 
1- Somar dois numeros
2- Multiplicar dois números
3- Subtrair dois números
4- Dividir dois números 
\nDigite a opção desejada: '''));
if (opcao==1):
    n1= float(input("Digite o primeiro numero: "))
    n2= float(input("Digite o segundo numero: "))
    x= n1+n2
    print("Resultado da soma: ", x)
elif (opcao==2):
    n1= float(input("Digite o primeiro numero: "))
    n2= float(input("Digite o segundo numero: "))
    x= n1*n2
    print("Resultado da multiplicação: ", x)
elif (opcao==3):
    n1= float(input("Digite o primeiro numero: "))
    n2= float(input("Digite o segundo numero: "))
    x= n1-n2
    print("Resultado da subtração: ", x)
elif (opcao==4):
    n1= float(input("Digite o primeiro numero: "))
    n2= float(input("Digite o segundo numero: "))
    if(n1==0 or n2==0):
        print("Numero Invalido")
    else:
        x= n1/n2
        print("Resultado da divisão: ", x)
else:
    print("Opção Invalida!")