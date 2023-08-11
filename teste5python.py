Variáveis em Python não precisam ser declaradas, basta começar a utiliza-las. Elas também não tem um tipo rígido. Existem alguns tipos básicos de dados em Python, como nas variáveis abaixo:

x=5 #variável int
y=2.3 #variável float, double
z=True #variável boolean False, True
txt="olá Python!" #texto,string

Para mostrar algum valor usamos o comando **print**

print(x) #mostra a variável x
print(y) #mostra a variável y
print("A variável y é: "+ str(y)) #str transforma o dado y(float) em uma string(texto)
print(z) #mostra a variável z
print(txt) #mostra a variável txt

Python possui vários tipos de coleções, o tipo mais comum é o ArrayList. Ele permite guardar qualquer tipo de objeto, pode aumentar ou diminuir dinamicamente e é acessado com um índice inteiro.

lista=[5,8,9,1,0,12]
print(lista)
print(lista[0])
print(lista[2])

Podemos criar uma lista vazia com [] e ir adicionando elementos com o append()

lista=[]
lista.append(3)
lista.append(7)
lista.append(8)
lista.append(12)
lista.append(17)
print(lista)

Também é possível acessar os elementos usando os índices negativos.

print(lista[-1])
print(lista[-2])

Usando o : é possível acessar subconjuntos do ArrayList.

#Acessar os elementos 0, 1, 2
#Lista[primeiro elemento:elemento depois do último]
print(lista[0:3])
#acessar todos os elementos
print(lista[:])
#acessar os elementos do primeiro ao terceiro elemento
print(lista[:3])
#acessar do terceiro até o último
print(lista[2:])
#acessar elementos em pares do 0 ao 4
print(lista[0:5:2])

Para saber o tamanho de uma lista usamos o comando len()

print(len(lista))
print(lista[1:len(lista)-1])