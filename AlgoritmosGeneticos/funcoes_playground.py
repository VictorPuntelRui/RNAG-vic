import random 

#### EQUACAO ###################################
def equacao (x, y):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

#####  GENES ###################################
def genes_hbl(valor_max_hbl):
    '''
    gerar valores tanto para x, quanto para y 
    '''
    gene = random.randint(0, valor_max_hbl)
    return gene

##### INDIVIDUO ###################################
def individuo_hbl(n_genes, valor_max_hbl):
    '''
    criar um individuo (lista) com os valores gerados.
    '''
    individuo = []
    for i in range(n_genes):
        gene = genes_hbl(valor_max_hbl)
        individuo.append(gene)
    return individuo

##### POPULACAO ###################################
def populacao_chutes_hbl(tamanho_pop, n_genes, valor_max_hbl):
    '''
    função que cria vários individuos
    Args:
        tamanho_pop: N
        n_genes : numero de genes d cada um
        valor_max_chute: maximo do chute
    '''
    populacao  = []
    for _ in range(tamanho_pop):
        individuo = individuo_hbl(n_genes, valor_max_hbl)
        populacao.append(individuo)
    return populacao
    
##### FITNESS/OBJ ###################################
def fitness_hbl (populacao, equacao):
    '''
    vejo o quão pequeno é meu "Z" (altura) em relação aos outros
    Args:
        individuo: as cordenadas de cada indiv
        equacao: eq para X,Y
    returns:
        result: lista com z's da f(x,y) 
    '''
    fitness=[]
    for individuo in populacao:
        x = individuo[0]
        y = individuo[1]
        z = equacao(x, y)
        fitness.append(z)
    return fitness
    
##### TORNEIO MINIMO ###################################
def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos indivíduos
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)
    return selecionados

##### CRUZAMENTO ###################################
def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1)

    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]

    return filho1, filho2

##### MUTAÇÃO ###################################
def mutacao_cordenada(individuo, valor_max_hbl):
    '''realiza a mutação de um gene no problema das caixas binarias
    arg:
        individuo: uma lista representando um individuo no problema das caixas binarias
    return: 
    um individuo com um gene mutado '''
    
    gene_a_ser_mutado = random.randint(0,len(individuo)-1)
    individuo[gene_a_ser_mutado] = genes_hbl(valor_max_hbl)
    
    return individuo

