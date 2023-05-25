# Experimentos de otimização e algoritmos genéticos
- - - -
Nesta pasta você encontrará os experimentos realizados sobre Algoritmos Genéticos e um breve esclarescimento sobre o método.

## Sobre os Algoritmos Genéticos
O funcionamento dos algoritmos genéticos é baseado na evolução de individuos de populações ao longo do tempo, da mesma forma como ocorre na natureza, como descrito por Charles Darwin, onde os indivíduos que se adaptam melhor ao ambiente, são os que mais tem chance de gerar descentendes.
Para construir a base do nosso algoritmo, vamos usar as principais componetnes; gene; individuo; população; objetivo; seleção; mutação; cruzamento.

##### Gene:
Valores que vão formar o individuo.   
Da mesma forma que temos nosso DNA composto de bases nitrogenadas, A, T, C e G, no algoritmo genético utilizamos do mesmo conceito, porém mudando as letras por valores que variam de acordo com nosso problema. Para compreender melhor como funciona, visite o Experimento A.01 - Busca Aleatória, onde os genes são valores de 0 e 1 para um problema de caixas binárias

##### Indivíduo:
Os indivíduos são os nossos pacotes de dados por assim dizer, o conjunto de dados que vão servir para a solução de meu problema.<dt>
Supondo que queremos gerar indivíduos com coordenadas de uma função, para achar um ponto em um plano cartesiano (podemos pensar em achar a coordenada de um barco no batalha naval), então temos por exemplo, indivíduos com com genes que representam os números na coordenada X e Y:
- indivíduo 1 = 3,2
- indivíduo 2 = 10,4
- indivíduo 3 = 2,8
- indivíduo 4 = 4,7
Ou seja, cada gene é um número e, ao juntar dois genes, temos um indivíduo que, neste caso, é uma coordenada.

##### População:
A população por sua vez, é o conjunto de indivíduos.
<dt>
Assim como na natureza, as mudanças ocorrem nos indivíduos dentro de uma população e, esta população muda conforme o tempo. Por isso é necessário a criação deste operador População.
Quando usamos os alrogitmos genéticos, estamos utilizando a estatística como base. Ao aumentar o número de indivíduos gerados, estamos trazendo as propriedades da aleatoriedade e da probabilística a um patamar acima, visto que, quanto mais indivíduos criados, maior a variação dentro de nosso universo amostral.<dt>

##### Objetivo:
O operador objetivo é basicamente o que queremos que nosso indivíduo tenha que irá agregar valor a ele. <dt>
Supondo que queremos o indivíduo que tenha o número mais alto. Nosso objetivo neste caso é o maior valor possível, fazendo com que o valor dos nossos indivíduos com o número mais alto, tenha um maior peso. <dt>
Comumente, também chamamos este ato de classificar o valor dos indivíduos de "Fitness"
##### Seleção:
Selecionamos os indivíduos que atendam melhor ao nosso problema.<dt>
Em nossa população, teremos vários valores distintos relacionados a cada um dos indivíduos. Com a seleção, pegamos os que melhor atendem aos requisitos determinados em "Objetivo" e os selecionamos para passar as características para a próxima geração. <dt>
Conforme o tempo vai passando, as próximas gerações vao ser cada vez melhores, visto que tem o seu material genético (os genes), com pesos maiores, se aproximando de nossa solução.
##### Mutação:
Para acrescentar ainda mais o fator de estatística e aleatoriedade em nosso algorítmo, a mutação é inserida.
<dt>A mutação é uma alteração que ocorre em um gene dentro de um indivíduo (por ex: indiv1 = ABCD, indivi mutado será ACBD).
<dt>É preciso se atentar bastante neste operador pois, se aumentarmos muito a sua taxa, pode ter um efeito negativo em nosso algorítmo, e se for muito baixo, nao surtirá quase nenhum efeito. É preciso acertar a dose certa de radiação XD
    
##### Cruzamento:
O cruzamento atua após a seleção, quando vamos criar a próxima geração.
<dt>Ao cruzarmos os indivíduos que são os mais adaptados para a situação específica, podemos aumentar a chance de ter um indivíduo mais adaptado ainda. juntando ao fato de que a próxima geração inteira será gerada a partir dos melhores indivíduos da anterior, temos uma melhoria constante.

