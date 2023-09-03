nome="Lidia Wolf"
encontrado=False

with open("nomes.txt", "rt") as arquivo:
  for linha in arquivo:
    if nome.strip() == linha.strip():
      encontrado = True
      break


if encontrado:
  print("Está na lista")
else:
  print("Não está na lista")