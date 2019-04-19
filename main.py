import sys
import os
from merge_sort import merge_sort
from bucket_sort import bucket_sort
from quick_sort import quick_sort
from utils import insere_randomico
from gera_relatorio import gera_csv_resultado, plot_grafico
import time
import random
import pandas as pd


def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Comparacao bucket sort, merge sort, e quick sort")
    print("2. Gera csv com relatório dos tempos de ordenação dos algoritmos")
    print("3. Sair")
    print(67 * "-")


def seleciona_algoritmo(algoritmo, lista, tempo_ordenacao, nome_algoritmo):
    for i in range(1000,11000, 1000):
        inicio_cronometagem = time.time()
        algoritmo(lista)
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_ordenacao[nome_algoritmo][i] = tempo_cronometragem
        insere_randomico(lista, 100)    

if __name__ == '__main__':
    loop=True
    tempo_ordenacao_python = {'bucket_sort': {1000: 0, 2000: 0,
                  3000: 0, 4000: 0, 5000: 0, 6000: 0,
                  7000: 0, 8000: 0, 9000: 0, 10000: 0},
                  'merge_sort':{}, 'quick_sort': {} }
    tempo_ordenacao_python['merge_sort'].update(tempo_ordenacao_python['bucket_sort'])
    tempo_ordenacao_python['quick_sort'].update(tempo_ordenacao_python['bucket_sort'])
    tamanho_vetor = 1000    

    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-3]: ")
        if choice=='1':     
            print("Opcao 1 foi escolhida")
            lista = random.sample(range(0,tamanho_vetor * 2), tamanho_vetor)
            seleciona_algoritmo(merge_sort, lista, tempo_ordenacao_python, 'merge_sort')
            seleciona_algoritmo(quick_sort, lista, tempo_ordenacao_python, 'quick_sort')
            seleciona_algoritmo(bucket_sort, lista, tempo_ordenacao_python, 'bucket_sort')
            print(tempo_ordenacao_python)
            plot_grafico(tempo_ordenacao_python)
        elif choice=='2':
            print("Opcao 1 foi escolhida")
            lista = random.sample(range(0,tamanho_vetor * 2), tamanho_vetor)
            seleciona_algoritmo(merge_sort, lista, tempo_ordenacao_python, 'merge_sort')
            seleciona_algoritmo(quick_sort, lista, tempo_ordenacao_python, 'quick_sort')
            seleciona_algoritmo(bucket_sort, lista, tempo_ordenacao_python, 'bucket_sort')
            gera_csv_resultado(tempo_ordenacao_python)
        elif choice=='3':
            print("Opcao 3 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")