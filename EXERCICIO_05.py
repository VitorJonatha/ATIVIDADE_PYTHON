senha1 = int(input("Digite sua senha:"))
senha2 = int(input("Digite sua senha novamente:"))

while senha1 != senha2:
    print("senhas não correspondem")
    senha2 = int(input("Digite sua senha novamente:"))
else:
    print("senhas correspondentes")
