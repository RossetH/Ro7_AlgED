from numpy import amin, absolute, sqrt, power, argsort
from sys import maxsize

class RIM(object):
    """docstring for Reference Ideal Method"""
    
    def __init__(self,matrix,criteria_range,reference_ideal,wheights):
        self.matrix = matrix 
        self.columns = len(matrix) #j
        self.rows = len(matrix[0]) #i
        self.criteria_range = criteria_range #[A,B]
        self.reference_ideal = reference_ideal #[C,D]
        self.wheights = wheights
        self.Iplus = []
        self.Iminus = []
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
        #    quit() 
    
    def normalization(self):
        for j in range(0,self.columns):
            for i in range(0,self.rows):
                self.matrix[j][i] = self.normalize_f(self.matrix[j][i],j)
    
    def weighted_normalized_matrix(self):
        for j in range(0,self.columns):
            for i in range(0,self.rows):
                self.matrix[j][i] = self.matrix[j][i]*self.wheights[j]
    
    def I_plus(self):
        for i in range(0,self.rows):
            temp_Iplus = 0
            for j in range(0,self.columns):
                temp_Iplus += power((self.matrix[j][i]-self.wheights[j]),2)
            self.Iplus.append(sqrt(temp_Iplus))
    
    def I_minus(self):
        for i in range(0,self.rows):
            temp_Iminus = 0
            for j in range(0,self.columns):
                temp_Iminus += power(self.matrix[j][i],2)
            self.Iminus.append(sqrt(temp_Iminus))
    
    def Rank_i(self):
        for i in range(0,self.rows):
            R = self.Iminus[i]/(self.Iplus[i]+self.Iminus[i])
            self.rank.append(R)
    
    def print_solution(self):
        print(self.rank)

    def solve(self):
        self.normalization()
        self.weighted_normalized_matrix()
        self.I_plus()
        self.I_minus()
        self.Rank_i()
        self.print_solution()


matrix = [[30,40,25,27,45],[0,9,0,0,15],[2,1,3,5,2],[3,3,1,3,2],[3,2,3,3,3],[2,2,2,1,4]]

criteria_range = [[23,60],[0,15],[0,10],[1,3],[1,3],[1,5]]

reference_ideal = [[30,35],[10,15],[0,0],[3,3],[3,3],[4,5]]

wheights = [0.2262,0.2143,0.1786,0.1429,0.1190,0.1190]

decision = RIM(matrix,criteria_range,reference_ideal,wheights)

decision.solve()

