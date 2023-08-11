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

print(len(lista)) #tamanho geral
print(lista[1:len(lista)-1]) #esse comando define a contagem do tamanho da lista a partir do índice 1 até o penúltmio índice, ou seja, mostra todos os elementos menos o primeiro e o último.

É possível colocar listas dentro de listas, parecido com matrizes.

m=[[1,3,5], [2,4,6,8]] #lista dentro da lista
print(m) #toda a lista
print(m[0]) #primeiro elemento de m
print(m[0][1]) #elemento de indice 1 dentro do primeiro elemento de m

Em Python, os blocos do programa são definidos pela identação. Ou seja, os comandos que estiverem recuados estão dentro de um bloco. Cada nível a amais de recuo significa um nível a mais de alinhamento da estrutura do código. Nunca misture tabs e espaços, abaixo segue exemplo de um comando if:

x=1
if x>2:
  print("primeiro comando")
  print("segundo comando")
print("terceiro comando")

A mesma lógica vale para estruturas aninhadas. Como um if dentro de um if

x=3
if x>2:
  print("comando1")
  print("comando2")
  if x>5:
    print("comando3")
    print("comando4")
  print("comando5")
print("comando6")

O comando if é semelhante à maioria das linguagens de programação. E tem os operadores:

a=1
b=5
c=3
d=2
#verificando igualdade

if b==5:
  print("b é igual a 5")

#verificando diferença

if a!=3:
  print("a é diferente de 3")

#maior >, menor <, maior igual >=, menor <=

if b <=10:
  print("b é menor ou igual a 10")

#negação ! (not)

if not(c==2):
  print("se não(c igual a 2)")

#operações lógicas e=and ou=or

if ((a!=b) and (c!=d) or ((c+d)==5)):
  print("(a é diferente de b e c é diferente de d) \
   ou c+d é igual a 5") # o caractere \ permite que a string seja continuada na outra linha

O laço de repetição for itera sobre uma sequência. O comando range cria uma sequência.o range tem a forma range(inicio, final+1, passo). Por exemplo:

#itera i na sequência de 0 até 9
for i in range(5):
  print(i)

print("-----")
for i in range(2,5):
  print(i)

print("-----")

for i in range(10,2,-2):
  print(i)

O for() pode iterar uma variável diretamente em uma lista. Por exemplo:

lista=["mercúrio","vênus","terra","marte"]
#acessando os elementos via índice

for i in range(4):
  print(lista[i])

#posso verrificar o tamanho da lista para fazer isso
print("-----")
for i in range(len(lista)):
  print(lista[i])
#também é possível iterar diretamente na lista
print("-----")
for planeta in lista:
  print(planeta)

Ao acessar com índice, é possível alterar a lista, mas não é possível alterar ao iterar diretamente na lista. Por exemplo:

#assim funciona
lista=["mercúrio","vênus","terra","marte"]
print("funcionou")
for i in range(len(lista)):
  lista[i]=lista[i]+"!"
print(lista)

#assim não funciona
print("não funcionou")
for planeta in lista:
  planeta=planeta+"*" #não funciona pq ele cria uma cópia do elemento
  print(planeta)
print(lista)

Concatenar listas é muito fácil!:

lista1=["pão","presunto"]
lista2=["queijo","pão"]
lista3=lista1+lista2
lista3.pop(3) #esse retira um elemento da lista usando seu índice
              #lista3.remove("pão") apaga o primeiro valor
              #lista3=list(set(lista3)) cria um conjunto sem itens repetidos e cria uma lista deste conjunto
print(lista3)

O laço de repetição while(enquanto) funciona como nas outras linguagens

lista=["a","b","c","d"]
i=0
while(lista[i]!="c"):
  print(lista[i]) #cada vez incrementa o índice i até ele chegar no c então para
  i=i+1

As funções me Python são definidas com "def", pode receber parâmetros oe retornar ou não valores.

def calcula_media(v1,v2,v3):
  soma=v1+v2+v3
  media=soma/3
  return media

print("calcula a média:")
media=calcula_media(7,10,4)
print(media)

Retornando mais de um valor da função

def media_e_maior(v1,v2,v3):
  media=(v1+v2+v3)/3.0
  maior=max([v1,v2,v3])
  return media,maior

media,maior=media_e_maior(10,50,20)
print(media)
print(maior)

