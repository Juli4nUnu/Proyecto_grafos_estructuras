class Nodo:
  def __init__(self, name):
    self.name = name
    
  def get_name(self):
    return self.name

  def agregar_conexion(self, conexion):
    self.conexiones.append(conexion)

  def __str__(self):
    return self.name


class Conexion:
  def __init_(self, n1, n2):
    self.n1 = n1
    self.n2 = n2

  def get_n1(self):
    return self.n1

  def get_n2(self):
    return self.n2

  def __str__(self):
    return self.n1.get_name() + "----->" + self.n2.get_name()


class Grafo:
  def __init__(self):
    self.grafo_Lista = {}

  def añadir_nodo(self, nodo):
    if nodo in self.grafo_Lista:
      return throw("Nodo ya existe")
    self.grafo_Lista[nodo] = []

  def añadir_conexion(self, partida, destino):
    if partida in self.grafo_Lista and destino in self.grafo_Lista:
      self.grafo_Lista[partida].append(destino)    

  def get_nodo(self, name):
    for nodo in self.grafo_Lista:
      if nodo.get_name() == name:
        return nodo
    return None
  
  def get_vecinos(self, nodo):
    return self.grafo_Lista[nodo]

  def __str__(self):
    a = ""
    for nodo in self.grafo_Lista:
      a += str(nodo) + " : "
      for conexion in self.grafo_Lista[nodo]:
        a += str(conexion) + ", "
      a += "\n"
    return a


G = Grafo()

G.añadir_nodo(Nodo("A"))
G.añadir_nodo(Nodo("B"))
G.añadir_nodo(Nodo("C"))

G.añadir_conexion(G.get_nodo("A"), G.get_nodo("B"))
G.añadir_conexion(G.get_nodo("B"), G.get_nodo("A"))
G.añadir_conexion(G.get_nodo("A"), G.get_nodo("C"))

print(G)