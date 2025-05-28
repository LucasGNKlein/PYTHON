sent_message = "Hello there!\n General Kenobi!"

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
  original_message = file.read()

  file.seek(0)

  unsent_message = "Uoooooon! Uoooooon!"

  file.truncate(len(unsent_message))

  file.write(unsent_message)

print("Original Message:", original_message)
print("Unsent Message:", unsent_message)
