

class Database :
    def __init__(self) -> None:
        self.__database ="Postgres"
        self._conexao = "//conection_string"
        self.user = "Sebastiao"

    def _get_database(self)-> None:
        print(self.__database)

    
    def _testing_connection(self)-> None:
        print("Conection ok")

    
class Repository(Database):

    def __init__(self)-> None:
        super().__init__()

    def select(self)-> None:
        self._testing_connection()
        print("Connecting up to {}".format(self._conexao))
        print("select *from table")
        

    
db = Database()

print(db._conexao)

repo = Repository()

repo.select()