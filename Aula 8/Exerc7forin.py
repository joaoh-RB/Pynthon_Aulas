print ("Exibição da somatoria ate n")
n = int(input("Digite o número n: "))
soma = 0
for num in range (0,n+1,1):
    soma1 = soma
    soma = num+soma
    print("O numero {} somado ao {} é igual a {}".format(num,soma1,soma))
    