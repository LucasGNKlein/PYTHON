O Numpy é uma biblioteca que incorpora ao Python várias funções para cálculo numérico e álgebra, fundamentais para ciências de dadoas. O mais comum é importar essa biblioteca com o apelido de "np"

import numpy as np

A estrutura de dados mais importande do numpy é o Array. O aray é uma matriz multidimensional com operadores de álgebra.

#criar um array apartir de uma lista

v=np.array([2,4,7])

print('vetor criado apartir de lista', v)
print('segundo elemento do vetor', v[1])

#criar array apartir de uma lista multidimensional

m=np.array([[2,5,3], [9,1,7]])
print('\nmatriz criada apartir de lista multidimensional:\n',m)
print('primeiro elemento da segunda linha:',m[1,0])

#também é possível usar slices num array

print('segunda coluna da matriz', m[:,1])

Existem outras formas de criar arrays, pode ser um array apenas com zeros, apenas com um, ou identidade

#matriz de zeros
A=np.zeros((3,3))
print("zeros\n",A)


#matriz de 1
B=np.ones((3,3))
print("ones\n",B)

#matriz identidade
C=np.eye((3))
print("identity\n",C)

O formato do array (número de linhas e colunas) é dado pelo shape

A=np.array([[1,2],[3,4],[5,6]])
print(A)
print('formato:', A.shape)
print('número de linhas:', A.shape[0])
print('número de colunas:', A.shape[1])

Diversas operações matemáticas podem ser realizadas com arrays, incluindo operações açlgébricas entre matrizes

A=np.array([[1,2],[1,2]])
print('A\n',A)

B=np.array([[3,1],[2,1]])
print('B\n',B)

C=A*B
#MULTIPLICAÇÃO PONTO A PONTO
print("\nMultiplicação ponto a ponto\n C=A*B\n", C)
D=np.matmul(A,B)
#MULTIPLICAÇÃO DE MATRIZES
print('\nMultiplicação de matrizes\n D=np.matmul(A,B)\n', D)
#divisão ponto a ponto
E=A/B
print('\nDivisão ponto a ponto\n E=A/B\n', E)
#SOMA
F=A+B
print('\nSoma\n F=A+B\n', F)
#SUBTRAÇÃO
G=A-B
print('\nSubtração\n G=A-B\n', G)
#INVERSA - A não é possível obter a inversa
H=np.linalg.inv(B)
print('\nMatriz inversa\n H=np.linalg.inv(A)\n', H)
#NEGATIVA
I=np.invert(A)
print('\nMatriz negativa\n', I)

