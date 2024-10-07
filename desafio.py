def ranking(num1, num2):
    # Validação para garantir que num1 e num2 sejam maiores que 0
    while num1 < 0:
        num1 = float(input("O número deve ser maior que 0. Insira novamente: "))
    while num2 < 0:
        num2 = float(input("O número deve ser maior que 0. Insira novamente: "))

    ranking_result = num1 - num2

    # Lógica para determinar o nível
    if ranking_result < 10:
        level = "Ferro"
    elif 10 <= ranking_result <= 20:
        level = "Bronze"
    elif 20 < ranking_result <= 50:
        level = "Prata"
    elif 50 < ranking_result <= 80:
        level = "Ouro"
    elif 80 < ranking_result <= 90:
        level = "Diamante"
    elif 90 < ranking_result <= 100:
        level = "Lendário"
    else:
        level = "Imortal"

    print(f"O herói tem saldo de {ranking_result}, logo, está no nível {level}.")

# Coletando entradas do usuário
num1 = float(input("Digite o número de vitórias obtidas: "))
num2 = float(input("Digite o número de derrotas sofridas: "))

# Chamada da função
ranking(num1, num2)