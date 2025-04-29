"""
Arquivo de testes para praticar implementações do algoritmo de Dijkstra.
Este arquivo contém vários problemas para você implementar e testar suas soluções.

INSTRUÇÃO:
1. Implemente a função 'dijkstra' para cada problema
2. Execute os testes para verificar sua solução
3. Não olhe as dicas antes de tentar resolver os problemas por conta própria!

Cada problema tem uma descrição e testes específicos.
"""

import unittest


# PROBLEMA 1: Caminho Mais Curto em um Grafo Simples
"""
Descrição: 
Implemente o algoritmo de Dijkstra para encontrar o caminho mais curto de um nó origem 
para todos os outros nós em um grafo simples representado como um dicionário de adjacências.

O grafo é representado como:
grafo = {
    'A': {'B': 2, 'C': 5},  # Do nó 'A' para 'B' o peso é 2, para 'C' o peso é 5
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'A': 5, 'F': 2},
    'D': {'B': 3},
    'E': {'B': 1, 'F': 4},
    'F': {'C': 2, 'E': 4}
}

A função deve retornar um dicionário onde as chaves são os nós de destino e os valores 
são tuplas contendo (distância, caminho), onde caminho é uma lista de nós do percurso.
"""

def dijkstra_problema1(grafo, origem):
    # Implemente o algoritmo de Dijkstra aqui
    pass


class TestProblema1(unittest.TestCase):
    def test_caminho_mais_curto(self):
        grafo = {
            'A': {'B': 2, 'C': 5},
            'B': {'A': 2, 'D': 3, 'E': 1},
            'C': {'A': 5, 'F': 2},
            'D': {'B': 3},
            'E': {'B': 1, 'F': 4},
            'F': {'C': 2, 'E': 4}
        }
        
        resultado = dijkstra_problema1(grafo, 'A')
        
        # Verificar as distâncias
        self.assertEqual(resultado['B'][0], 2)
        self.assertEqual(resultado['C'][0], 5)
        self.assertEqual(resultado['D'][0], 5)
        self.assertEqual(resultado['E'][0], 3)
        self.assertEqual(resultado['F'][0], 7)
        
        # Verificar os caminhos
        self.assertEqual(resultado['B'][1], ['A', 'B'])
        self.assertEqual(resultado['C'][1], ['A', 'C'])
        self.assertEqual(resultado['D'][1], ['A', 'B', 'D'])
        self.assertEqual(resultado['E'][1], ['A', 'B', 'E'])
        self.assertEqual(resultado['F'][1], ['A', 'C', 'F'])





if __name__ == '__main__':
    print("Execute os testes para verificar suas soluções:")
    print("python -m unittest test_dijkstra_problems.py")
    print("\nDICA: Tente resolver cada problema individualmente!")