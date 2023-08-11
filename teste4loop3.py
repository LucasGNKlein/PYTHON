# Um jovem mágico escolheu um número secreto.
# Ele o ocultou em uma variável chamada secret_number.
# Ele quer que todos que executam seu programa joguem o jogo
# Adivinhe o número secreto e adivinhem qual número ele escolheu para eles.
# Quem não adivinhar o número ficará para sempre em um loop infinito! 
# Infelizmente, ele não sabe como completar o código.
# Crie um código para ajudar o Mago.

counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)