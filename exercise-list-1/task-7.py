class main(object):
    """docstring for """

    def __init__(self):
        self.n = 0
        self.data = []

    def get_n(self):
        while True:
            self.n = int(input('Digite o número N que indica o número de postes.\n'))
            if self.n < 3: 
                print('Por favor forneça um número maior ou igual a 3.\n')
            elif self.n > 1000:
                print('Por favor forneça uma lista com menos de 1000 postes.\n')
                pass 
            else:
                break
    
    def get_x(self):
        x = input('Digite os tamanhos em cm de cada poste separados por espaços.\n')
        self.data = x.split(' ')
        self.data = [int(i) for i in self.data]
        
    def test_x(self):
        flg = True
        for j in range(0,self.n):
            if self.data[j] < 0:
                print('Você forneceu postes com tamanho negativo. Tente novamente.\n')
                flg = False
                break
            elif self.data[j] > 100:
                print('Você forneceu postes com mais de 100cm. Tente novamente.\n')
                flg = False
                break
            else:
              pass
        return flg
    
    def get_data(self):
        while True:
            self.get_x()
            if self.test_x():
                break
            else:
                pass

    def compute(self):
        change = 0
        fix = 0
        i = 0
        for i in range(0,self.n):
            if self.data[i] < 50:
               change += 1
            elif self.data[i] < 85:
                fix += 1
            else:
                pass
        print(f'É necessário substituir {change} postes e consertar {fix} postes.')

    def run(self):
        self.get_n()
        self.get_data()
        self.compute()
        
postes = main()
postes.run()