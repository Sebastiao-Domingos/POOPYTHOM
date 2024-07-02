
class Pessoa :
    __estatico ="sebastiao" 

    def __init__ (self , estado) -> None :
        self.estado = estado

    
    def get_estatico(self):
        print(self.__estatico)


    @classmethod
    def set_estatico(cls, estatico:str):
        cls.__estatico = estatico


class Loja:
    tarifa = 1.03
    def __init__(self, endereco : str) -> None:
        self.__endereco=endereco


    def apresentar(self)->None:
        print(self.__endereco)

    @classmethod
    def alterar_taxa(cls,nova_tarifa:float)-> None:
        cls.tarifa=nova_tarifa

    def vender(self) -> float:
        return self.tarifa*40


loja1 = Loja("Kikolo")

print(loja1.vender())
loja2 = Loja("Viana")
print(loja2.vender())

loja2.alterar_taxa(1.78)
print(loja1.tarifa)
print(loja2.tarifa)

print("="*30)
print("Vender".center(30))

print(loja2.vender())
print(loja1.vender())