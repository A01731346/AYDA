
  # Ethienne J. Cruz Gutiérrez | A01731346
  # Análisis y diseño de algoritmos
  # Grafo de adyacencia DFS
   
  # Instrucciones: Implementar DFS sobre un grafo que utilice matrices de adyacencia en lugar de listas ligadas



from pyvis import network as net
from IPython.core.display import display, HTML


class Grafo:

    matriz = []
    aristas = []

    def __init__(self, v, e):
        self.v = v
        self.e = e
        Grafo.matriz = [[0 for i in range(v)]
                        for j in range(v)]

    def agregarArista(self, inicio, e):
        Grafo.matriz[inicio][e] = 1
        Grafo.matriz[e][inicio] = 1
        Grafo.aristas.append([inicio, e])

    def DFS(self, inicio, visitado):
        print(inicio, end=' ')
        visitado[inicio] = True
        for i in range(self.v):
            if(Grafo.matriz[inicio][i] == 1 and (not visitado[i])):
                self.DFS(i, visitado)

    def grafico(self):
        g = net.Network(height='400px', width='50%', heading='Grafo')
        i = 0
        while i < self.v:
            g.add_node(i)
            i = i + 1
        for par in self.aristas:
            g.add_edge(par[0], par[1])
        g.show('grafo.html')
        display(HTML('grafo.html'))


# Definir número de vértices y aristas del grafo. 
v, e = 8, 9

# Inicializar el grafo.
G = Grafo(v, e)

# Definir aristas existentes.
G.agregarArista(0, 1)
G.agregarArista(0, 3)
G.agregarArista(1, 4)
G.agregarArista(3, 4)
G.agregarArista(2, 3)
G.agregarArista(2, 5)
G.agregarArista(4, 5)
G.agregarArista(5, 6)
G.agregarArista(6, 7)

# DEPTH FIRST SEARCH
visitado = [False] * v
G.DFS(0, visitado)
