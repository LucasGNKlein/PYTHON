# Define the Higher-order function 
def apply_operation(operation, numbers):
  result = []
  for num in numbers:
    result.append(operation(num))
  return result

# Example operation
def double(x):
  return x * 2

# List of numbers
numbers_list = [1, 2, 3, 4, 5]

# Using the higher-order function
doubled_numbers = apply_operation(double, numbers_list)

# Displaying the outcomes
print('Original Numbers:', numbers_list)
print('Doubled Numbers:', doubled_numbers)
