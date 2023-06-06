print("Elaborar um programa para ler uma lista A de 15 elementos e um valor X. O programa deve copiar para a lista B somente os elementos de A que são maiores que X. Exibir no final a lista B. ")
listaA=[]
listaB=[]

for i in range (1,16):
   varNum =int(input(f'Digite o {i}º numero da lista: '))
   listaA.append(varNum)

varX =int(input(f'Digite o valor de x número da lista: '))

for j in range (0,len(listaA)):
    if listaA[j] > varX:
       listaB.append(listaA[j]) 
       
print(f"elementos de A que são maiores que X: {listaB}")

   
