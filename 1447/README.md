# Arte Valiosa - 2962

## Descrição

Um grupo de amigos resolveu ir à Alemanha para apoiar a seleção brasileira em sua jornada gloriosa rumo ao hexa. Como as passagens aéreas e as estadias eram caras, cada um trouxe uma quantidade de dinheiro que julgou suﬁciente para passar o mês com conforto e voltar para casa sem problemas.

Porém, após a bela campanha do Brasil na copa do mundo, o grupo de amigos se viu obrigado a gastar o dinheiro que tinha guardado para as etapas ﬁnais da copa com a famosa cerveja alemã. As consequências de tais atos foram terríveis. Após uma grande bebedeira, todos foram pegos pela polícia local dormindo na rua, e receberam multas pesadíssimas. Além disso, todos perderam suas passagens de volta. Devido a esses contratempos, a viagem de volta ﬁcou ameaçada. De repente, eles descobriram que precisavam voltar para casa gastando a menor quantidade possível de dinheiro.

Analisando as rotas aéreas disponíveis, os amigos notaram que em todas as rotas o número de assentos disponíveis nos aviões era sempre o mesmo. Porém, os preços das viagens entre uma cidade e outra eventualmente variavam bastante. Assustados com a possibilidade de não encontrar lugares suﬁciente nos aviões para que todos pudessem voltar e preocupados em gastar a menor quantidade possível de dinheiro, o grupo de amigos resolveu pedir sua ajuda.


## Entrada

O problema é composto por várias instâncias. Cada instância começa com uma linha com dois inteiros positivos N (2 ≤ N ≤ 100) e M (1 ≤ M ≤ 5000), onde N é o número de cidades que pertencem às M rotas de voo consideradas. Os amigos querem ir da cidade 1 até a cidade N.

Nas próximas M linhas são fornecidos triplas de inteiros A B C descrevendo a rota do avião (A e B) e o preço da passagem aérea por pessoa (C). Os valores de A e B estão entre 1 e n. As rotas são bidirecionais (ou seja, há um voo de A até B e um voo de B até A com preço C) e haverá no máximo uma rota entre duas cidades. Na próxima linha são dados dois inteiros, D e K, onde D é o número de amigos e K é o número de assentos livres em cada voo. Cada rota só pode ser utilizada uma vez.

## Saída

Para cada instância, imprima a linha "Instancia k", onde k é o número da instância atual. Além disso, imprima a menor quantidade possível de dinheiro que os amigos vão gastar para voltar ao Brasil (que está limitada por 1015). Caso não seja possível escolher um conjunto de voos que levem todos para casa, imprima "impossivel".

Imprima uma linha em branco após cada instância.