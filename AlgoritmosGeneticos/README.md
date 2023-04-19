# Experimentos de otimização e algoritmos genéticos
- - - -
Nesta pasta você encontrará os experimentos realizados sobre Algoritmos Genéticos e um breve esclarescimento sobre o método.

## Sobre os Algoritmos Genéticos
O funcionamento dos algoritmos genéticos é baseado na evolução de individuos de populações ao longo do tempo, da mesma forma como ocorre na natureza, como descrito por Charles Darwin, onde os indivíduos que se adaptam melhor ao ambiente, são os que mais tem chance de gerar descentendes.
Para construir a base do nosso algoritmo, vamos usar as principais componetnes; gene; individuo; população; objetivo; seleção; mutação; cruzamento.

Gene: Valores que vão formar o individuo. 
Da mesma forma que temos nosso DNA composto de bases nitrogenadas, A, T, C e G, no algoritmo genético utilizamos do mesmo conceito, porém mudando as letras por valores que variam de acordo com nosso problema. Para compreender melhor como funciona, visite o Experimento A.01, onde os genes são valores de 0 e 1 para um problema de caixas binárias

Indivíduo:
População:
Objetivo:
Seleção:
Mutação:
Cruzamento:

## Experimentos
Aqui voce encontrará os experimentos realizados e de grosso modo, o intuíto de cada um deles. Tais experimentos vão estar nomeados como "Experimento A.0X - Nome do experimento"

#### Experimento A.01 - Busca aleatória
A busca aleatória é uma das formas de se encontrar o melhor indivíduo para um problema específico. O método se baseia em 'chutes aleatórios' em um espaço de busca específico. 
Após os genes terem sido escolhidos aleatoriamente, é analisado qual destes selecionados tem o melhor valor.
Por se tratar de uma busca aleatória (ou seja, chutes), nem sempre encontraremos o melhor gene possivel para o problema.

Para ilustrar o funcionamento do método, foi usado o problema das caixas binárias, que consiste em:
4 caixas as quais podem ter em seu interior o valor de 1 ou 0 e, nosso objetivo é encontrar a combinaçao em que a soma dos valores das 4 caixas, seja o maior possível.
Posto isso, vemos que a combunação que atinge o maior valor possível é 1, 1, 1, 1, cuja soma é 4.

#### Experimento A.02 - Busca em Grade
O busca em grade ja é uma forma mais consistente e precisa para encontrar o indivíduo desejado.
Para o funcionamento deste, procuramos cobrir todo o universo de possibiliddes de nosso evento, de forma que não se deixe escapar qualquer combinação

#### Experimento A.03 - Algorítmo genético

#### Experimento A.04 - Caixas não-binarias 

#### Experimento A.05 - Descobrindo a senha
Ja temos a senha - conseguiu descobrir - nao para ate achar a senha

#### Experimento A.06 - O Caixeiro viajante
se eu nao sei a resposta, entao usa criterio parada - NP, nao polinomial - 
#### Experimento A.07 - Aplicando restrições
