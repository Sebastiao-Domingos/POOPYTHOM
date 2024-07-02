class Pessoa :
    def __init__(self , nome:str , idade: int, bi :str):
        self.nome = nome
        self.idade = idade
        self.__bi = bi
    
    def __apresentar_documento(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nBI: {self.__bi}")

    def beber(self , bebida :str):
        if bebida == "alcool" or bebida == "vinho":
            self.__apresentar_documento()

        print(f"{self.nome} esta bebendo {bebida}.")
    
    def correr(self):
        print(f"{self.nom} esta correndo.")


class Calculadora :
    def __init__(self , num1 : int , num2:int):
        self.num1= num1
        self.num2 = num2

    
    def __adicionar(self):
        return self.num1+self.num2
    
    def __multiplicar(self):
        return self.num1 * self.num2
    
    def __subtracao(self):
        return self.num1 -self.num2
    
    def __divisao(self):
        return self.num1 / self.num2
    
    def __potencia(self):
        return self.num1 ** self.num2
    
    def calcular(self,operacao : str):
        if operacao == "+":
            return self.__adicionar()
        
        elif operacao == "*":
            return self.__multiplicar()
        elif operacao == "-":
            return self.__subtracao()
        elif operacao == "/":
            return self.__divisao()
        elif operacao == "**":
            return self.__potencia()


    