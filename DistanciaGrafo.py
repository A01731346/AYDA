#  A C T: D I S T A N C I A   D E   G R A F O  
#  ETHIENNE J. CRUZ GUTIÉRREZ 


from collections import defaultdict
from queue import Queue

#Esta clase representa un gráfico dirigido, usando la representación de la lista de adyacencia
class Graph:

    def __init__(self):
        #Diccionario predeterminado para almacenar gráfico
        self.graph = defaultdict(list)
        self.vertexNames = {}

    #Función para agregar una arista al gráfico
    def EdgeBFS(self, u, v):
        self.graph[u].append(v)

    #Función para agregar un vértice al gráfico
    def addVertexName(self, vertex, name):
        self.vertexNames[vertex] = name

    #Función para imprimir un BFS de gráfico
    def BFS(self, s):
        queue = Queue() #Queue para hacer BFS 

        #Crear un diccionario con gran distancia infinito de cada vértice de origen
        distances = {distance: 9999999 for distance in self.graph.keys()}
        visitedVertices = set()
        queue.put(s)
        while not queue.empty():
            vertex = queue.get()
            if vertex == s:
                distances[vertex] = 0
                visitedVertices.update({s})
            for u in self.graph[vertex]:
                if u not in visitedVertices:
                    if distances[u] > distances[vertex] + 1:
                        distances[u] = distances[vertex] + 1
                    queue.put(u)
                    visitedVertices.update({u})
        return self.display(s, distances)

    def display(self, s, distances):
        print('Distancia establecida desde ' + self.vertexNames[s] + ' hasta:')
        for vertex, distance in distances.items():
            print('  - ' + self.vertexNames[vertex] + ': ' + str(distance))


#Creación del grafo
g = Graph()
g.addVertexName(0, 'El Rosario')
g.addVertexName(1, 'Instituto del Petróleo')
g.addVertexName(2, 'Deportivo 18 de Marzo')
g.addVertexName(3, 'Martín Carrera')
g.addVertexName(4, 'La Raza')
g.addVertexName(5, 'Consulado')
g.addVertexName(6, 'Tacuba')
g.addVertexName(7, 'Guerrero')
g.addVertexName(8, 'Garibaldi')
g.addVertexName(9, 'Oceanía')
g.addVertexName(10, 'Hidalgo')
g.addVertexName(11, 'Bellas Artes')
g.addVertexName(12, 'Morelos')
g.addVertexName(13, 'San Lázaro')
g.addVertexName(14, 'Balderas')
g.addVertexName(15, 'Salto de Agua')
g.addVertexName(16, 'Pino Suárez')
g.addVertexName(17, 'Candelaria')
g.addVertexName(18, 'Tacubaya')
g.addVertexName(19, 'Centro Médico')
g.addVertexName(20, 'Chabacano')
g.addVertexName(21, 'Jamaica')
g.addVertexName(22, 'Pantitlán')
g.addVertexName(23, 'Santa Anita')
g.addVertexName(24, 'Mixcoac')
g.addVertexName(25, 'Zapata')
g.addVertexName(26, 'Ermita')
g.addVertexName(27, 'Atlalilco')

g.EdgeBFS(0, 1)
g.EdgeBFS(0, 6)

g.EdgeBFS(1, 0)
g.EdgeBFS(1, 2)
g.EdgeBFS(1, 4)

g.EdgeBFS(2, 1)
g.EdgeBFS(2, 4)
g.EdgeBFS(2, 3)

g.EdgeBFS(3, 2)
g.EdgeBFS(3, 5)

g.EdgeBFS(4, 1)
g.EdgeBFS(4, 2)
g.EdgeBFS(4, 5)
g.EdgeBFS(4, 7)

g.EdgeBFS(5, 3)
g.EdgeBFS(5, 4)
g.EdgeBFS(5, 9)
g.EdgeBFS(5, 12)

g.EdgeBFS(6, 0)
g.EdgeBFS(6, 10)
g.EdgeBFS(6, 18)

g.EdgeBFS(7, 4)
g.EdgeBFS(7, 8)
g.EdgeBFS(7, 10)

g.EdgeBFS(8, 7)
g.EdgeBFS(8, 11)
g.EdgeBFS(8, 12)

g.EdgeBFS(9, 5)
g.EdgeBFS(9, 13)
g.EdgeBFS(9, 22)

g.EdgeBFS(10, 6)
g.EdgeBFS(10, 7)
g.EdgeBFS(10, 11)
g.EdgeBFS(10, 14)

g.EdgeBFS(11, 8)
g.EdgeBFS(11, 10)
g.EdgeBFS(11, 15)
g.EdgeBFS(11, 16)

g.EdgeBFS(12, 5)
g.EdgeBFS(12, 8)
g.EdgeBFS(12, 13)
g.EdgeBFS(12, 17)

g.EdgeBFS(13, 12)
g.EdgeBFS(13, 9)
g.EdgeBFS(13, 17)
g.EdgeBFS(13, 22)

g.EdgeBFS(14, 10)
g.EdgeBFS(14, 19)
g.EdgeBFS(14, 18)
g.EdgeBFS(14, 15)

g.EdgeBFS(15, 11)
g.EdgeBFS(15, 14)
g.EdgeBFS(15, 16)
g.EdgeBFS(15, 20)

g.EdgeBFS(16, 11)
g.EdgeBFS(16, 15)
g.EdgeBFS(16, 17)
g.EdgeBFS(16, 20)

g.EdgeBFS(17, 12)
g.EdgeBFS(17, 13)
g.EdgeBFS(17, 16)
g.EdgeBFS(17, 21)

g.EdgeBFS(18, 6)
g.EdgeBFS(18, 14)
g.EdgeBFS(18, 19)
g.EdgeBFS(18, 24)

g.EdgeBFS(19, 14)
g.EdgeBFS(19, 18)
g.EdgeBFS(19, 20)
g.EdgeBFS(19, 25)

g.EdgeBFS(20, 16)
g.EdgeBFS(20, 19)
g.EdgeBFS(20, 21)
g.EdgeBFS(20, 15)
g.EdgeBFS(20, 23)
g.EdgeBFS(20, 26)

g.EdgeBFS(21, 17)
g.EdgeBFS(21, 20)
g.EdgeBFS(21, 22)
g.EdgeBFS(21, 23)

g.EdgeBFS(22, 9)
g.EdgeBFS(22, 13)
g.EdgeBFS(22, 21)

g.EdgeBFS(23, 20)
g.EdgeBFS(23, 21)
g.EdgeBFS(23, 27)

g.EdgeBFS(24, 18)
g.EdgeBFS(24, 25)

g.EdgeBFS(25, 19)
g.EdgeBFS(25, 24)
g.EdgeBFS(25, 26)

g.EdgeBFS(26, 20)
g.EdgeBFS(26, 25)
g.EdgeBFS(26, 27)

g.EdgeBFS(27, 23)
g.EdgeBFS(27, 26)


print("====================================================")
print("         D I S T A N C I A   D E   G R A F O")
print("====================================================")
g.BFS(0)

# Materiales utilizados: 
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# https://www.askpython.com/python/examples/distance-between-nodes-unweighted-graph
