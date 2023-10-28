import random
import time

from AgenteTransitoAutomatico import AgenteTransitoAutomatico
from Veiculo import Veiculo
from geradores.GeradorVeiculo import GeradorVeiculo

import threading

def main():

    #Objetos monitorados = Faixas de trânsito
    num_faixas = 10

    agenteTransito = AgenteTransitoAutomatico(num_faixas)

    #Escolher a forma de inserção dos veículos nas faixas:
    randomico = True

    #PARA AVALIAÇÃO 2 - CRIAÇÃO DE FAIXA EM UM SISTEMA DE BAIXA COMPLEXIDADE

    # cenario_um_random(agenteTransito, randomico)

#CENÁRIOS PARA AVALIAÇÃO 2:

    #Com as threads:
    for faixa in agenteTransito.get_faixas():
        thread_faixa = threading.Thread(target=cenario_dois_random, args= (agenteTransito, faixa))
        thread_faixa.start()
        # thread_faixa.join()

    # Imprimir estado inicial do semáforo (processamento d.1)
    # Nessa situação, os veículos foram alocados mas os semáforos recém iniciados estão com com o tempo padrão de 25 segundos.
    agenteTransito.imprimir_faixas()

    # Imprimir a lista de veículos por cada faixa monitorado (processamento d.2)  
    # ATENÇÃO: deve ficar claro quais leituras pertencem a cada um;
    # agenteTransito.imprimir_veiculos()

    # Ajustar o tempo de sinal vermelho
    agenteTransito.ajustar_tempo_vermelho()

    # Imprimir estado após o ajuste
    agenteTransito.imprimir_estado()

    #Aqui acontece a ordenação das faixas, considerando da maior quantidade de veículos para a menor.
    #(item d.3)
    agenteTransito.ordenar_faixas() 

    #Imprimindo novamente as faixas:
##  agenteTransito.imprimir_faixas()

def cenario_um_random(agenteTransito, randomico):
    agenteTransito = GeradorVeiculo.gerar_veiculos(agenteTransito, randomico)

def cenario_dois_random(agenteTransito, f):
    tempos_vermelho = []
    range_grafico = 20
    for i in range(range_grafico):
        agenteTransito = GeradorVeiculo.gerar_veiculos_thread(agenteTransito, f.get_numero() -1)
        agenteTransito.ajustar_tempo_vermelho()
        tempo_vermelho = agenteTransito.faixas[f.get_numero() - 1].get_tempo_vermelho()
        tempos_vermelho.append(tempo_vermelho)
    print(f"Tempos de Sinal Vermelho faixa {f.get_numero()}:", tempos_vermelho)

def cenario_um_exponencial(agenteTransito):
    for f in range(len(agenteTransito.get_faixas())):
        
        tempos_vermelho = []
        # range_grafico = 10
        range_grafico = 10
        for i in range(range_grafico):
            agenteTransito = GeradorVeiculo.gerar_veiculos_exponencial(agenteTransito, i, f)
            agenteTransito.ajustar_tempo_vermelho()
            tempo_vermelho = agenteTransito.faixas[f].get_tempo_vermelho()
            tempos_vermelho.append(tempo_vermelho)
            
        titulo = f'Tempo de Sinal Vermelho vs. Número de Veículos Faixa: {f + 1}'
        print(f"Tempos de Sinal Vermelho faixa {f + 1}:", tempos_vermelho)
       
def cenario_dois_exponencial(agenteTransito, faixa):
        tempos_vermelho = []
        # range_grafico = 10
        range_grafico = 20
        for i in range(range_grafico):
            agenteTransito = GeradorVeiculo.gerar_veiculos_exponencial(agenteTransito, i, faixa.get_numero() - 1)
            agenteTransito.ajustar_tempo_vermelho()
            tempo_vermelho = agenteTransito.faixas[faixa.get_numero() - 1].get_tempo_vermelho()
            tempos_vermelho.append(tempo_vermelho)
            
        # print(f"Tempos de Sinal Vermelho faixa {faixa.get_numero()}:", tempos_vermelho)

        print(f"Tempos de Sinal Vermelho faixa {faixa.get_numero()}:", tempos_vermelho)

if __name__ == "__main__":  
    main()