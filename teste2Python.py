number1 = int(input('Numero 1: '))
number2 = int(input('Numero 2: '))
number3 = int(input('Numero 3: '))

largest_number = number3

if number1 > number3:
    largest_number = number1

if number2 > number3:
    largest_number = number2

print("O maior numéro é", largest_number)