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