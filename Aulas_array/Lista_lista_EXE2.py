import os
os.system('cls')

print("Elaborar um programa em Python que leia os nomes e telefones de 20 pessoas e armazene numa lista. A partir de uma consulta por nome, o programa deverá mostrar o NOME e TELEFONE da pessoa.")

lista=[]
lista2=[]
soma=0
resp="S"
while resp == "S":
    lista.append(str(input('Digite o nome: ')))
    lista.append(int(input('Digite a telefone: ')))
    lista2.append(lista[:])
    lista.clear()
    resp = input("Deseja cadastrar mais alguem? S/N: ").upper()
    while resp!="S" and resp!="N":
        resp = input("Digite S/N: ").upper() 
        
s = 0
pos=0
pos2=0

resp2="S"
while resp2 == "S":
    name = (str(input("Digite o nome para consulta desejado?")))

    for j,k in enumerate(lista2):
        if name in lista2[j][0]:
            print(f"O número de {k[0]} é {k[1]}")
            break
        else:
            print("Nome não registrado.")
            break
            
    
    resp2 = input("Deseja consultar mais algum número? S/N: ").upper()
    while resp2!="S" and resp2!="N":
        resp2 = input("Digite S/N: ").upper() 
        
    
    
