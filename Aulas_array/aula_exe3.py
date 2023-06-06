print("Elaborar um programa que leia uma lista com 4 números reais, em seguida o programa deve exibir os números e a média.")
num=[]
soma = 0
total=0

for i in range (1,5):
   varNum =int(input(f'Digite o {i}º numero da lista: '))
   num.append(varNum)

for j in range (0,len(num)):
    soma = soma + num[j]
    total = soma / len(num)
    print(f"O {j+1}º item da lista tem o valor de {num[j]}")

print(f"A média dos números é de: {total}")

   
