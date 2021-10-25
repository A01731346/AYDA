/* 
   Ethienne J. Cruz Gutiérrez | A01731346
   Análisis y diseño de algoritmos
   Grafo de adyacencia DFS
   
   Instrucciones: Implementar DFS sobre un grafo que utilice matrices de adyacencia en lugar de listas ligadas
*/

public class Graph{

    private boolean adjacencyMatrix[][];
    private int vertex;
    private int edges;

    private Graph(){}

    public Graph(int vertex, int edges){

        this.vertex = vertex;
        this.edges = edges;

        // Fill the matrix;
        // Bidirectional Graph so its symmetric

        adjacencyMatrix = new boolean[vertex][vertex];

    }

    public void addEdge(int start, int finish){

        // Bidirectional:
        adjacencyMatrix[start][finish] = true;
        adjacencyMatrix[finish][start] = true;

    }

    public void DFS(int start, boolean[] visitedList){

        // Print the current node:
        System.out.print(start + " ");

        // Set the current node as visited:
        visitedList[start] = true;

        // Traverse the whole adjacency matrix:
        for(int i = 0; i < this.vertex; i++){

            // Check if i is adjacent to the current node and if its not visited:
            if(this.adjacencyMatrix[start][i] == true && visitedList[i] == false){
                
                // Recurse to node i:
                this.DFS(i, visitedList);

            }

        }

    }

    // Time complexity O(vertex * edges) which is the size of the adjacency matrix.

    // Runner function:
    public static void main(String[] args) {

        int vertex = 8;
        int edges = 9;
        boolean visitedList[] = new boolean[vertex];

        Graph myGraph = new Graph(vertex, edges);

        myGraph.addEdge(0, 1);
        myGraph.addEdge(0, 3);
        myGraph.addEdge(1, 4);
        myGraph.addEdge(3, 4);
        myGraph.addEdge(2, 3);
        myGraph.addEdge(2, 5);
        myGraph.addEdge(4, 5);
        myGraph.addEdge(5, 6);
        myGraph.addEdge(6, 7);

        myGraph.DFS(0, visitedList);
        System.out.println();

        visitedList = new boolean[vertex];
        myGraph.DFS(4, visitedList);

    }

}
