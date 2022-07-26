num = int(input("Insira um número"))
cont = 1

if num <= 10 and num >0:
    while cont <= 10:
        res = num * cont
        print(num,"*",cont,"=",res)
        cont = cont + 1
        continue
else:
    print("número inválido")