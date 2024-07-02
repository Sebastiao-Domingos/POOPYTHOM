

class PostgesDB : 
    def __init__(self):
        self.__conexao = "Postgres"


    def conectar(self):
        print("Conectando a banco Postgress...")
        return self.__conexao


    def desconectar(self):
        print("Desconectar a banco Postgress...")
        return self.__conexao