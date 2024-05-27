# Arte Valiosa - 2962

## Descrição

A Mona Dura é uma das obras de arte mais valiosas do museu da Nlogônia. A famosa pintura fica em exibição num salão retangular de ``M`` por ``N`` metros. A entrada do salão fica em um canto, e a Mona fica no canto diagonalmente oposto à entrada.

Para impedir roubos, o salão dispõe de sensores de movimento, que são ativados toda noite quando o museu fecha. Cada sensor tem um valor de sensibilidade ``S``, tal que o sensor dispara um alarme se detectar qualquer movimento a no máximo S metros de distância dele.

Um ladrão invadiu o museu esta noite com a intenção de roubar a Mona Dura. Para isso, ele precisa entrar no salão e chegar até a pintura sem ser detectado por nenhum sensor de movimento. Ou seja, ele tem que manter uma distância maior do que S i metros do i-ésimo sensor o tempo todo, para todos os sensores.

O ladrão obteve acesso às plantas do museu, e portanto sabe as dimensões do salão e as coordenadas e sensibilidades de cada um dos sensores. Dadas essas informações, sua tarefa é determinar se o roubo é possı́vel ou não.

## Entrada

A primeira linha contém três inteiros, M, N e K, as dimensões do salão e o número de sensores de movimento, respectivamente (10 ≤ M, N ≤ 104 , 1 ≤ K ≤ 1000). A entrada do salão fica no ponto (0, 0) e a pintura fica no ponto (M, N).

Cada uma das K linhas seguintes corresponde a um dos K sensores e contém três inteiros, X, Y e S, onde (X, Y) indica a localização do sensor e S indica a sua sensibilidade (0 < X < M, 0 < Y < N, 0 < S ≤ 104). Todas as dimensões e coordenadas da entrada são em metros. É garantido que todos os sensores têm coordenadas distintas.