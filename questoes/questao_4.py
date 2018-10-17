## QUESTÃO 4 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))
dia = int(input("Digite o dia: "))

print('A data digita foi {}-{}-{}'.format(ano, mes, dia))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    ano_bi = 1
else:
    ano_bi = 0

if ano_bi == 1:
    if(mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
        if dia == 31:
            dia = 1
            if mes == 12:
                mes = 1
                ano += 1
            else:
                mes += 1
        else:
            dia += 1
            print('A data seguinte será: {}-{}-{}'.format(ano, mes, dia))
    else:
        if (dia == 29) and (mes == 2):
            dia = 1
            mes += 1
            print('A data seguinte será: {}-{}-{}'.format(ano, mes, dia))
        else:
            if (dia == 30):
                dia = 1
                mes += 1
            else:
                dia += 1
                print('A data seguinte será: {}-{}-{}'.format(ano, mes, dia))
else:
    if(dia == 31):
        dia = 1
        if(mes == 12):
            mes = 1
            ano += 1
        else:
            mes += 1
    else:
        if(dia == 28) and (mes == 12):
            dia = 1
            mes += 1
        else:
            if(dia == 30):
                dia = 1
                mes += 1
            else:
                dia += 1
                print('A data seguinte será: {}-{}-{}'.format(ano, mes, dia))







    
if __name__ == '__main__':
    main()
