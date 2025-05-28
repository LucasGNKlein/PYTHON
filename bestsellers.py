import csv

csv_file_path = 'Bestseller - Sheet1.csv'

best_selling_book = None
max_sales = 0

#ler csv
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
  csv_reader = csv.reader(csv_file)
  
  #pula o cabeçalho
  csv_file.readline()
  
  for row in csv_reader:
    #extrai a coluna sales para usar
    current_sales = float(row[4])
    
    if current_sales > max_sales:
      max_sales = current_sales
      best_selling_book = row

#cria um novo arquivo
output_file_path = 'bestseller_info.csv'
with open(output_file_path, 'w', newline='') as output_file:
  csv_writer = csv.writer(output_file)
  
  #escreve cabeçalho
  csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
  
  #escreve as informações dos livros mais vendidos
  csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])

#mensagem de confirmação
print('Bestselling info written to', output_file_path)
