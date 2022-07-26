
nome = str(input("Digite seu nome:"))
senha = str(input("Digite sua senha:"))

while nome == senha:
    print("senha e nome não podem ser iguais")
    nome = str(input("Digite seu nome:"))
    senha = str(input("Digite sua senha:"))
else:
    print("usuário cadastrado")
