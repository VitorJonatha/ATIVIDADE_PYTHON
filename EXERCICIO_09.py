soma = 0
quantidade = 0
while True:
    num = int(input("Digite números inteiros. Para sair do loop digite 0:"))
    if num == 0:
        break
    soma = soma + num
print("soma: ", soma)