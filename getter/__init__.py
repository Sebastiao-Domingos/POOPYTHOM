
class Alarme :
    def __init__(self , estado : bool) -> None:
        self.__estado = estado

    def get_estado(self)-> bool:
        return self.__estado

    
    def set_estado(self , estado :bool) ->None:
        if isinstance(estado,bool):
            self.__estado = estado