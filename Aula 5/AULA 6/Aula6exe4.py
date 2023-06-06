from hashlib import sha3_224


print("Aula 6 Exercício 4")

num = int(input("Digite a Opção: "))

if num >=1 and num<=4:
    s1 = float(input("Digite o primeiro número: "))
    s2 = float(input("Digite o segundo número: "))
    if num == 1:
        total = s1+s2
        print("A soma é: ", total);

    elif num == 2:
        total = s1*s2
        print("A multiplicação é: ", total);

    elif num == 3:
        total = s1-s2
        print("A subtração é: ", total);

    elif num == 4:
        if s1 == 0 or s2 == 0:
          print("Número invalido");

        else:
            total = s1/s2
            print("A subtração é: ", total);   
else:
    print("Digite uma opção valida");
