num = int(input("Digite um número de 1 a 10:"))
cont = 1
if num <= 10 and num >0:
    while cont <= 10:
        res = num * cont
        print(num,"*",cont,"=",res)
        cont = cont + 1
else:
    print("número inválido")