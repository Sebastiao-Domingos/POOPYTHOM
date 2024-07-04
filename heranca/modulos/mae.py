

class Mae :
    def __init__(self , nome : str , sobrenome : str , idade : int) -> None:
         self.nome = nome
         self.sobrenome = sobrenome
         self.idade = idade

    def comer(self)-> None:
         print(f"{self.nome} esta comendo")

    def estudar(self)->None:
         print(f"{self.nome} esta estudando")

    def apresentar(self)->None:
         print(f"{self.nome} {self.sobrenome} tem {self.idade} anos")

class Filha ( Mae ) :
     def __init__(self , nome : str , sobrenome : str , idade : int ) -> None:
          super().__init__(nome  , sobrenome , idade )
         
     def brincar(self)-> None:
      print(f"{self.nome} esta brincando")

    
class Neta(Filha):
     
     def __init__(self , nome : str , sobrenome : str , idade : int ):
          super().__init__(nome  , sobrenome , idade)

clara = Filha("Ana" , "Sebastiao",23)
clara.apresentar()


neta = Neta("Joana" , "Sebastiao" , 45)

neta.brincar()