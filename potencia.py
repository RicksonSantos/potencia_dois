
#importar a funções matemáticas complexas pelo padrão C#

import math
num=int(input('Olá, digite um número: '))
p1=math.log10(num)
p2=math.log10(2)

r=p1/p2

#usar o if para saber se o resultado da operação de r será numero inteiro#
#para isso transformo o r em inteiro e depois questiono se é igual o r da operação p1/p2#

if(int(r)==r):
    print('true')
else:
    print('false')

