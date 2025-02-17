class registro():
    def amigo_tempo(self,tipo,numero):
        if tipo == 'R' or tipo == 'E':
            self.tipo = tipo
            self.numero = numero
            self.tempo += 1
        else:
            self.tempo += numero
    def tempo(self,tempo):
        self.tempo = tempo

tempo = registro()
tempo.tempo(0)

for cont in range(int(input())):
    inpt = 