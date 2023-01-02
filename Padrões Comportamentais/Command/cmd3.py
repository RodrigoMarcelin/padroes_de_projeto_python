from abc import ABCMeta, abstractmethod

class Ordem(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass


class OrdemCompra(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.comprar()

class OrdemVenda(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.comprar()


class OrdemVenda(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.vender()

class Acao:

    def comprar(self):
        print('Você irá comprar ações...')

    def vender(self):
        print('Você irá vender ações')

class Agente:

    def __init__(self):
        self.__fila_ordens = []

    def adicionar_ordem_na_fila(self, ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()

if __name__ == "__main__":

    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    ordem_venda = OrdemVenda(acao)

    agente = Agente()
    agente.adicionar_ordem_na_fila(ordem_compra)
    agente.adicionar_ordem_na_fila(ordem_venda)