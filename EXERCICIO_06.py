nota = int(input("Digite uma nota de 0 a 10:"))

while nota < 0 or nota > 10:
    print("nota inválida")
    nota = int(input("Digite uma nota de 0 a 10:"))
else:
    print("nota válida")