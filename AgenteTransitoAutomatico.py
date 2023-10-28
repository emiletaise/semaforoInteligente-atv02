from Faixa import Faixa

class AgenteTransitoAutomatico:
    def __init__(self, num_faixas):
        self.num_faixas = num_faixas
        tempo_vermelho_inicial = 30

        self.faixas = [Faixa(i, tempo_vermelho_inicial) for i in range(1, num_faixas + 1)]

    def get_faixas(self):
        return self.faixas
    
    #O sensor detecta o veículo na faixa e adiciona ele na contagem dessa faixa.
    def monitorar_veiculo(self, veiculo, faixa_numero):
        if 1 <= faixa_numero <= self.num_faixas:
            faixa = self.faixas[faixa_numero - 1]
            faixa.adicionar_veiculo(veiculo)

    #Sempre que esse método é chamado, o tempo do foco vermelho do semáforo é recalculado.
    def ajustar_tempo_vermelho(self):
        for faixa in self.faixas:
            faixa.tempo_vermelho = faixa.calcular_tempo_vermelho()

    #Nesse método o estado de cada faixa é impresso:
    #Método com complexidade O(N) pois o laço de repetição vai permanecer até o valor N ser alcançado.
    def imprimir_estado(self):
        print("Estado das Faixas:")
        for faixa in self.faixas:
            print(f"{faixa}")

    #Nesse método o ID da faixa é impresso, permitindo sua identificação.
    #Método com complexidade O(N) pois o laço de repetição vai permanecer até o valor N ser alcançado.
    def imprimir_faixas(self):
        print("Faixas monitoradas:")
        for faixa in self.faixas:
            print(f"Numero da faixa: {faixa.numero}" )


    #Nesse método os veículos de cada faixa são impressos, permitindo a identificação de cada um deles.
    #Método com complexidade O(N^2) pois o laço de repetição está aninhado a outro externo.
    #Essa inserção de um laço em outro garante que para cada uma das N repetições do laço externo, o laço interno repita N vezes, por isso a complexidade O(N^2).
    def imprimir_veiculos(self):
        for faixa in self.faixas:
            print(f"Monitoramento da faixa: {faixa.get_numero()}" )
            for veiculo in faixa.get_veiculos():
                print(f"{veiculo}")


    #Nesse método as faixas que estão sendo monitoradas são ordenadas de acordo com a quantidade de veículos de cada uma.
    #O método tem complexidade O(N^2) pois cada um dos laços de repetição perpassam pelo array de ordem N uma vez, como estão aninhados, para cada vez que o laço superior inicia, ele passa N vezes pelo laço interno, gerando o produto N*N.
    # O Bubble Sort é conhecido por ser um algoritmo de ordenação ineficiente para grandes conjuntos de dados, mas pode ser adequado para listas pequenas ou parcialmente ordenadas.
    def ordenar_faixas(self):
       n = len(self.faixas)
       for i in range(n - 1):
           for j in range(0, n - i - 1):
               if len(self.faixas[j].veiculos) > len(self.faixas[j + 1].veiculos):
                   # Trocar as faixas se a faixa atual tiver mais veículos que a próxima
                   self.faixas[j], self.faixas[j + 1] = self.faixas[j + 1], self.faixas[j]
