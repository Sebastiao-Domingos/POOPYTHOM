

class MinaClass:
    def __init__(self,nome)->None:
        self.nome = nome

    @staticmethod
    def apresentar():
        print(f"ola como estatico metodo")





MinaClass.apresentar()


class Error :
    variavel :str= "oladsfadsfa"
    @staticmethod
    def error_500():
        print("Interval Server error")
    

    @staticmethod 
    def error_401():
        print("Not found")

    @staticmethod 
    def error_400():
        print("bad request")

    @classmethod
    def apresentar(cls, var:str) -> None:
        cls.variavel = var

def linha()-> None :print("="*30)


linha()
print("Error".center(30))
linha()


Error.error_400()
err = Error()


err.error_500()


linha()

erro = Error()

erro.apresentar("Sebastiao Afonso")


print(err.variavel)