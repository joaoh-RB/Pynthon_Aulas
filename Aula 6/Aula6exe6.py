print ("Aula 6 Exercício 6");
peso= int(input("Digite quantos kilos de peixe: "))


if (peso<=0):
        print("Digite o valor correto")    
    
else:
    if (peso>50):
        E= peso - 50 
        M= E * 4
        print("você excedeu o peso de", E,"kilos \n Valor da multa:",M,"reais")    
    else:
        E = "Não Excedeu o peso máximo"
        M = "Sem Multa"
        print(E,M)

    
  