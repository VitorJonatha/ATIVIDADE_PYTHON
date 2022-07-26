condition = True

soma = 0
numero = []
cont = 1

while condition:
    num = int(input("Digite a nota:"))
    if num != 0:
        soma += num
        numero.append(num)
        media = soma / cont
        cont = cont + 1

    else:
        break

print("Media: ",media)