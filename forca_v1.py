import random

def escolher_palavra(): #função que define uma lista de palavras e escolhe um palavra aleatória dessa lista
    palavras = ["python", "programacao", "computador", "algoritmo", "openai", "inteligencia"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas): #função que recebe a palavra secreta e uma lisa de letras que o jogador á acertou além de montar uma string com as letras reveladas e as que ainda não foram
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogar_jogo_da_forca(): #inicia o jogo, as listas e define o número máximo de tentativas
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!") #mensagem inicial

    while tentativas > 0: #loop que o ogador fica enquanto ainda tem vidas
        print("\nPalavra:", mostrar_palavra(palavra, letras_corretas)) #mostra a palavra parcialmente revelada
        print("Tentativas Restantes:", tentativas) #mostra a quantidade de tentativas restantes
        print("Letras Erradas:", letras_erradas) #mostra a lista de letras erradas

        palpite = input("Digite uma letra: ").lower() #lê a letra e converte para minúscula

        if len(palpite) != 1 or not palpite.isalpha(): #garante que o ogador digitou apenas letras
            print("Por favor, digite apenas uma letra válida.")
            continue

        if palpite in letras_corretas or palpite in letras_erradas: #garante que o jogador não repita letras
            print("Você já tentou esta letra. Tente novamente.")
            continue

        if palpite in palavra: #se o palpite estiver na palavra, ele é adicionado à lista de letras corretas.
            letras_corretas.append(palpite)
            if len(set(letras_corretas)) == len(set(palavra)): #se o número de letras únicas acertadas for igual ao número de letras únicas na palavra, o jogador ganha.
                print("\nParabéns! Você venceu!")
                print("A palavra era:", palavra)
                break
        else:
            letras_erradas.append(palpite) #se errou, adiciona a letra à lista de erradas e diminui uma tentativa.
            tentativas -= 1
    else:
        print("\nVocê perdeu! A palavra era:", palavra) #se o loop acabar (tentativas = 0), o jogador perde e a palavra correta é revelada.

# Executar o jogo
jogar_jogo_da_forca()
