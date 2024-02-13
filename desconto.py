valor_produto = float(input("Digite o valor do produto: R$"))

print(f'Valor do produto (sem desconto): R${valor_produto:.2f}')
print(f'Valor do produto (com desconto): R${valor_produto*0.95:.2f}')