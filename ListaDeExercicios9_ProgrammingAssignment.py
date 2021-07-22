#Adriano Siqueira - Lista de Exercícios-9 - Programming Assingment - THE FINAL TEST!!! - 07/21/2021

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a assinatura do texto.'''
    tamanho_med_pal = total_letras(texto) / len(texto.split());
    relacao_tt = n_palavras_diferentes(lista_palavras(texto)) / len(texto.split());
    hapax_lego = n_palavras_unicas(lista_palavras(texto)) / len(texto.split());
    tamanho_med_sen = num_char_sen(texto) / len(separa_sentencas(texto));
    complex_sen = num_frases(texto) / len(separa_sentencas(texto));
    tamanho_med_frase = num_char_frase(texto) / num_frases(texto);

    assinatura = [tamanho_med_pal, relacao_tt, hapax_lego, tamanho_med_sen, complex_sen, tamanho_med_frase];

    return assinatura;

    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e 
    deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass


def num_frases(texto):
    frases = 0;
    for sentenca in separa_sentencas(texto):
        frases += len(separa_frases(sentenca));

    return frases;

def num_char_sen(texto):
    caracteres = 0;
    for sen in separa_sentencas(texto):
        caracteres += len(sen);

    return caracteres;

def num_char_frase(texto):
    caracteres = 0;
    for sen in separa_sentencas(texto):
        for frase in separa_frases(sen):
            caracteres += len(frase);

    return caracteres;

def lista_palavras(texto): 
    palavras = [];
    for sentenca in separa_sentencas(texto):
           for frase in separa_frases(sentenca):
               for palavra in separa_palavras(frase):
                   palavras.append(palavra);

    return palavras;

def total_letras(texto):
    letras = 0;
    for sentenca in separa_sentencas(texto):
           for frase in separa_frases(sentenca):
               for palavra in separa_palavras(frase):
                   letras += len(palavra);

    return letras;


calcula_assinatura("Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.");