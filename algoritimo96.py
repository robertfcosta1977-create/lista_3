""" Entrar com um número e informar se ele é divisível por 3 e por 7. """

numero=int(input("Digite um numero: "))
if numero % 3 == 0:
    print("esse numero é divisivel por 3")
elif numero % 7 == 0:
    print("Esse numero é divisivel por 7")
else:
    print("Náo é divisivel nem por 3 nem por 7 ")