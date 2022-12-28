from typing import List, Tuple

class Curso:

    def __init__(self: object, nome: str = 'Curso Padrão', carga_horaria: int = 45) -> None:
        self.__nome = nome
        self.__carga_horaria = carga_horaria


    

curso1: Curso = Curso()
curso2: Curso = Curso(nome='Padrões de Projeto em python')
curso3: Curso = Curso(nome='Orquestração de conteiners com Kubernetes', carga_horaria=23)

nome: str = 'Geek University'
tupla: Tuple = (1, 2, 3, 4, 5)
lista: List = [1, 2, 3, 4, 5]

print(nome[:4], tupla[:5], lista[:4])

class Pessoa:

    def __init__(self: object, nome: str) -> None:
        self.__nome = nome

    def andar(self: object) -> None:
        print('Estou andando...')

class Aluno(Pessoa):

    def __init__(self: object, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.__matricula = matricula

felicity = Aluno('Felicity', '12345')

class Motor:

    def ligar(self: object) -> None:
        print('Motor ligando...')

class Pneu:

    def encher(self: object) -> None:
        print('Pneu cheio')

class Carro:
    
    def __init__(self: object, modelo: str) -> None:
        self.__modelo = modelo
        self.__motor = Motor()
        self.__pneu1 = Pneu()
        self.__pneu2 = Pneu()
        self.__pneu3 = Pneu()
        self.__pneu4 = Pneu()


fusca = Carro()
