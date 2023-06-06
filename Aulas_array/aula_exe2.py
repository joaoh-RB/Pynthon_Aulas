print("Elaborar um programa que leia uma lista de 6 números inteiros e mostre cada número juntamente com a sua posição na lista.")
num=[]

for i in range (1,7):
   varNum =int(input(f'Digite o {i}º numero da lista: '))
   num.append(varNum)

for j in range (0,len(num)):
    
    print(f"O {j+1}º item da lista tem o valor de {num[j]}")
    

   
