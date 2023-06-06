print("Elaborar um programa que leia uma lista que contenha 20 números inteiros e em seguida o programa deve exibir o maior e o menor número.")
num=[]

for i in range (1,6):
   varNum =int(input(f'Digite o {i}º numero da lista: '))
   num.append(varNum)
   
menor = min(num)
maior = max(num)
print(f"O maior número da lista é {maior} e o menor número é {menor}")

   
