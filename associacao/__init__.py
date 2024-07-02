from typing import Type

class Interruptor :
    def __init__(self, comodo :str)->None :
        self.comodo = comodo
    
    def acender(self, nome:str)-> None:
        print(f"{nome} esta acendendo a luz do (a) {self.comodo}")

    def apagar(self , nome : str) -> None:
        print(f"{nome} esta apagando a luz do (a) {self.comodo}")
        

class Pessoa :
    def __init__(self , nome)->None:
        self.__nome = nome

    def get_nome(self)->str:
        return self.__nome
    
    def set_nome(self  ,novo_nome:str)->None:
        self.__nome = novo_nome

    def acender(self , interruptor : Interruptor)->None:
        interruptor.acender(self.get_nome())
    
    def apagar(self , interruptor :Type[Interruptor])-> None :
        interruptor.apagar(self.get_nome())

    def dormir(self):
        print("Estoudormindo!...")

pess1 = Pessoa("Sebastiao")

pess1.apagar(Interruptor("Quarto"))
pess1.acender(Interruptor("Sala"))
pess1.set_nome("Afonso Domingos")
pess1.apagar(Interruptor("Quarto"))
pess1.acender(Interruptor("Sala"))