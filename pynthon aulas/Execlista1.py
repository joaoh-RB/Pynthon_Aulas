import os
os.system('cls')

print('Receba o nome e a nota de cada aluno(a) até receber uma informação de finalização pelo usuário; - guarde estes valores em uma lista, calcule e mostre: a média, aluno(a) com maior nota e aluno (a) com menor nota.')

soma = 0
lista = []
lista2 = []
resp = "S"


while resp == "S":
    lista.append(str(input('Digite o nome do aluno: ')))
    nota = (int(input('Digite a nota: ')))
    while nota<0 or nota>10:
        nota = (int(input('Digite novamente a nota: ')))
    lista.append(nota)
    lista2.append(lista[:])
    lista.clear()
    resp = input("Deseja cadastrar mais alguma nota? S/N: ").upper()
    while resp!="S" and resp!="N":
        resp = input("Digite S/N: ").upper()
        
s = 0
    
for i in lista2:
    print(f'Nome: {i[0]}, {i[1]}')

for e in lista2:
    soma = soma + e[1]
media = soma / len(lista2)
print(f'Nota media da sala: {media}')

maior = 0
menor = 0
pos = 0
posi = 0

for z,y in enumerate(lista2):
    if z == 0:
        maior = menor = y[1]
        pos = 0
        posi = 0
    else:
        if maior < y[1]:
            maior = y[1]
            posi = z
        if menor > y[1]:
            menor = y[1]
            pos = z

print(f'{lista2[pos][0]} obteve a menor nota que foi {menor}')
print(f'{lista2[posi][0]} obteve a maior nota que foi {maior}')