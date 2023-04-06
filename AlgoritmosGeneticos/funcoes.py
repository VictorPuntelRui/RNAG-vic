###### IMPORTAÇÕES #####

import random



###### FUNÇÕES #####


def gene_cb():
    """gera um GENE válido para o problema das caixas binárias
    
    return:
        um valor zero ou um
    """
    
    lista = [0, 1]
    gene = random.choice(lista)
    return gene

    # pass # -> a função nao faz nada enqt colocamos o pass (quando ficar completa, retiramos o pass para o funcionamento)
    
    
    
def individuo_cb(n):
    """gera um individuo para o problema das caixas binárias
    arg:
        n: numero de genes do indivíduo
    return:
        uma lista com N Genes, cada um é um valor zero ou um
    """
    
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo


    
def populacao_cb(tamanho, n):
    ''''Cria uma populaão para oproblema das caixas binarias
    
    Args: 
        n: numero de genes de um individuo
    
    Returns:
        uma lista onde cada item é um individuo(lista com N genes)'''
    
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao
        
        
def selecao_roleta_max(populacao, fitness):
    ''' seleciona individuos de uma populacao usando o metodo da roleta.
    NOTA: epaneas funciona para problemas de maximização
    
    ARGS: 
        inidivuo: lista contendo os genes das caixas binárias
        fitness: lista com o valor da funcao objetivo dos indiv da pop
    
    Returns:
        população dos individuos'''
    
    populacao_selecionada = random.choices(populacao, weights = fitness, k=len(populacao))
    return populacao_selecionada
    
    


def funcao_objetivo_cb(individuo):
    """Computa a função objetivono problema das caixas binárias
    args:
        individuo: lista com os genes das caixas binárias
    return:
        uma valor representando a soma dos genes do indivídu=
    """
    
    return sum(individuo) 



def funcao_objetivo_pop_cb (populacao):
    '''calcula  a funcao objetivo para todos os membros d euma populacaoi
    
    args
        populacao: lista com todos os individuos da pop
        
    return
        lista de valores representando a fitness de cada individuo da populacao'''
    fitness = []
    for individuo in populacao:
        fobj= funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness
        
##### ##### ##### ##### 

def cruzamento_ponto_simples(pai, mae):
    '''operador de cruzamento de ponto simples
    
    args:
        pai : lista repsesentando um indiv
        mae : lista representando um indv
        
    Return:
        duas listas, sendo que cada uma reespresnta um filho dos pais que foram argumentos.
        '''
    ponto_de_corte = random.randint(1,len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2



def mutacao_cb(individuo):
    '''realiza a mutação de um gene no problema das caixas binarias
    
    arg:
        individuo: uma lista representando um individuo no problema das caixas binarias
    
    return: 
    
    um individuo com um gene mutado '''
    
    gene_a_ser_mutado = random.randint(0,len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    
    return individuo

##########################
#   Aula 3 - 23/03/23    #
##########################
###################
# EXEPERIMENTO 04 #
###################

# gerar o valor que será inserido na caixa
def gene_cnb(valor_max_caixa):
    ''' gera um gene valido para oproblema das caixas não-binárias
    
    Args:
        valor_max)caixa: Valor maximo que a caixa pode assumir
    return: 
        uma lista com n genes. Cada gene é um valor zero ou um
    '''
    gene = random.randint(0, valor_max_caixa)
    return gene
#[gene_cb() for i in range()]


# criar individuo com os 4 genes
def individuo_cnb(numero_genes, valor_max_caixa):
    '''gera um individuo valido para o problema das caixas nao binárias
    Args:
        numero_genes: numero de genes na lista que representa o individuo
        valor_max_caixas: Valor maximo que a caixa pode assumir
    return:
        uma lista que representa um individuo valido para o prpblema das CNB
        
    '''
    individuo = []
    for _ in range(numero_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo


# Criamos a nossa população com vários indivíduos
def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    '''Cria uma populacao de individuos para o problema das caixas NAO binárias
    Args:
        tamanho_populacao: numero de individuos gerados
        numero_genes: numero de genes do individuo
        valor_max_caixa: valor maximo que a caixa pode assumir
    return:
        uma lista onde cada item representa um individuo
    '''
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    return populacao


# Soma dos genes do individuo 
def funcao_objetivo_cnb(individuo):
    '''
    calcula o fitness do individuo para o problema das caixas nao binárias
    Args:
        individuo: lista que representa um individuo dentro do problema das caixas nao binarias
    return: 
        Um valor que representa a soma dos genes, ou seja, o fitness do individuo
    '''
    fitness = sum(individuo)
    return fitness


#
def funcao_objetivo_pop_cnb(populacao):
    '''
    calcula o fitness da populacao completa
    Args
        populacao: lista com todos os individuos da populacao
    return:
        uma lista com o fitness de cada individuo em ordem
    '''
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop


# funcao que vai causar mutacao no individuo
def mutacao_cnb(individuo, valor_max_caixa):
    '''
    realiza a mutação do individuo
    args:
        individuo: indiv que deve sofrer mutacao
        valor_max)caixa: valor maximo que a caixa pode assumir
    return:
        individuo sofreu mutacao
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo

                  ##################
# # # # # # # # # # EXPERIMENTO 05 # # # # # # # # # # # FAZENDO BRINCANDO
                  ##################


# funcoes que preciso definir : - - - - -

#     Gerar uma Senha (com x valores) - gene
#     Armazenar os X valores - individuo
#     Gerar vários indivíduos - População
    
#     Onde quero chegar - Onde estou p/ Objetivo
#     Definir os Valores de cada gene - fitness obj
#     Selção dos mais aptos - valores dos adaptados
#     Mesclar e gerar nova leva - Crossing over e mutalção

# # Gerando o Gene:
# def gene_letra(letras)
#     '''
#     gera um gene - no caso uma letra
#     args:
#         letras que podem ser inseridas no nosso gene
#     return:
#         letra gerada
#     '''
#     letra_gerada = random.choice(letras)
#     return letra_gerada

# def criar_indiv(individuo)
    


# # Gerando os Indivíduos:
# def individuo_senha
#     '''
#     criar um individuo com os genes gerados - armazenar em uma lista
    
#     '''
                   #################    
# # # # # # # # # #  AULA 30/03/23 # # # # # # # # # #
                  ##################
    
def gene_letra(letras):
    """Sorteia uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra


def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado


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
    
    
def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo


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

    
def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca    
    
#################################################################
#                CAIXEIRO VIAJANTE  - EXP 06                    #
#################################################################

# NOVIDADE
def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


# NOVIDADE
def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades

# NOVIDADE
def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes)
    return nomes

# NOVIDADE
def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao

# NOVIDADE
def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.
    Ver pág. 37 do livro do Wirsansky.
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = random.randint(0, len(pai) -2)
    corte2 = random.randint(corte1 + 1, len(pai) -1)
    
    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
            
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
    return filho1, filho2

def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    Args:
      individuo: uma lista representado um individuo.
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)
    
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    
    return individuo
#individuo[indice1], indiviudo[indice2] = individuo[indice2], individuo[indice1]--> outra alternativa mas parece q eh pior
    
# NOVIDADE
def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    for posicao in range(len(individuo) -1):
    
        partida=cidades[individuo[posicao]]
        chegada=cidades[individuo[posicao + 1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
        
    # calculando o caminho de volta para a cidade inicial
    
    partida=cidades[individuo[-1]]
    chegada=cidades[individuo[0]]
    
    percurso=distancia_entre_dois_pontos(partida, chegada)
    distancia= distancia + percurso
    
    return distancia


# NOVIDADE
def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado