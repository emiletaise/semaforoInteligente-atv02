import random
from Veiculo import Veiculo

class GeradorVeiculo:

    def gerar_veiculos(agenteTransito, randomico):
        num_faixas = len(agenteTransito.get_faixas())
        total_veiculos_faixas = 100
        if(randomico):
        #(item a) gerar automaticamente (randomicamente) os dados dos sensores para qualquer quantidade N objetos monitorados.
        #Nesse exemplo, os veículos são criados randomicamente e inseridos nas faixas escolhidas randomicamente, para representar a dinâmica do trânsito.
            for id in range(total_veiculos_faixas):
                placa = f"ABC-{random.randint(1000, 9999)}"
                tipo = random.choice(["Carro", "Moto", "Caminhão"])
                veiculo = Veiculo(placa, tipo, id)
                faixa_numero = random.randint(1, num_faixas)
                agenteTransito.monitorar_veiculo(veiculo, faixa_numero)
            return agenteTransito
        else:
        #(item a) gerar automaticamente (randomicamente) os dados dos sensores para qualquer quantidade N objetos monitorados.
        #Nesse exemplo, os veículos são criados randomicamente e inseridos nas faixas uma a uma;
            for id in range(total_veiculos_faixas):
                placa = f"ABC-{random.randint(1000, 9999)}"
                tipo = random.choice(["Carro", "Moto", "Caminhão"])
                veiculo = Veiculo(placa, tipo, id)
                faixa_numero = id%10 + 1
                agenteTransito.monitorar_veiculo(veiculo, faixa_numero)
            return agenteTransito
            
    #(item d.4) Esse método tem complexidade O(2^N) que é grandeza exponencial.
    #Ao receber o agenteTransito e o índice da faixa (f) que está sendo monitorada,
    # o código então passa a adicionar de forma exponencial o número de veículos naquela faixa.
    # Isso indica que o tempo do vermelho vai ser reduzido de forma exponencial também.

    def gerar_veiculos_exponencial(agenteTransito, i, f):
        for x in range(2 ** i):
            placa = f"ABC-{i}"
            tipo = "Carro"
            veiculo = Veiculo(placa, tipo, x)
            agenteTransito.monitorar_veiculo(veiculo, f+1)
        return agenteTransito
               
    # CRIADO PARA AVALIAÇÃO 2:

    def gerar_veiculos_thread(agenteTransito, f):
        total_veiculos_faixas = 100
        #(item a) gerar automaticamente (randomicamente) os dados dos sensores para qualquer quantidade N objetos monitorados.
        #Nesse exemplo, os veículos são criados randomicamente e inseridos nas faixas escolhidas randomicamente, para representar a dinâmica do trânsito.
        for id in range(total_veiculos_faixas):
            placa = f"ABC-{random.randint(1000, 9999)}"
            tipo = random.choice(["Carro", "Moto", "Caminhão"])
            veiculo = Veiculo(placa, tipo, id)
            agenteTransito.monitorar_veiculo(veiculo, f)
        return agenteTransito

            