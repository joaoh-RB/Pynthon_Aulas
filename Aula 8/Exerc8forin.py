print ("Exibição da media aritmetica de n valores lidos")
n = int(input("Digite o número de provas a ser feito a media: "))
soma = 0
for j in range (1,n+1,1):
    print("Digite a nota da ",j,"º prova: ",end="")
    num = int(input())
    soma = soma+num
    media = soma/n

print("A média é ",media)