from dataclasses import dataclass

@dataclass
class Cliente:
    nome : str
    cpf : int
    vivo : bool

    def exibirvivo(self):
        print(self.vivo)

pedro = Cliente(nome="Pedro",cpf=15687452158,vivo=False)

pedro.exibirvivo()