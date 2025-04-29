
# PROBLEMA 5: Roteamento com Conexões Restritas
"""
Descrição:
Em uma rede de transporte aéreo, algumas conexões só estão disponíveis em certos dias da semana.
Você precisa encontrar o caminho mais rápido considerando essas restrições e o tempo mínimo 
necessário para fazer conexões.

A rede é representada como:
rede = {
    ('A', 'B'): {'dias': [1, 3, 5], 'tempo': 2},  # Voo disponível nas segundas, quartas e sextas
    ('A', 'C'): {'dias': [2, 4, 6], 'tempo': 3},  # Voo disponível nas terças, quintas e sábados
    ...
}

O tempo mínimo de conexão é de 1 unidade de tempo em cada aeroporto.
Implemente o algoritmo de Dijkstra modificado para encontrar o caminho mais rápido entre dois aeroportos,
considerando o dia de partida e as restrições de conexão.
"""

def dijkstra_problema5(rede, origem, destino, dia_partida, hora_partida):
    # Implemente o algoritmo de Dijkstra aqui
    pass


class TestProblema5(unittest.TestCase):
    def test_conexoes_restritas(self):
        rede = {
            ('A', 'B'): {'dias': [1, 3, 5], 'tempo': 2},
            ('A', 'C'): {'dias': [2, 4, 6], 'tempo': 3},
            ('B', 'D'): {'dias': [1, 2, 3, 4, 5], 'tempo': 4},
            ('C', 'D'): {'dias': [1, 3, 5, 7], 'tempo': 2},
            ('B', 'E'): {'dias': [2, 4, 6], 'tempo': 3},
            ('D', 'E'): {'dias': [1, 2, 3, 4, 5, 6, 7], 'tempo': 1}
        }
        
        # Partindo na segunda-feira às 8h
        tempo_total, caminho = dijkstra_problema5(rede, 'A', 'E', 1, 8)
        self.assertEqual(tempo_total, 7)  # 2 (A->B) + 4 (B->D) + 1 (D->E) = 7
        self.assertEqual(caminho, ['A', 'B', 'D', 'E'])
        
        # Partindo na terça-feira às 10h
        tempo_total, caminho = dijkstra_problema5(rede, 'A', 'E', 2, 10)
        self.assertEqual(tempo_total, 6)  # 3 (A->C) + 2 (C->D) + 1 (D->E) = 6
        self.assertEqual(caminho, ['A', 'C', 'D', 'E'])

