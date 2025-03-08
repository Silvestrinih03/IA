from grafo import Grafo
from visualizargrafo import VisualizarGrafo

def obter_dados_usuario():
    """Obtém os dados necessários para criar o grafo."""
    while True:
        num_vertices = int(input("Número de vértices (15, 500, 5000, 10000): "))
        while num_vertices not in {15, 500, 5000, 10000}:
            print("Entrada inválida! Escolha entre 15, 500, 5000, 10000.")
            num_vertices = int(input("Número de vértices: "))

        num_arestas = int(input("Número de arestas por nó (3, 5, 7): "))
        while num_arestas not in {3, 5, 7}:
            print("Entrada inválida! Escolha entre 3, 5, 7.")
            num_arestas = int(input("Número de arestas por nó: "))

        return num_vertices, num_arestas

def executar():
    """Executa o fluxo principal do programa."""
    while True:
        # Obter dados do usuário
        num_vertices, num_arestas = obter_dados_usuario()

        # Criar o grafo e gerar as arestas
        grafo = Grafo(num_vertices)
        grafo.gerar_arestas_aleatorias(num_arestas)

        # Imprimir conexões
        print("\nGrafo gerado!")
        grafo.imprimir_conexoes()

        # Visualizar o grafo
        visualizador = VisualizarGrafo(grafo)
        print("\nDesenhando o grafo...")
        visualizador.desenhar_grafo()

        # Perguntar se o usuário quer gerar outro grafo
        repetir = input("\nDeseja gerar outro grafo? (s/n): ").strip().lower()
        if repetir == 'n':
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    executar()