
# PROBLEMA 3: Redes de Transporte com Múltiplos Meios
"""
Descrição:
Uma cidade tem múltiplos meios de transporte (ônibus, metrô e a pé) entre diferentes 
locais. Cada meio de transporte tem seu próprio tempo de viagem.

A rede é representada como um dicionário onde as chaves são tuplas (origem, destino) e os 
valores são dicionários com os meios de transporte e seus tempos:

rede = {
    ('A', 'B'): {'onibus': 5, 'metro': 3, 'pe': 10},
    ('A', 'C'): {'onibus': 7, 'pe': 14},
    ...
}

Implemente o algoritmo de Dijkstra para encontrar o caminho mais rápido entre dois locais,
considerando que você pode trocar de meio de transporte a qualquer momento em qualquer local.
"""



class TestProblema3(unittest.TestCase):
    def test_rede_transporte(self):
        rede = {
            ('A', 'B'): {'onibus': 5, 'metro': 3, 'pe': 10},
            ('A', 'C'): {'onibus': 7, 'pe': 14},
            ('B', 'C'): {'onibus': 2, 'metro': 4, 'pe': 8},
            ('B', 'D'): {'metro': 6, 'pe': 12},
            ('C', 'D'): {'onibus': 3, 'pe': 5},
            ('C', 'E'): {'metro': 8, 'pe': 15},
            ('D', 'E'): {'onibus': 4, 'metro': 2, 'pe': 7}
        }
        
        # Adicionar conexões reversas (considerando grafo não direcionado)
        reverse_rede = {}
        for (origem, destino), meios in rede.items():
            reverse_rede[(destino, origem)] = meios
        rede.update(reverse_rede)
        
        tempo, caminho, meios = dijkstra_problema3(rede, 'A', 'E')
        
        # O caminho mais rápido de A para E deve levar 13 unidades de tempo
        self.assertEqual(tempo, 13)
        
        # Verificar se o caminho é válido (A -> B -> D -> E)
        self.assertEqual(caminho, ['A', 'B', 'D', 'E'])
        
        # Verificar os meios de transporte usados
        self.assertEqual(meios, ['metro', 'metro', 'metro'])
