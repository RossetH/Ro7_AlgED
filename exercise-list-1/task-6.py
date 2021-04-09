class main(object):
    """docstring for """

    def __init__(self):
        self.n = 0
        self.data = []

    def get_n(self):
        while True:
            self.n = int(input('Digite o número N que indica o número de dias que a lista contém.\n'))
            if self.n < 1: 
                print('Por favor forneça um número maior que 1.\n')
            elif self.n > 1000:
                print('Por favor forneça uma lista com menos de 1000 dias.\n')
                pass 
            else:
                break
        
    def get_a(self):
        print('Digite os valores correspondentes aos acessos para cada dia.')
        while True:
            a = int(input())
            if a < 0: 
                print('Por favor forneça um número positivo.\n')
            elif a > 1000000:
                print('Por favor forneça um númerno menor que 1mi.\n')
                pass 
            else:
                break
        return a

    def get_rows(self):
        for _ in range(0,self.n):
            self.data.append(self.get_a())
    
    def compute_days(self):
        i=0
        total_a = 0
        while True:
            total_a += self.data[i]
            if total_a >= 1000000:
                break
            else:
                i += 1
                pass
        print(f'Foram necessários {i+1} dias até chegar ao milionésimo acesso.')

    def run(self):
        self.get_n()
        self.get_rows()
        self.compute_days()

premiodomilhao = main()
premiodomilhao.run()


