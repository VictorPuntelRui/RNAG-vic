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
# EXPERIMENTO 05 #
##################


# funcoes que preciso definir : - - - - -

#     Gerar uma Senha (com x valores) - gene
#     Armazenar os X valores - individuo
#     Gerar vários indivíduos - População
    
#     Onde quero chegar - Objetivo
#     Definir os Valores de cada gene - fitness obj
#     Selção dos mais aptos - valores dos adaptados
#     Mesclar e gerar nova leva - Crossing over e mutalção

# Gerando o Gene:
def gene_letra(letras)
    '''
    gera um gene - no caso uma letra
    args:
        letras que podem ser inseridas no nosso gene
    return:
        letra gerada
    '''
    letra_gerada = random.choice(letras)
    return letra_gerada

# Gerando os Indivíduos:
def individuo_senha
    '''
    criar um individuo com os genes gerados - armazenar em uma lista
    
    '''
