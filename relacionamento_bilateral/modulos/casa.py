
class Casa :
    def __init__(self ) -> None:
        self.__endereco = "Rangel , CTT"
        self.__proprietario = None
    
    def acender_luzes(self) -> None:
        print("Luzes acendidas")
    
    def desligar_luzes(self) -> None:
        print("Luzes apagadas")
    
    def get_endereco(self) -> str:
        return self.__endereco

    def get_proprietario(self) -> any:
        return self.__proprietario
    
    def set_endereco(self , novo_endereco : str) -> None:
        self.__endereco = novo_endereco
    
    def set_proprietario(self , novo_proprietario : any) -> None:
        self.__proprietario = novo_proprietario

    

