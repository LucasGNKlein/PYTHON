import random

def escolher_palavra(genero):  # Define uma palavra aleatória com base no gênero
    palavras_por_genero = {
        "animais": ["gato", "elefante", "rato", "corvo", "gralha", "formiga", "porco", "galinha", "peixe", "tubarão"],
        "frutas": ["uva", "laranja", "ameixa", "caqui", "tomate", "morango", "banana", "caju", "framboesa", "melão", "melancia"],
        "tecnologia": ["python", "computador", "algoritmo", "inteligencia", "programacao", "chamado", "codar", "suporte", "software", "hardware"],
        "países": ["brasil", "canada", "japao", "alemanha", "argentina", "egito", "franca"],
        "cores": ["vermelho", "azul", "amarelo", "verde", "roxo", "preto", "branco"],
        "esportes": ["futebol", "basquete", "tenis", "volei", "natacao", "ciclismo", "boxe"],
        "filmes/séries": ["supernatural", "harry potter", "indiana jones", "star wars", "vingadores"]
    }

    if genero not in palavras_por_genero:
        print("Gênero inválido. Usando 'tecnologia' por padrão.")
        genero = "tecnologia"

    return random.choice(palavras_por_genero[genero])

def mostrar_palavra(palavra, letras_corretas):  # Mostra a palavra com letras acertadas e underscores
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogar_jogo_da_forca():
    letras_corretas = []
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")

    # Gêneros disponíveis
    palavras_por_genero = {
        "animais": [],
        "frutas": [],
        "tecnologia": [],
        "países": [],
        "cores": [],
        "esportes": [],
        "filmes/séries": []
    }

    print("\nCategorias disponíveis:")
    for genero in palavras_por_genero:
        print(f"- {genero.capitalize()}")

    # Escolha do gênero
    genero_escolhido = ""
    while True:
        genero_escolhido = input("\nDigite o gênero desejado: ").lower()
        if genero_escolhido in palavras_por_genero:
            break
        else:
            print("❌ Gênero inválido. Por favor, escolha um dos gêneros disponíveis.")

    palavra = escolher_palavra(genero_escolhido)

    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavra, letras_corretas))
        print("Tentativas Restantes:", tentativas)
        print("Letras Erradas:", letras_erradas)

        palpite = input("Digite uma letra ou tente adivinhar a palavra: ").lower()

        # Palpite de palavra inteira
        if len(palpite) > 1:
            if palpite == palavra:
                print("\n🎉 Parabéns! Você acertou a palavra inteira!")
                print("A palavra era:", palavra)
                break
            else:
                tentativas -= 1
                print("❌ Palavra incorreta! Você perdeu uma tentativa.")
                continue

        # Verificação de letra válida
        if not palpite.isalpha() or len(palpite) != 1:
            print("Por favor, digite apenas uma letra válida ou uma palavra.")
            continue

        if palpite in letras_corretas or palpite in letras_erradas:
            print("Você já tentou esta letra. Tente novamente.")
            continue

        # Letra correta
        if palpite in palavra:
            letras_corretas.append(palpite)
            if len(set(letras_corretas)) == len(set(palavra.replace(" ", ""))):  # Palavras compostas
                print("\n🎉 Parabéns! Você venceu!")
                print("A palavra era:", palavra)
                break
        else:
            letras_erradas.append(palpite)
            tentativas -= 1

    else:
        print("\n💀 Você perdeu! A palavra era:", palavra)

# Iniciar o jogo
jogar_jogo_da_forca()
