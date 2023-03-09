def gene_caixa_binária():
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
        gene = gene_caixa_binária()
        individuo.append(gene)
    return individuo
    
    

def funcao_objetivo_cb(individuo):
    """Computa a função objetivono problema das caixas binárias
    args:
        individuo: lista com os genes das caixas binárias
    return:
        uma valor representando a soma dos genes do indivídu=
    """
    
    return sum(individuo) 
