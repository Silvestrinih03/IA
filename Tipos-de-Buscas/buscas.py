from collections import deque

class Buscas:
    def __init__(self, grafo):
        self.grafo = grafo

    # Busca em Largura
    def busca_em_largura(self, inicio, objetivo):
        visitados = {v: False for v in self.grafo.conexoes}
        distancia = {v: float('inf') for v in self.grafo.conexoes}
        anterior = {v: None for v in self.grafo.conexoes}
        fila = deque([inicio])
        visitados[inicio] = True
        distancia[inicio] = 0

        while fila:
            atual = fila.popleft()
            if atual == objetivo:
                break
            for vizinho in self.grafo.conexoes[atual]:
                if not visitados[vizinho]:
                    visitados[vizinho] = True
                    distancia[vizinho] = distancia[atual] + 1
                    anterior[vizinho] = atual
                    fila.append(vizinho)

        # Reconstruir o caminho
        caminho = []
        atual = objetivo
        while atual is not None:
            caminho.append(atual)
            atual = anterior[atual]
        caminho.reverse()
        return caminho, distancia[objetivo]