## Experimentos
Aqui voce encontrará os experimentos realizados e de grosso modo, o intuíto de cada um deles. Tais experimentos vão estar nomeados como "Experimento A.0X - Nome do experimento"

#### <a href="https://github.com/VictorPuntelRui/RNAG-vic/blob/main/AlgoritmosGeneticos/experimento%20A.01%20-%20busca%20aleatoria.ipynb" >Experimento A.01 - Busca Aleatória </a> <br>
A busca aleatória é uma das formas de se encontrar o melhor indivíduo para um problema específico. O método se baseia em 'chutes aleatórios' em um espaço de busca específico. 

Para ilustrar o funcionamento do método, foi usado o problema das caixas binárias, que consiste em:
4 caixas as quais podem ter em seu interior o valor de 1 ou 0 e, nosso objetivo é encontrar a combinaçao em que a soma dos valores das 4 caixas, seja o maior possível.
Posto isso, vemos que a combinação que atinge o maior valor possível é 1, 1, 1, 1, cuja soma é 4.

#### <a href="https://github.com/VictorPuntelRui/RNAG-vic/blob/main/AlgoritmosGeneticos/experimento%20A.02%20-%20busca%20em%20grade.ipynb">Experimento A.02 - Busca em Grade</a> <br>
O busca em grade ja é uma forma mais consistente e precisa para encontrar o indivíduo desejado.
Para o funcionamento deste, procuramos cobrir todo o universo de possibiliddes de nosso evento, de forma que não se deixe escapar qualquer combinação.

#### <a href="https://github.com/VictorPuntelRui/RNAG-vic/blob/main/AlgoritmosGeneticos/experimento%20A.03%20-%20algoritmo%20genetico.ipynb">Experimento A.03 - Algorítmo genético </a> <br>    
Também voltado para otimização do problema das caixas binárias, porém agora utilizando o **algoritmo genético**, aplicando os métodos de gerar os genes, individuos, população, fitness, geração e seleção.

#### <a href="https://github.com/VictorPuntelRui/RNAG-vic/blob/main/AlgoritmosGeneticos/experimento%20A.04%20-%20caixas%20nao-binarias.ipynb">Experimento A.04 - Caixas não-binarias </a> <br>
De forma semelhante ao experimento A03, neste caso as caixas podem assumir valores de 0 a 100.


#### <a href="https://github.com/VictorPuntelRui/RNAG-vic/blob/main/AlgoritmosGeneticos/experimento%20A.05%20-%20descobrindo%20a%20senha.ipynb">Experimento A.05 - Descobrindo a senha </a> <br>
Tenta-se minimizar o erro para encontrar uma senha já conhecida pelo algorítmo. Neste experimento utilizamos como seleção, a função torneio e, como critério de parada, quando não se tem distância entre a senha objetivo e o indivíduo.

#### <a href="https://github.com/VictorPuntelRui/RNAG-vic/blob/main/AlgoritmosGeneticos/experimento%20A.06%20-%20o%20caixeiro%20viajante-Copy1.ipynb">Experimento A.06 - O Caixeiro viajante </a> <br>
Este é um problema classificado como NP-difícil, onde para encontrar a melhor solução, teríamos que varrer todo o espaço amostral. Neste experimento se apresentam novos operadores de mutação e cruzamento, tendo em vista uma característica especial neste problema.

#### <a href="https://github.com/VictorPuntelRui/RNAG-vic/blob/main/AlgoritmosGeneticos/experimento%20A.07%20-%20aplicando%20restricoes-Copy1.ipynb">Experimento A.07 - Aplicando restrições </a> <br> <dt>
Aqui, como o título sugere, aplicamos uma restrição no nosso código no que diz respeito a viabilidade do indivíduo. 
Temos uma mochila a qual queremos otimizar os objetos que podem ser carregados nela, caso o peso ultrapasse a capacidade da mochila, nosso indivíduo é extremamente desvalorizado.
