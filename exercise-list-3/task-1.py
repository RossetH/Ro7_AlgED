from numpy import amin, absolute
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
        # criar teste para avaliar ordem dos vetores está correta
        # e avaliar se há mesmo numero de ranges que colunas (critérios)
    def d_min(self,x,j):
        return amin([absolute(x-self.reference_ideal[j][0]),
                        absolute(x-self.reference_ideal[j][1])])
    def normalize_f(self,x,j):
        if x in range(reference_ideal[j][0],reference_ideal[j][1]):
            return 1
        elif x in range(criteria_range[j][0],reference_ideal[j][0]):
            return 1 - d_min(x)/absolute(criteria_range[j][0]-reference_ideal[j][0])
        elif x in range(reference_ideal[j][1],criteria_range[j][1]):
            return 1 - d_min(x)/absolute(reference_ideal[j][1]-criteria_range[j][1])
        else:
            print('Reference Ideal isn\'t contained in the range [A,B]')
            quit() 
    def normalization(self):
        for j in range(0,self.columns):
            for i in range(0,self.rows):
                return normalize_f(self.matrix[j][i],j)
                pass
            pass
    def weighted_normalized_matrix(self):
        pass

matrix = [[30,40,25,27,45],[0,9,0,0,15],[2,1,3,5,2],[3,3,1,3,2],[3,2,3,3,3],[2,2,2,1,4]]

criteria_range = [[23,60],[0,15],[0,10],[1,3],[2,3],[1,3]]

reference_ideal = [[30,35],[10,maxsize],[0,0],[3,3],[1,1],[4,5]]

wheights = [0.2262,0.2143,0.1786,0.1429,0.1190,0.1190]

test = RIM(matrix,criteria_range,reference_ideal,wheights)


