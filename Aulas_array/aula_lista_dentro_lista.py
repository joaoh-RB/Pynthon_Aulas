import os
os.system('cls')

print('Receba lista de 10 pessoas e exiba a media de idade, pessoa mais nova e seu nome, maiores de idade.')

soma = 0
lista = []
lista2 = []
menor = []


for i in range (3):
    lista.append(str(input('Digite o nome: ')))
    lista.append(int(input('Digite a idade: ')))
    lista2.append(lista[:])
    lista.clear()

for i in lista2:
    print(f'Nome: {i[0]}, {i[1]} anos')
    
for e in range (0,len(lista2)):
    soma = soma + lista2[e][1]
    media = soma / len(lista2)
    
for z in range (0,len(lista2)):
    novo = lista2[z][0,1]
    menor.append(novo[1]) 
print(min(menor))
print(media)
#for i in lista2[1]:
    #soma = soma + lista2
    #print(soma)
    #media = (lista2)/len(lista2)
#print(f'A media de idade é de {media} anos')

#for i in lista2[i]:
    #novo = min(lista2[i])
    #velho = max(lista2[i])

#print(novo, velho)