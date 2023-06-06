print("Elaborar um programa que contém uma lista com 5 elementos. O usuário deve preencher essa lista. Exibir no final os valores inseridos pelo usuário, porém os valores negativos (caso existirem) devem ser substituídos por zero (0).")
num=[]

for i in range (1,6):
   varNum =int(input(f'Digite o {i}º numero da lista: '))
   num.append(varNum)
   
for j in range (0,len(num)):
    if num[j] < 0:
        del num[j]
        num.insert(j,0)
    
print(f"Valores substituídos: {num}")

   
