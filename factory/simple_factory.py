from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):

    def falar(self):
        print('AU AU')

class Gato(Animal):

    def falar(self):
        print('Miau!')



class Fabrica:

    def criar_animal_falante(self, tipo):
        return eval(tipo)().falar()


#Cliente
if __name__ == '__main__':
    fab = Fabrica()
    animal = input('Qual animal você quer que fale? [Cachorro, Gato]: ')
    fab.criar_animal_falante(animal.title())