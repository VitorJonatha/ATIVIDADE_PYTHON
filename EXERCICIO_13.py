num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
res = num1
res2 = num2

if num1 <= num2:
    while res <= num2:
        print(res)
        res = res + 1
elif num1 > num2:
    while res2 <= num1:
        print(res2)
        res2 = res2 + 1
else:
    print(".")