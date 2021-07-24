#Adriano Siqueira - Lista de Exercícios-9 - Programming Assingment - THE FINAL TEST!!! - 07/21/2021

import re

def main ():
    '''função para rodar o programa em sua totalidade.''' 
    print("Bem-vindo ao detector automático de Autoria.");
    print("Esse algoritmo identifica qual texto tem maior probabilidade\nde ter sido escrito pelo mesmo autor do texto autoral\n");
    texto_ori = input("Insira o texto autoral: \n");
    ass_cp = calcula_assinatura(texto_ori);
    textos = le_textos();
   
    return print("O texto", avalia_textos(textos, ass_cp), "possui a assinatura mais proxima ao texto autoral dentre os textos apresentados");

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1;
    textos = [];
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):\n\n");
    while texto:
        textos.append(texto);
        i += 1;
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):\n\n");

    return textos;

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto);
    if sentencas[-1] == '':
        del sentencas[-1];
    return sentencas;

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca);

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split();

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict();
    unicas = 0;
    for palavra in lista_palavras:
        p = palavra.lower();
        if p in freq:
            if freq[p] == 1:
                unicas -= 1;
            freq[p] += 1;
        else:
            freq[p] = 1;
            unicas += 1;

    return unicas;

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict();
    for palavra in lista_palavras:
        p = palavra.lower();
        if p in freq:
            freq[p] += 1;
        else:
            freq[p] = 1;

    return len(freq);

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas.'''
    i = 0;
    soma = 0;
    while i < len(as_b):
        soma += abs(as_a[i] - as_b[i]);
        i += 1;

    return soma / 6;


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a assinatura do texto.'''
    tamanho_med_pal = total_letras(texto) / len(texto.split());
    relacao_tt = n_palavras_diferentes(lista_palavras(texto)) / len(texto.split());
    hapax_lego = n_palavras_unicas(lista_palavras(texto)) / len(texto.split());
    tamanho_med_sen = num_char_sen(texto) / len(separa_sentencas(texto));
    complex_sen = num_frases(texto) / len(separa_sentencas(texto));
    tamanho_med_frase = num_char_frase(texto) / num_frases(texto);

    return [tamanho_med_pal, relacao_tt, hapax_lego, tamanho_med_sen, complex_sen, tamanho_med_frase];

    

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e 
    devolve o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 0;
    provavel_cp = 1;
    valor_cp = compara_assinatura(calcula_assinatura(textos[0]), ass_cp);
    while i < len(textos):
        if compara_assinatura(calcula_assinatura(textos[i]), ass_cp) < valor_cp:
            valor_cp = compara_assinatura(calcula_assinatura(textos[i]), ass_cp);
            provavel_cp = i + 1;
        i += 1;

    return provavel_cp;

def num_frases(texto):
    '''Essa função recebe um texto e retorna o numero de frases existentes'''
    frases = 0;
    for sentenca in separa_sentencas(texto):
        frases += len(separa_frases(sentenca));

    return frases;

def num_char_sen(texto):
    '''essa função retorna o numero de caracteres em todas as sentenças de um texto'''
    caracteres = 0;
    for sen in separa_sentencas(texto):
        caracteres += len(sen);

    return caracteres;

def num_char_frase(texto):
    '''essa função retorna o numero de caracteres em todas as frases de um texto'''
    caracteres = 0;
    for sen in separa_sentencas(texto):
        for frase in separa_frases(sen):
            caracteres += len(frase);

    return caracteres;

def lista_palavras(texto): 
    '''Essa função retorna uma lista de palavras contendo todas as palavras do texto'''
    palavras = [];
    for sentenca in separa_sentencas(texto):
           for frase in separa_frases(sentenca):
               for palavra in separa_palavras(frase):
                   palavras.append(palavra);

    return palavras;

def total_letras(texto):
    '''Essa função retorna o número total de letras em um texto'''
    letras = 0;
    for sentenca in separa_sentencas(texto):
           for frase in separa_frases(sentenca):
               for palavra in separa_palavras(frase):
                   letras += len(palavra);

    return letras;

main(); #chamada para a função main