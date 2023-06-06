#Exibir as seguintes listas, derivadas da lista acima.
num=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
listaMultiplos=[]
soma=0
print(f"Intervalo de 1 a 9:{num[1:10]}")
print(f"Intervalo de 8 a 13:{num[8:14]}")
print(f"Números pares:{num[::2]}")
print(f"Números Impares:{num[1::2]}")
print(f"Números Impares:{num[1::2]}")
print(f"Todos os múltiplos de 2, 3 e 4:",end="")

for i in (num[1::]):
    if i%2 == 0 or i%3 == 0:
       listaMultiplos.append(i)
print(listaMultiplos)

print(f"Lista reversa:{num[::-1]}")

print(f"Soma do intervalo de 10 a 15:",end="")
for i in (num[10:16]):
       soma = soma+num[i]      
print(soma)

varNum =(int(input(f'Digite um novo numero na lista: ')))
num.append(varNum)
print(f"Uma lista com um novo elemento {num}")


num.insert(5,varNum)
print(f"Substituir o elemento com índice 6: {num}")
