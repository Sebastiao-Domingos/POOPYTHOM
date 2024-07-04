from mae import Mae


class Filha ( Mae ) :
     def __init__(self , nome : str , sobrenome : str , idade : int ) -> None:
          super().__init__(nome  , sobrenome , idade )