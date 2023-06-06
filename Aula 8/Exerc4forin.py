print ("Calculo do quadrado de N valores lidos")
n = int(input("Digite quantos números deseja calcular: "))
for j in range (1,n+1,1):
    print("Digite o ",j,"º número: ",end="")
    num = int(input())
    quad = num * num
    print("O quadrado de ",num,"é de ",quad)
    
    