class main(object):
    """docstring for """

    def __init__(self):
        self.n = 0
        self.map = [0,0]
        self.position=[0,0]
    
    def get_map(self):
        self.map[0] = int(input('Digite o número de linhas do mapa:\n'))-1
        self.map[1] = int(input('\nDigite o número de colunas do mapa:\n'))-1
    
    def get_position(self):
        self.position[0] = int(input('\nDigite a linha da posição inicial:\n'))
        self.position[1] = int(input('\nDigite a coluna da posição inicial\n'))

    def go_to(self):
        print(f'\nVocê está em ({self.position[0]},{self.position[1]})')

    def death(self):
        print('\nVocê morreu!')
        print('\nGame Over')
        quit()
    
    def get_direction(self):
        x=int(input('\nInsira a direção:\n'))
        if x == 1:
            if self.position[0] != 0:
                self.position[0] -= 1
                self.go_to()
            else:
                self.death()

        if x == 2:
            if self.position[0] != 0 and self.position[1] != self.map[1]:
                self.position[0] -= 1
                self.position[1] += 1
                self.go_to()
            elif self.position[0] == 0 and self.position[1] != self.map[1]:
                self.position[1] += 1
            else:
                self.death()
        if x == 8:
            if self.position[0] != 0 and self.position[1] != 0:
                self.position[0] -= 1
                self.position[1] -= 1
                self.go_to()
            elif self.position[0] == 0 and self.position[1] != 0:
                self.position[1] -= 1
            else:
                self.death()

        if x == 3:
            if self.position[1] != self.map[1]:
                self.position[1] += 1
                self.go_to()
            else:
                self.death()
        if x == 7:
            if self.position[1] != 0:
                self.position[1] -= 1
                self.go_to()
            else:
                self.death()

        if x == 4:
            if self.position[0] != self.map[0] and self.position[1] != self.map[1]:
                self.position[0] += 1
                self.position[1] += 1
                self.go_to()
            elif self.position[0] == self.map[0] and self.position[1] != self.map[1]:
                self.position[1] += 1
            else:
                self.death()
        if x == 6:
            if self.position[0] != 0 and self.position[1] != self.map[1]:
                self.position[0] -= 1
                self.position[1] -= 1
                self.go_to()
            elif self.position[0] == self.map[0] and self.position[1] != self.map[1]:
                self.position[1] -= 1
            else:
                self.death()

        if x == 5:
            if self.position[0] != self.map[0]:
                self.position[0] += 1
                self.go_to()
            else:
                self.death()
    
    def run(self):
        self.get_map()
        self.get_position()
        while True:
            if self.position == [0,3]:
                print('Você achou o Tesouro!')
            else:
                pass
            self.get_direction()

game = main()
game.run()