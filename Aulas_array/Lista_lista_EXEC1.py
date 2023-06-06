

import os
os.system('cls')

print("Elabore um programa em Python que realize o que se pede: - receba o nome e a nota de cada aluno(a) até receber uma informação de finalização pelo usuário; - guarde estes valores em uma lista, calcule e mostre: a média, aluno(a) com maior nota e aluno (a) com menor nota.")

lista=[]
lista2=[]
soma=0
resp="S"
while resp == "S":
    lista.append(str(input('Digite o nome: ')))
    nota = (int(input('Digite a nota: ')))
    while nota<0:
        nota = (int(input('Digite novamente a nota: ')))
    lista.append(nota)
    lista2.append(lista[:])
    lista.clear()
    resp = input("Deseja cadastrar mais alguem? S/N: ").upper()
    while resp!="S" and resp!="N":
        resp = input("Digite S/N: ").upper()
        
s = 0

for e in lista2:
    soma = soma + e[1]
media = soma / len(lista2)
print(f'A media de notas foi de {media}')

maior = menor = 0
pos = 0
posMaior = 0 

for z,y in enumerate(lista2):
    if z == 0:
        maior = menor = y[1]
        pos = 0
    else:
        if maior > y[1]:
            maior = y[1]
            posMaior = z
        if menor < y[1]:
            menor = y[1]
            pos = z

print(f'{lista2[posMaior][0]} tirou a maior nota, que foi de:{maior} ')
print(f'{lista2[pos][0]} tirou a menor nota, que foi de:{menor} ')
    