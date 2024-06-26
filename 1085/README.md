# Babel - 1085

## Descrição

Joãozinho e Mariazinha são dois irmãos que estão muito empolgados com suas aulas de idiomas, cada um está fazendo vários diferentes cursinhos. Ao chegar em casa comentam sobre gramática, vocabulário, cultura dos países etc. Numa dessas conversas perceberam que algumas palavras são comuns a mais de um idioma, mesmo que não necessariamente tenham o mesmo significado. Por exemplo, “amigo” existe em português e espanhol e tem o mesmo significado, enquanto que “date” é uma palavra comum entre francês e inglês mas que pode ter significados diferentes, uma vez que “date” também se refere a um encontro em inglês, além de “data” de calendário. Já “red” em espanhol se refere a uma rede, enquanto que em inglês se refere à cor vermelha. Outro exemplo seria “actual” que, em inglês significa algo real e, em espanhol, tem o significado de presente, atual (como em português).

Empolgados com essas descobertas, resolveram escrever num caderno todas as palavras em comum que conseguiram pensar, associando cada uma a um par de idiomas. Observador como é, Joãozinho propˆos um desafio a Mariazinha: dados um idioma de origem e um de destino, escrever uma série de palavras sendo que a primeira necessariamente deveria pertencer ao idioma de origem e a última ao de destino. Duas palavras adjacentes nessa seqüência deveriam necessariamente pertencer a um mesmo idioma. Por exemplo, se o idioma de origem fosse português e o de destino francês, Mariazinha poderia escrever a seqüência amigo actual date (português/espanhol, espanhol/inglês, inglês/francês).

Para a surpresa de Joãozinho, Mariazinha conseguiu resolver o problema com muita facilidade. Irritado com o sucesso de sua irmã, ele resolveu complicar ainda mais o problema com duas restrições: Mariazinha deve encontrar a solução que tenha o menor comprimento da seqüência total não contando os espaços entre as palavras e duas palavras consecutivas não podem ter a mesma letra inicial.

Sendo assim, a solução anterior passa a ser inválida, pois “amigo” e “actual” têm a mesma letra inicial. é possível, porém, encontrar outra solução, que no caso seria amigo red date, cujo comprimento total é 12. Joãozinho fez uma extensa pesquisa na internet e compilou uma enorme lista de palavras e desafiou Mariazinha a resolver o problema. Como é possível que haja mais de uma solução, ele pediu para que ela apenas respondesse o comprimento da seqüência encontrada dadas as restrições ou se não há solução possível. Você seria capaz de ajudar Mariazinha?

## Entrada

A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro M (1 ≤ M ≤ 2000), representando o total de palavras compiladas por Joãozinho. A segunda linha contém duas cadeias de caracteres distintas O e D, separadas por um espaço em branco, indicando os idiomas de origem e destino respectivamente. Cada uma das M linhas seguintes contém três cadeias de caracteres I1, I2 e P, separadas por um espaço em branco, representando dois idiomas e uma palavra comum entre ambos (I1 e I2 são sempre diferentes). Todas as cadeias de caracteres terão tamanho mínimo 1 e máximo 50 e conterão apenas letras minúsculas. Um mesmo par de idiomas pode ter várias palavras diferentes associadas a ele, porém uma mesma palavra P nunca será repetida.

O final da entrada é indicado por uma linha que contém apenas um zero.

## Saída

Para cada caso de teste da entrada seu programa deve imprimir um único inteiro, o comprimento da menor sequência que satisfaça as restrições de Joãozinho, ou impossivel (em minúsculas, sem acento) caso não seja possível.

-------------------------------------------------------------------

## Resolução

1. Modelagem
    - Cada idioma é um nó
    - Cada palavra comum entre dois idiomas uma aresta com peso do comprimento da palavra
    - Duas palavras consecutivas não podem ter a mesma letra inicial

2. Busca de Caminho minimo com Dijkstra:
    - Presença de pesos com comprimento da palavra
    - matriz de distâncias dist[u][c], onde u é um idioma e c é a primeira letra da última palavra usada para chegar a u