import random
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    # Função que inicializa número fixo de vértices e cria lista de arestas vazias
    def __init__(self, num_vertices):
        self.qtdVertices = num_vertices
        self.conexoes = {i: set() for i in range(num_vertices)}

    # Função que adiciona aresta entre dois vértices
    def adicionar_aresta(self, origem, destino):
        if origem != destino and destino not in self.conexoes[origem]:
            self.conexoes[origem].add(destino)
            self.conexoes[destino].add(origem)

    # Função que gera o grafo garantindo que cada nó tenha exatamente o número correto de arestas
    def gerar_arestas_aleatorias(self, num_arestas):
        todos_os_nos = list(self.conexoes.keys())
        
        for i in range(self.qtdVertices - 1):
            self.adicionar_aresta(i, i + 1)

        nos_disponiveis = [n for n in todos_os_nos if len(self.conexoes[n]) < num_arestas]

        while len(nos_disponiveis) > 1:
            origem, destino = random.sample(nos_disponiveis, 2)

            self.adicionar_aresta(origem, destino)

            if len(self.conexoes[origem]) >= num_arestas:
                nos_disponiveis.remove(origem)
            if len(self.conexoes[destino]) >= num_arestas:
                nos_disponiveis.remove(destino)

    # Imprime todas as conexões (arestas) que foram criadas
    def imprimir_conexoes(self):
        for vertice, vizinhos in sorted(self.conexoes.items()):
            print(f"{vertice}: {sorted(vizinhos)}")

# Função que cria o desenho gráfico utilizando a biblioteca NetworkX e Matplotlib
def desenhar_grafo(grafo):
    G = nx.Graph()

    for vertice, vizinhos in grafo.conexoes.items():
        for vizinho in vizinhos:
            G.add_edge(vertice, vizinho)

    pos = nx.spring_layout(G, seed=42)  # Define a posição dos nós para visualização

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=8)
    plt.title("Grafo Gerado")
    plt.show()

# Função principal
def main():
    while True:
        num_vertices = int(input("Número de vértices (15, 500, 5000, 10000): "))
        while num_vertices not in {15, 500, 5000, 10000}:
            print("Entrada inválida! Escolha entre 15, 500, 5000, 10000.")
            num_vertices = int(input("Número de vértices: "))

        num_arestas = int(input("Número de arestas por nó (3, 5, 7): "))
        while num_arestas not in {3, 5, 7}:
            print("Entrada inválida! Escolha entre 3, 5, 7.")
            num_arestas = int(input("Número de arestas por nó: "))

        grafo = Grafo(num_vertices)
        grafo.gerar_arestas_aleatorias(num_arestas)

        print("\nGrafo gerado!")
        grafo.imprimir_conexoes()

        print("\nDesenhando o grafo...")
        desenhar_grafo(grafo)
        
        repetir = input("\nDeseja gerar outro grafo? (s/n): ").strip().lower()
        if repetir != 's':
            print("Encerrando o programa...")
            break

# Executa o programa se rodado diretamente
if __name__ == "__main__":
    main()
