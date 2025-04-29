
# PROBLEMA 4: Roteamento com Restrições de Tráfego
"""
Descrição:
Uma rede de estradas tem diferentes condições de tráfego em diferentes horas do dia.
O tempo para percorrer uma estrada varia de acordo com o horário.

A rede é representada como:
rede = {
    ('A', 'B'): {9: 5, 12: 7, 15: 9},  # Tempos às 9h, 12h e 15h
    ('A', 'C'): {9: 3, 12: 4, 15: 3},
    ...
}

Implemente o algoritmo de Dijkstra para encontrar o caminho mais rápido entre dois locais,
considerando um horário de partida específico e que o tempo gasto influencia no tráfego das próximas estradas.
"""

def dijkstra_problema4(rede, origem, destino, hora_partida):
    # Implemente o algoritmo de Dijkstra aqui
    pass


class TestProblema4(unittest.TestCase):
    def test_restricoes_trafego(self):
        rede = {
            ('A', 'B'): {9: 5, 12: 7, 15: 9},
            ('A', 'C'): {9: 3, 12: 4, 15: 3},
            ('B', 'D'): {9: 4, 12: 3, 15: 6},
            ('C', 'D'): {9: 6, 12: 5, 15: 4},
            ('B', 'E'): {9: 7, 12: 5, 15: 8},
            ('D', 'E'): {9: 3, 12: 4, 15: 2}
        }
        
        # Adicionar conexões reversas
        reverse_rede = {}
        for (origem, destino), horarios in rede.items():
            reverse_rede[(destino, origem)] = horarios
        rede.update(reverse_rede)
        
        # Testar com partida às 9h
        tempo, caminho = dijkstra_problema4(rede, 'A', 'E', 9)
        self.assertEqual(tempo, 12)  # O tempo total deve ser 12 unidades
        
        # Testar com partida às 12h
        tempo, caminho = dijkstra_problema4(rede, 'A', 'E', 12)
        self.assertEqual(tempo, 13)  # O tempo total deve ser 13 unidades
