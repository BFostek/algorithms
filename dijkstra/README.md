# Algoritmo de Dijkstra - Problemas e Implementações

Este documento apresenta uma coleção de problemas para praticar implementações do algoritmo de Dijkstra.

## Sobre o Algoritmo de Dijkstra

O algoritmo de Dijkstra é um algoritmo clássico de busca de caminho mais curto em grafos ponderados. Ele calcula o caminho mais curto entre um nó origem e todos os outros nós do grafo.

```mermaid
flowchart TD
    A[Inicialização] --> B[Selecionar nó não visitado com menor distância]
    B --> C{Todos os nós visitados?}
    C -->|Sim| D[Fim do algoritmo]
    C -->|Não| E[Atualizar distâncias dos vizinhos]
    E --> F[Marcar nó como visitado]
    F --> B
```

## Problema 1: Caminho Mais Curto em um Grafo Simples

### Descrição
Implemente o algoritmo de Dijkstra para encontrar o caminho mais curto de um nó origem para todos os outros nós em um grafo simples representado como um dicionário de adjacências.

### Representação do Grafo

```mermaid
graph LR
    A --- B
    A --- C
    B --- D
    B --- E
    C --- F
    E --- F
    
    linkStyle 0 stroke-width:2px,fill:none,stroke:blue;
    linkStyle 1 stroke-width:2px,fill:none,stroke:green;
    linkStyle 2 stroke-width:2px,fill:none,stroke:purple;
    linkStyle 3 stroke-width:2px,fill:none,stroke:orange;
    linkStyle 4 stroke-width:2px,fill:none,stroke:red;
    linkStyle 5 stroke-width:2px,fill:none,stroke:brown;
```

```mermaid
graph LR
    A --2--- B
    A --5--- C
    B --3--- D
    B --1--- E
    C --2--- F
    E --4--- F
```

### Estrutura do Grafo
```
grafo = {
    'A': {'B': 2, 'C': 5},  # Do nó 'A' para 'B' o peso é 2, para 'C' o peso é 5
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'A': 5, 'F': 2},
    'D': {'B': 3},
    'E': {'B': 1, 'F': 4},
    'F': {'C': 2, 'E': 4}
}
```

### Resultado Esperado
Caminhos mais curtos a partir do nó 'A':
- A → B: distância = 2, caminho = ['A', 'B']
- A → C: distância = 5, caminho = ['A', 'C']
- A → D: distância = 5, caminho = ['A', 'B', 'D']
- A → E: distância = 3, caminho = ['A', 'B', 'E']
- A → F: distância = 7, caminho = ['A', 'C', 'F']

## Problema 2: Encontrando o Caminho Mais Curto em uma Grade

### Descrição
Implemente o algoritmo de Dijkstra para encontrar o caminho mais curto em uma grade representada como uma matriz, onde cada célula contém um custo para ser atravessada.

### Representação da Grade

```mermaid
graph TD
    subgraph "Grade de Custos"
    A1[1] --- A2[3] --- A3[1] --- A4[2]
    A1 --- B1[1]
    A2 --- B2[9]
    A3 --- B3[8]
    A4 --- B4[2]
    B1 --- B2 --- B3 --- B4
    B1 --- C1[5]
    B2 --- C2[2]
    B3 --- C3[1]
    B4 --- C4[1]
    C1 --- C2 --- C3 --- C4
    C1 --- D1[4]
    C2 --- D2[1]
    C3 --- D3[7]
    C4 --- D4[1]
    D1 --- D2 --- D3 --- D4
    end
```

### Estrutura da Grade
```
grade = [
    [1, 3, 1, 2],
    [1, 9, 8, 2],
    [5, 2, 1, 1],
    [4, 1, 7, 1]
]
```

### Caminho de Menor Custo
Caminho de (0,0) para (3,3):
```mermaid
graph TD
    subgraph "Caminho Mínimo"
    A1[1] --- A2[3]
    A2 --- B2[9]
    B2 --- C2[2]
    C2 --- C3[1]
    C3 --- C4[1]
    C4 --- D4[1]
    
    style A1 fill:#90EE90
    style D4 fill:#FF6347
    style A2 fill:#ADD8E6
    style B2 fill:#ADD8E6
    style C2 fill:#ADD8E6
    style C3 fill:#ADD8E6
    style C4 fill:#ADD8E6
    end
```

## Problema 3: Redes de Transporte com Múltiplos Meios

### Descrição
Uma cidade tem múltiplos meios de transporte (ônibus, metrô e a pé) entre diferentes locais. Cada meio de transporte tem seu próprio tempo de viagem.

### Representação da Rede de Transporte

```mermaid
graph TD
    A --- B
    A --- C
    B --- C
    B --- D
    C --- D
    C --- E
    D --- E
    
    classDef bus stroke:#FF6347,stroke-width:2px
    classDef metro stroke:#4169E1,stroke-width:2px
    classDef walk stroke:#2E8B57,stroke-width:2px
    
    linkStyle 0 stroke:#FF6347,stroke-width:2px
    linkStyle 0 stroke-dasharray: 5 5
    linkStyle 1 stroke:#2E8B57,stroke-width:2px
    linkStyle 2 stroke:#FF6347,stroke-width:2px
    linkStyle 3 stroke:#4169E1,stroke-width:2px
    linkStyle 4 stroke:#FF6347,stroke-width:2px
    linkStyle 5 stroke:#4169E1,stroke-width:2px
    linkStyle 6 stroke:#4169E1,stroke-width:2px
```

