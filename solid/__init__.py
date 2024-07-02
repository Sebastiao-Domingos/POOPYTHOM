

class SistemaCadastro:

    def cadastrar(self , nome:str , idade : int) -> None :
        if self.__verificar_dados(nome, idade):
            self.__armazenando_usuariio(nome ,idade)
        else :
            self.__erro("Dados invlidos!")

    def __verificar_dados(self , nome : str , idade : int)->bool:
        """
        This method is responsible for verifying the validity of the user's data.

        Parameters:
        nome (str): The name of the user.
        idade (int): The age of the user.

        Returns:
        bool: True if the data is valid, False otherwise.

        Note:
        This method checks if the 'nome' is a string and 'idade' is an integer.
        """
        if isinstance(nome,str) and isinstance(idade,int):
            return True
        else :
            return False
        
    def __armazenando_usuariio(self, nome, idade)->None:
        print(f"Acessando o banco de dados...")
        print(f"Cadastrando o Usuario {nome} de idade {idade} anos.")

    def __erro(self , sms:str) -> None:
        print(sms)