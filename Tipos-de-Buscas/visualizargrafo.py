import networkx as nx
import matplotlib.pyplot as plt

class VisualizarGrafo: 
    def __init__(self, grafo):
        self.grafo = grafo

    # Função que cria o desenho gráfico utilizando a biblioteca NetworkX e Matplotlib
    def desenhar_grafo(self):
        grafo = self.grafo
        if grafo.qtdVertices > 500:
            print("Grafo muito grande para visualização!")
            return
        
        G = nx.Graph()
        for vertice, vizinhos in grafo.conexoes.items():
            for vizinho in vizinhos:
                G.add_edge(vertice, vizinho)

        if grafo.qtdVertices > 100:
            layout = nx.kamada_kawai_layout(G, weight=None)
        else:
            layout = nx.spring_layout(G, seed=42, k=0.2)  # Aumentando o parâmetro k para mais espaçamento

        plt.figure(figsize=(12, 8))
        nx.draw(G, layout, with_labels=True, node_color="lightblue", edge_color="gray",
                node_size=300 if grafo.qtdVertices > 100 else 500, font_size=6 if grafo.qtdVertices > 100 else 8)
        plt.title("Grafo Gerado")
        plt.show()