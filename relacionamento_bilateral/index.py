from modulos import *

casa_de_amigo = Casa()
ana =Pessoa("Sebastiao Afonso Domingos")


ana.set_local(casa_de_amigo)
casa_de_amigo.set_proprietario(ana)

prorpientario = casa_de_amigo.get_proprietario()

prorpientario.se_apresentar()


local = ana.get_local()

print(local.get_endereco())



print("========== Novo ============")

joao = Pessoa("Paulino")
case_joao =Casa()

joao.set_local(case_joao)
case_joao.set_proprietario(joao)

print(joao.get_local().get_endereco())

