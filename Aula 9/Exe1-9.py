#Em quantos anos A passa B
a = 98000000
b = 200000000
cont = 0

while a <= b:
    a = a + a * 0.035
    b = b + b * 0.015
    cont = cont + 1

print(f"O pais A passara o pais B em {cont} anos")