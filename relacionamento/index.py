

class Malambarismo :

    def apresentar_show(self):
        print("Malambarismo apresentando seu show.")


class Palhaco:

    def apresentar_show(self):
        print("Palhaco apresentando seu show")


class Circo:

    def apresentar(self, apresentador: Malambarismo | Palhaco)->None:
      apresentador.apresentar_show()

circ = Circo()
ma = Malambarismo()
pa = Palhaco()

circ.apresentar(ma)
circ.apresentar(pa)