## QUESTÃO 2 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
from math import sqrt

def main():
    
x=0
y=0
local = input('Digite o deslocamento desejado: ').upper()

while local:


   direc = local[ : local.find(' ')]
   passos = local[local.find(' ') + 1 : ]
  #Se a direção indicada for 'baixo', o número digitado irá subtrair o y visto que no plano cartesiano quanto menor o y mais para baixo se localiza o ponto
   if direc == 'BAIXO':
       y = y - int(passos)
  # Se a direção indicada for 'cima', o número digitado irá somar ao y visto que no plano cartesiano quanto maior o y mais para cima se localiza o ponto
   elif direc == 'CIMA':
       y = int(passos)+y
  # Se a direção indicada for 'direita', o número digitado irá somar ao x visto que no plano cartesiano quanto maior o x mais para direita se localiza o ponto
   elif direc == 'DIREITA':
       x = int(passos)+x
  # Se a direção indicada for 'esquerda', o número digitado irá subtrair o x visto que no plano cartesiano quanto menor o x mais para esquerda se localiza o ponto
   elif direc =='ESQUERDA':
       x = x - int(passos)
   local = input('Digite novo deslocamento desejado: ')

  #O programa sairá do loop caso nada seja digitado
deslocamento = sqrt(x**2 + y**2)
print(int(deslocamento))




    
if __name__ == '__main__':
    main()