### Estrutura da Rede
```
rede = {
    ('A', 'B'): {'onibus': 5, 'metro': 3, 'pe': 10},
    ('A', 'C'): {'onibus': 7, 'pe': 14},
    ('B', 'C'): {'onibus': 2, 'metro': 4, 'pe': 8},
    ('B', 'D'): {'metro': 6, 'pe': 12},
    ('C', 'D'): {'onibus': 3, 'pe': 5},
    ('C', 'E'): {'metro': 8, 'pe': 15},
    ('D', 'E'): {'onibus': 4, 'metro': 2, 'pe': 7}
}
```

### Caminho Mais Rápido
Caminho mais rápido de A para E:
- A → B → D → E (usando metrô em todo percurso)
- Tempo total: 13 unidades

## Problema 4: Roteamento com Restrições de Tráfego

### Descrição
Uma rede de estradas tem diferentes condições de tráfego em diferentes horas do dia. O tempo para percorrer uma estrada varia de acordo com o horário.

### Representação da Rede com Horários

```mermaid
graph TD
    A --- B
    A --- C
    B --- D
    B --- E
    C --- D
    D --- E
    
    subgraph "Horários"
    h9[9h]
    h12[12h]
    h15[15h]
    end
    
    classDef t9 fill:#90EE90
    classDef t12 fill:#ADD8E6
    classDef t15 fill:#FFA07A
    
    class h9 t9
    class h12 t12
    class h15 t15
```

### Estrutura da Rede com Horários
```
rede = {
    ('A', 'B'): {9: 5, 12: 7, 15: 9},
    ('A', 'C'): {9: 3, 12: 4, 15: 3},
    ('B', 'D'): {9: 4, 12: 3, 15: 6},
    ('C', 'D'): {9: 6, 12: 5, 15: 4},
    ('B', 'E'): {9: 7, 12: 5, 15: 8},
    ('D', 'E'): {9: 3, 12: 4, 15: 2}
}
```

### Resultados Esperados
- Partindo às 9h: Tempo total = 12
- Partindo às 12h: Tempo total = 13

## Problema 5: Roteamento com Conexões Restritas

### Descrição
Em uma rede de transporte aéreo, algumas conexões só estão disponíveis em certos dias da semana. Você precisa encontrar o caminho mais rápido considerando essas restrições e o tempo mínimo necessário para fazer conexões.

### Representação da Rede de Voos

```mermaid
graph TD
    A --- B
    A --- C
    B --- D
    B --- E
    C --- D
    D --- E
    
    subgraph "Dias da Semana"
    d1[Segunda]
    d2[Terça]
    d3[Quarta]
    d4[Quinta]
    d5[Sexta]
    d6[Sábado]
    d7[Domingo]
    end
```

### Estrutura da Rede de Voos
```
rede = {
    ('A', 'B'): {'dias': [1, 3, 5], 'tempo': 2},
    ('A', 'C'): {'dias': [2, 4, 6], 'tempo': 3},
    ('B', 'D'): {'dias': [1, 2, 3, 4, 5], 'tempo': 4},
    ('C', 'D'): {'dias': [1, 3, 5, 7], 'tempo': 2},
    ('B', 'E'): {'dias': [2, 4, 6], 'tempo': 3},
    ('D', 'E'): {'dias': [1, 2, 3, 4, 5, 6, 7], 'tempo': 1}
}
```

### Resultados Esperados
- Partindo na segunda-feira às 8h: 
  - Caminho: A → B → D → E 
  - Tempo total: 7
- Partindo na terça-feira às 10h: 
  - Caminho: A → C → D → E 
  - Tempo total: 6

## Implementação do Algoritmo de Dijkstra

```mermaid
stateDiagram-v2
    [*] --> Inicializar
    Inicializar --> SelecionarProximo: Inicializa distâncias\ne predecessores
    SelecionarProximo --> VerificarFim: Seleciona nó com\nmenor distância
    VerificarFim --> [*]: Todos nós visitados\nou destino encontrado
    VerificarFim --> AtualizarVizinhos: Ainda há nós\npara visitar
    AtualizarVizinhos --> MarcarVisitado: Atualiza distâncias\ne predecessores
    MarcarVisitado --> SelecionarProximo: Marca nó atual\ncomo visitado
```

## Dicas para Implementação

1. Use uma fila de prioridade (priority queue) para selecionar o próximo nó com menor distância.
2. Mantenha um conjunto de nós já visitados.
3. Para cada problema, adapte a estrutura de dados e a função de cálculo de distância conforme necessário.
4. Lembre-se de rastrear não apenas as distâncias, mas também os caminhos percorridos.
5. Nos problemas com restrições temporais, considere incluir o tempo/dia na representação do estado.