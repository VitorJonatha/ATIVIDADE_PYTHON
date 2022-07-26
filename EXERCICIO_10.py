nome=str(input("Informe o nome: "))
while (len(nome) <= 3) or (not nome.isalpha()):
    print("O nome deve ter mais de 3 cacteres e conter apenas letras.")
    nome = str(input("informe o nome: "))

    idade=int(input("Qual a idade:"))
while (idade < 0) or (idade >150):
    print("A idade de ser entre 0 e 150.")
    idade = str(input("Informe uma idade válida: "))


    salario = float(input("Informe o salário: "))
while (salario <0):
    print("Valor invállido!")
    salario = float(input("Informe novamente um valor acima de 0 para o salário: "))


    sexo= str(input("Informe o sexo (masculino ou feminino): ")).lower()
while (sexo != "feminino") and (sexo != "masculino") and (sexo != 'f') and (sexo != 'm'):
    print("informação inválida")
    sexo = str(input("Informe o sexo (masculuno ou feminino): "))


print("Informe s para solteiro(a) , c para casado(a), v para viúvo(a) ou d para divorviado(a). ")
e_civil = str(input("Informe o estado civil: ")).lower()


while (e_civil != "s") and (e_civil != "c") and (e_civil != "v") and (e_civil != "d"):
    print("Informação inválida! Informe s para solteiro(a), c para casado(a), v para viúvo(a) ou d para divorviado(a)")
    e_civil=str(input("Informe novamente o estado civil de acordo com as orientações acima: "))