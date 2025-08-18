# simular de maquide cassino

import random
import time

simbolos = ["🍇", "🍈", "🍉", "🍋", "🍊", "🍌", "🍍", "🥭", "🍎", "🍏", "🍐", "🍑", "🍒"]

for _ in range(15):
	giro = random.choices(simbolos, k=3)
	print("\r*🎰* " + " ".join(giro), end="", flush=True)
	time.sleep(0.15)

resultado = random.choices(simbolos, k=3)

print("\r*🎰*" + " ".join(resultado))

if resultado[0] == resultado [1] == resultado[2]:
	print("Parabéns! Você ganhou! 🎉")
else:
	print("Tente novamente! 🍀")