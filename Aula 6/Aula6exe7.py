print ("Aula 6 Exercício 6");
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o segundo número: "))


if (n1 <= 0 or n2 <= 0 or n3 <=0):
    print("Digite o valor correto")

else:    
    media = n1+n2+n3/3
    
    #encontrar o menor
    if (n1 < n2):
        if (n1 < n3):
            print("O primeiro número é o menor")    
        
        else:
            print("O terceiro número é o menor") 
        
    else:
            print("O segundo número é o menor") 
       
        #encontrar o maior
    if (n1 > n2):
        if (n1 > n3):
            print("O primeiro número é o maior")    
        
        else:
            print("O terceiro número é o maior") 
        
    else:
        if (n2 > n3):
            print("O segundo número é o maior") 
        else:
            print("O terceiro número é o maior") 
            
            
        print("A média é:", media)


            
            
        
    
     

