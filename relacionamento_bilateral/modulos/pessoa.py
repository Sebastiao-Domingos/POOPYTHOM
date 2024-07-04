

class Pessoa :
    def __init__(self, nome:str) -> None:
        self.__nome = nome
        self.__local = None

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()
        print(f"Estou no endereco {self.__local.get_endereco()}")

    def se_apresentar(self)->None:
        print(f"Meu nome é {self.__nome} e estou no endereco {self.__local.get_endereco()}")

    def set_local(self , local :any)-> None :
        self.__local = local
    
    def get_local(self) -> None:
        return self.__local

