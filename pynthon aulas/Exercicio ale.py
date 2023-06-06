import os
os.system('cls')

print('Receba lista de 10 pessoas e exiba a media de idade, pessoa mais nova e seu nome, maiores de idade.')

soma = 0
lista = []
lista2 = []
resp = "S"


while resp == "S":
    lista.append(str(input('Digite o nome: ')))
    idade = (int(input('Digite a idade: ')))
    while idade<1 or idade>120:
        idade = (int(input('Digite novamente a idade: ')))
    lista.append(idade)
    lista2.append(lista[:])
    lista.clear()
    resp = input("Deseja cadastrar mais alguem? S/N: ").upper()
    while resp!="S" and resp!="N":
        resp = input("Digite S/N: ").upper()
        
s = 0
    
for i in lista2:
    print(f'Nome: {i[0]}, {i[1]} anos')

for e in lista2:
    soma = soma + e[1]
media = soma / len(lista2)
print(f'A media de idades é de {media} anos')

maior = menor = 0
pos = 0

for z,y in enumerate(lista2):
    if z == 0:
        maior = menor = y[1]
        pos = 0
    else:
        if maior < y[1]:
            menor = y[1]
        if menor > y[1]:
            menor = y[1]
            pos = z

print(f'A menor idade é {menor} e o nome é {lista2[pos][0]}')
print(f'A maior idade é {maior}')
    