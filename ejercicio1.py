'''
-----------------------------
 EJERCICIO N°1
 Una pila desde dos enfoques
-----------------------------
'''
# ENFOQUE PROCEDIMENTAL
pila = []

def push(val):
  pila.append(val)

def pop():
  val = pila[-1]
  del pila[-1]
  return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

# ENFOQUE ORIENTADO A OBJETOS
class Pila:     # define la clase Pila
  def __init__(self):    # define la función del constructor
    print("¡Hola!")
    #self.listaPila = []

objetoPila = Pila()    # instanciando el objeto
#print(len(objetoPila.listaPila))


class Pila:
  def __init__(self):
    self.__listaPila = []

objetoPila = Pila()
print(len(objetoPila.__listaPila))
