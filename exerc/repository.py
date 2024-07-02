from databases import PostgesDB
class Repository:

    def select(self , db_conection : PostgesDB)->None:
        conection = db_conection.conectar()
        print("Conectei - me no banco {}".format(conection))
        print("fazendo um SELECT *FROM")
        db_conection.desconectar()

    
    def insert(self , db_conection : PostgesDB)->None:
        conection = db_conection.conectar()
        print("Conectei - me no banco {}".format(conection))
        print("fazendo um INSERT INTO")
        db_conection.desconectar()
    
    def delete(self , db_conection : PostgesDB)-> None:
        conection = db_conection.conectar()
        print("Conectei - me no banco {}".format(conection))
        print("fazendo um DELETE FROM")
        db_conection.desconectar()
    
    def update(self , db_conection : PostgesDB)-> None:
        conection = db_conection.conectar()
        print("Conectei - me no banco {}".format(conection))
        print("fazendo um UPDATE SET")
        db_conection.desconectar()