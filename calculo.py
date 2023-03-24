#%%#
import math


def alg(p1, p2):
      x1, y1 = p1 
      x2, y2 = p2
      print(p1, p2)
      print(x1, y1)
      print(x2, y2)
      calculo_x = x2 - x1
      calculo_x = calculo_x ** 2
      calculo_y = y2 - y1
      calculo_y = calculo_y ** 2
      d = calculo_x + calculo_y
      return math.sqrt(d)
#%%#

def classificacao(valor):
    if valor <= 7 and valor >= 5:
      resultado = 'infantil A'
    elif valor <= 10 and valor >= 8:
      resultado = 'infantil B'
    elif valor <= 13 and valor >= 11:
      resultado = 'juvenil A'
    elif valor <= 17 and valor >= 12:
      resultado = 'juvenil B'
    elif valor > 17:
      resultado = 'Maior de 18'
    else:
      resultado = 'Digite uma idade acima de 4 anos'
    
    return resultado