class Pessoa:

    def se_apresentar(self)-> None : 
        print("Estou me apresentando !")

class PessoA(Pessoa) :
    def __init__(self)-> None :
        super.__init__()

    def se_apresentar(self) -> None:
        print("Alterado.....")

pess = Pessoa()

pess.se_apresentar()



def apresentar(): 
    print("oal , como eestas !")

pess.se_apresentar = apresentar


pess .se_apresentar()



pess1 = PessoA()

pess1.se_apresentar()