def wordCounter():
    """
    Conta o número de palavras em uma frase digitada pelo usuário.

    Solicita uma frase para o usuário, calcula as palavras com base nos espaços entre elas e retorna a quantidade.

    Returns:
        int: O número de palavras na frase fornecida pelo usuário.
    """
    string = input("Digite uma frase: ")
    return len(string.split())

print(wordCounter())