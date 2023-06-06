print("Elaborar um programa que receba uma lista com 10 valores numéricos, gere uma nova lista onde cada elemento dessa lista é o quadrado dos elementos da primeira lista.")
listaA=[]
listaB=[]

for i in range (1,11):
   listaA.append(int(input(f'Digite o {i}º numero da lista: ')))

for j in range (0,len(listaA)):
    quad = listaA[j] * listaA[j]
    listaB.append(quad) 
       
print(f"elementos ao quadrado da lista: {listaB}")

   
