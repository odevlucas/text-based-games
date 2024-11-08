import random

def jogar():
    tutorial = f"""
    Vamos brincar de adivinhar o número!
    Você dirá um intervalo de número, eu escolherei um número nesse intervalo e você tentará adivinhar qual número escolhi.
    Solicitarei o intervalo para você, por ex: De 1 a 10
    """
    print(tutorial)

    valor_inicial = int(input("Insira o valor inicial (Ex: 1): "))
    valor_final = int(input("Insira o valor final (Ex: 10): "))

    numero_aleatorio = random.randint(valor_inicial, valor_final)

    print(f"Eu escolhi um número entre o {valor_inicial} e {valor_final}. Tente adivinhar!")


    while True:
        tentativa_user = int(input("O número que eu pensei é: "))

        if tentativa_user < numero_aleatorio:
            print("Não foi dessa vez, eu pensei em um número maior!")
        elif tentativa_user > numero_aleatorio:
            print("Não foi dessa vez, eu pensei em un número menor!")
        else:
            print(f"Parabéns! Você acertou! O número era: {numero_aleatorio} ")
            break
while True:
    jogar()
    jogar_novamente = input("Deseja jogar novamente? S/N: ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima!")
        break