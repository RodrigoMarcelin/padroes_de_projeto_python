

class Modelo:

    def __init__(self):
        self.produtos = {
            'ps5': {'id': 1, 'nome': 'Playstation 5', 'preco': 4700},
            'xbox': {'id': 2, 'nome': 'Xbox serie X', 'preco': 4800},
            'nintendo': {'id': 3, 'nome': 'Nintendo swith', 'preco': 2875}
        }

class Controlador:

    def __init__(self):
        self.modelo = Modelo()

    def listar_produtos(self):
        produtos = self.modelo.produtos.keys()

        print('------------Produtos------------')

        for chave in produtos:
            print(f"ID: {self.modelo.produtos[chave]['id']}")
            print(f"Nome: {self.modelo.produtos[chave]['nome']}")
            print(f"Preço: {self.modelo.produtos[chave]['preco']}")
            print('')


class Visao:

    def __init__(self):
        self.controlador = Controlador()

    def produtos(self):
        self.controlador.listar_produtos()


if __name__ == '__main__':
    visao = Visao()
    visao.produtos()