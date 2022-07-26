ved = 'verde'
vem = 'vermelho'
ama = 'amarelo'
cor = str(input("Digite a cor do semáforo:"))

if cor == ved:
    print("PODE PASSAR!")
elif cor == vem:
    print("NÃO PODE PASSAR!")
elif cor == ama:
    print("ATENÇÃO!")
else:
    print("Cor errada")