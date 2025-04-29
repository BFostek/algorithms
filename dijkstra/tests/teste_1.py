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

def dijkstra_problema3(rede, origem, destino):
    # Implemente o algoritmo de Dijkstra aqui
    pass


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


if __name__ == '__main__':
    print("Execute os testes para verificar suas soluções:")
    print("python -m unittest test_dijkstra_problems.py")
    print("\nDICA: Tente resolver cada problema individualmente!")