from numpy import amin, absolute, sqrt, power

class RIM(object):
    """docstring for Reference Ideal Method"""
    
    def __init__(self,matrix,criteria_range,reference_ideal,weights):
        self.matrix = matrix 
        self.columns = len(matrix) #j
        self.rows = len(matrix[0]) #i
        self.criteria_range = criteria_range #[A,B]
        self.reference_ideal = reference_ideal #[C,D]
        self.weights = weights
        self.iplus = []
        self.iminus = []
        self.rank = []
        # criar teste para avaliar ordem dos vetores está correta
        # e avaliar se há mesmo numero de ranges que colunas (critérios)
   
    def d_min(self,x,j):
        return amin([absolute(x-self.reference_ideal[j][0]),
                        absolute(x-self.reference_ideal[j][1])])
    
    def normalize_f(self,x,j):
        if x in range(self.reference_ideal[j][0],self.reference_ideal[j][1]+1):
            return 1
        elif x in range(self.criteria_range[j][0],self.reference_ideal[j][0]):
            return 1 - self.d_min(x,j)/absolute(self.criteria_range[j][0]-self.reference_ideal[j][0])
        elif x in range(self.reference_ideal[j][1],self.criteria_range[j][1]):
            return 1 - self.d_min(x,j)/absolute(self.reference_ideal[j][1]-self.criteria_range[j][1])
        else:
            print('Reference Ideal isn\'t contained in the range [A,B]')
    
    def normalization(self):
        for j in range(0,self.columns):
            for i in range(0,self.rows):
                self.matrix[j][i] = self.normalize_f(self.matrix[j][i],j)
    
    def weighted_normalized_matrix(self):
        for j in range(0,self.columns):
            for i in range(0,self.rows):
                self.matrix[j][i] = self.matrix[j][i]*self.weights[j]
    
    def i_plus(self):
        for i in range(0,self.rows):
            temp_iplus = 0
            for j in range(0,self.columns):
                temp_iplus += power((self.matrix[j][i]-self.weights[j]),2)
            self.iplus.append(sqrt(temp_iplus))
    
    def i_minus(self):
        for i in range(0,self.rows):
            temp_iminus = 0
            for j in range(0,self.columns):
                temp_iminus += power(self.matrix[j][i],2)
            self.iminus.append(sqrt(temp_iminus))
    
    def rank_i(self):
        for i in range(0,self.rows):
            self.rank.append(self.iminus[i]/(self.iplus[i]+self.iminus[i]))
    
    def print_solution(self):
        print(self.rank)

    def solve(self):
        self.normalization()
        self.weighted_normalized_matrix()
        self.i_plus()
        self.i_minus()
        self.rank_i()
        self.print_solution()


matrix = [[30,40,25,27,45],[0,9,0,0,15],[2,1,3,5,2],[3,3,1,3,2],[3,2,3,3,3],[2,2,2,1,4]]

criteria_range = [[23,60],[0,15],[0,10],[1,3],[1,3],[1,5]]

reference_ideal = [[30,35],[10,15],[0,0],[3,3],[3,3],[4,5]]

weights = [0.2262,0.2143,0.1786,0.1429,0.1190,0.1190]

decision = RIM(matrix,criteria_range,reference_ideal,weights)

decision.solve()

