'''
-----------------------------
 EJERCICIO N°2
 Creación de una pila
-----------------------------
'''
class Pila:
  def __init__(self):
    self.__listaPila = []

  def push(self, val):
    self.__listaPila.append(val)

  def pop(self):
    val = self.__listaPila[-1]
    del self.__listaPila[-1]
    return val

# Código de prueba 1
objetoPila = Pila()

objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())

'''
# Código de prueba 2
objetoPila1 = Pila()
objetoPila2 = Pila()

objetoPila1.push(3)
objetoPila2.push(objetoPila1.pop())

print(objetoPila2.pop())

# Código de prueba 3
pequeñaPila = Pila()
otraPila = Pila()
graciosaPila = Pila()

pequeñaPila.push(1)
otraPila.push(pequeñaPila.pop() + 1)
graciosaPila.push(otraPila.pop() - 2)

print(graciosaPila.pop())
'''
