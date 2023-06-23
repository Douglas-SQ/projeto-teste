from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self,pontos):
        pass
    @abstractmethod
    def reduzir_claridade(self,pontos):
        pass

class MonitorFullHd(Monitor):
    def aumentar_claridade(self, pontos):
        print(f'aumentando a claridade em {pontos} pontos')
    def reduzir_claridade(self, pontos):
        print(f'reduzindo a claridade em {pontos} pontos')

monitor=MonitorFullHd()
monitor.aumentar_claridade(5)
monitor.reduzir_claridade(8)