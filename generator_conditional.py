# -*- coding: utf-8 -*-
import numpy as np
# ---------------------------------------------------------------------------------------------------

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
    less_than = l <= (r - 1) and e <= (r - 1)
    greather_than_zero = l > 0 and e > 0 and r > 0

    if not (less_than and greather_than_zero):
        print("Data Generator Error: Bad Entry.")
        return (None, None, None)
    else:
        if rho:
            matriz_lr = np.random.randint(0, tam + 1, size=(l, r))
            return (matriz_lr)
        else:
            vector = np.random.randint(0, tam + 1, size=r)
            matriz_lr = np.random.randint(0, tam + 1, size=(l, r))
            matriz_er = np.random.randint(0, tam + 1, size=(e, r))

        return (vector, matriz_lr, matriz_er)

# ---------------------------------------------------------------------------------------------------

def generator_conditional(r, l, e, tam=1000, t = 0):
    """
        Entradas:
            r, l, e: Numeros naturais maiores que zero
            tam = tamanho maximo para numero aleatorio
            t = variação maxima do gerador do conjunto Q
        Saidas:
            c: Vetor de tamanho r
            rho: Matriz de ordem l x r
            pi: Matriz de ordem e x r
            rho_r: vetor de tamanho l
            pi_r: vetor de tamanho e
            Q: Conjunto de tamanho r + 1 tal que U0 = Ur
    """

    c, rho, pi = data_generator(r, l, e, tam=tam)

    # Ultima coluna das matrizes Rho e Pi respectivamente
    rho_r = rho[:, -1:]
    pi_r = pi[:, -1:]

    if t == 0:
        t = np.random.randint(0, tam, 1)

    # Q = {U0, U1, U2, ..., Ur-1, U0}
    Q = np.random.randint(0, t, r)
    Q = Q.tolist()
    Q.append(Q[0])
    Q = set([tuple(Q)])
    
    return (c, rho, pi, rho_r, pi_r, Q)
