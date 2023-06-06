print ("Aula 6 Exercício 5");
hosp= str(input("Digite o nome do hospede: "))

if (hosp.isalpha()):
    tpa= input("Qual tipo de AP o hospede ficou\nA- 150,00\nB- 100,00\nC- 75,00\nD- 50,00\nDigite a opção desejada: ")
    if (tpa=="A" or tpa=="a"):
        vd= 150
    elif (tpa=="B" or tpa=="b"):
        vd= 100
    elif (tpa=="C" or tpa=="c"):
        vd= 75
    elif (tpa=="D" or tpa=="d"):
        vd= 50
    else:
        exit("Opcao invalida")
else:
    exit("Nome Invalido")
    
diar= int(input("Quantos dias o hospede se hospedou: "))

vc= int(input("Digite o valor consumido: "))
 
vtd = diar*vd
subt = vtd+vc
tx = subt*10/100
vts = subt*10/100+subt
vt = vts+subt
print("Nome do hospede: ",hosp,"\nTipo do apartamento: ",tpa,"\nNumero de diarias: ",diar,"\nValor unitario da diaria: ",vd,"\nValor total das diarias: ",vtd,"\nValor do Consumo: ",vc,"\nSubtotal: ",subt,"\nTaxa de Servico: ",tx,"\nTotal da despesa: ",vt)
