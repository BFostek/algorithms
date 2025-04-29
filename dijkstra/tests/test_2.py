
# PROBLEMA 2: Encontrando o Caminho Mais Curto em uma Grade
"""
Descrição:
Implemente o algoritmo de Dijkstra para encontrar o caminho mais curto em uma grade 
representada como uma matriz, onde cada célula contém um custo para ser atravessada.

A grade é representada como:
grade = [
    [1, 3, 1, 2],
    [1, 9, 8, 2],
    [5, 2, 1, 1],
    [4, 1, 7, 1]
]

Você pode se mover apenas nas quatro direções cardeais (norte, sul, leste, oeste).
A função deve retornar o custo mínimo para ir da origem ao destino, e o caminho percorrido.
"""

def dijkstra_problema2(grade, origem, destino):
    # Implemente o algoritmo de Dijkstra aqui
    pass


class TestProblema2(unittest.TestCase):
    def test_caminho_em_grade(self):
        grade = [
            [1, 3, 1, 2],
            [1, 9, 8, 2],
            [5, 2, 1, 1],
            [4, 1, 7, 1]
        ]
        
        # Testar caminho do canto superior esquerdo (0,0) ao canto inferior direito (3,3)
        custo, caminho = dijkstra_problema2(grade, (0, 0), (3, 3))
        self.assertEqual(custo, 11)  # O custo mínimo deve ser 11
        
        # Verificar se o caminho é válido
        self.assertEqual(len(caminho), 8)  # Deve ter 8 células no caminho
        
        # Calcular o custo total pelo caminho encontrado
        custo_total = sum(grade[y][x] for x, y in caminho)
        self.assertEqual(custo_total, 11)
        
        # Testar outro caminho
        custo, caminho = dijkstra_problema2(grade, (0, 0), (2, 1))
        self.assertEqual(custo, 7)  # O custo mínimo deve ser 7
