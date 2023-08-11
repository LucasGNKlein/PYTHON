def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Solicita ao usuário quantos termos da sequência de Fibonacci deseja gerar
num_terms = int(input("Digite o número de termos da sequência Fibonacci: "))

# Gera a sequência de Fibonacci
sequence = fibonacci(num_terms)

# Exibe a sequência gerada
print("Sequência de Fibonacci:")
for num in sequence:
    print(num, end=" ")