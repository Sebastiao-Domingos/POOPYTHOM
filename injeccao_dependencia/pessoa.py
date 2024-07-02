class Casa :
    def __init__(self, nome:str)-> None :
        self.__endereco= f"Rua dos CTT2 , nome : {nome}"
        self.__nome = nome

    def acender_luzes(self) -> None:
        print("Estou acendendo as luzes.")

    def desligar_luzes(self)-> None :
        print("Estou desligar as luzes.")

    def get_endereco(self)->str:
        return self.__endereco
    

class Pessoa:
    def __init__(self , nome:str , local : Casa)->None:
        self.__nome = nome
        self.__local = local

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(f"Estou no endereco {endereco}")

    

casa_de_amigo = Casa("Paulino Passil")
seba = Pessoa("Seba" , casa_de_amigo)

seba.entrar_no_local()
seba.apresentar_local()