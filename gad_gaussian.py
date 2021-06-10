import numpy as np

#---------------------------------------------------------------------------------------------------
#----------------------------------- Funçoes Bases -------------------------------------------------
def data_generator(r, l, e, tam=1000, rho=False):
    '''
        Entrada:
            r, l, e: Numeros Naturais maiores que zero
            tam : Valor maximo de cada elemento, padrao: 1000.
            rho : Flag para retornar apenas uma matriz l x r
        Saida:
            vetor: tamanho r, matriz: ordem l x r, matriz: ordem e x r
        Erro:
            tupla: None, print do erro.
    '''
    less_than = l <= (r-1) and e <= (r-1)
    greather_than_zero = l > 0 and e > 0 and r > 0

    if not (less_than and greather_than_zero):
        print("Data Generator Error: Bad Entry.")
        return (None, None, None)
    else:
        if rho:
            matriz_lr = np.random.randint(0, tam+1, size = (l, r))
            return (matriz_lr)
        else: 
            vector = np.random.randint(0, tam+1, size = r)
            matriz_lr = np.random.randint(0, tam+1, size = (l, r))
            matriz_er = np.random.randint(0, tam+1, size = (e, r))

        return (vector, matriz_lr, matriz_er)

#---------------------------------------------------------------------------------------------------
def gaussian(matrix):
    '''
        Entrada:
            matriz: Ordem m x n
        Saída:
            matriz escalonada: Ordem m x n
        Função:
            Escalona uma matriz a sua forma triangular superior através do algoritimo do método 
            da Eliminação Gaussiana.
    '''
    m, n = np.shape(matrix)
    for j in range(m):
        for i in range(m):
            if i > j:
                try:
                    c = -(matrix[i][j] / matrix[j][j])
                    for k in range(n):
                        matrix[i][k] = c * matrix[j][k] + matrix[i][k]
                except ZeroDivisionError:
                    pass
                    
    for x in range(m -1):
         if all(a == 0 for a in matrix[x]):
                matrix[x], matrix[x+1] = matrix[x+1], matrix[x]
    return matrix

#---------------------------------------------------------------------------------------------------
def rank(matrix):
    '''
        Entrada:
            matriz: Ordem m x n
        Saída:
            posto: Quantidade de linhas não nulas de uma matriz escalonada.
    '''
    rows = np.shape(matrix)[0]
    nulls = 0
    for i in range(rows):
        if all(a == 0 for a in matrix[i]):
            nulls += 1
    return (rows - nulls)
#----------------------------------- Fim Funçoes Bases ---------------------------------------------
#---------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------
#----------------------------------- Função principal ----------------------------------------------
def generator_with_gaussian(r, l, e, tam=1000):
    '''
        Entrada:
            r, l, e: Numeros Naturais maiores que zero
            tam : Valor maximo de cada elemento, padrao: 1000.
        Saida:
            vetor: tamanho r, matriz escalonada: ordem l x r, matriz: ordem e x r
        Erro:
            tupla: None, print do erro.
        Função: 
            gerar dados através da função data_generator(r,l,e), escalonar a matriz através
            da função gaussian(matriz), encontrar o posto da matriz escalonada, com a função
            rank(matriz_reduzida), e verificar se o posto é valido, em nosso caso, se ele é r-1.
    '''
    vec, matriz_lr, matriz_er = data_generator(r, l, e, tam=tam)
    reduced = gaussian(matriz_lr)
    rank_matriz = rank(reduced)
    
    while rank_matriz != l:
        matriz_lr = data_generator(r, l, e, tam=tam, rho=True)
        reduced = gaussian(matriz_lr)
        rank_matriz = rank(reduced)
    
    return (vec, reduced, matriz_er)
#----------------------------------- Fim Função principal ------------------------------------------
#---------------------------------------------------------------------------------------------------
