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