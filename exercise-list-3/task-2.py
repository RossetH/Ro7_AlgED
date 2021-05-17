from numpy import array, power, sqrt, zeros

class ELECTRE(object):
    """docstring for ELimination and Et Chouce Translating REality (ELECTRE)"""
    
    def __init__(self,matrix,weights, non_benefitial_att):
        self.matrix = matrix #array 2D
        self.weights = weights #array 1D
        self.alternatives = self.matrix.shape[0]
        self.criterias = self.matrix.shape[1] 
        self.nb_list = non_benefitial_att #list
        self.norm_matrix = zeros([self.alternatives,self.criterias])
        self.wn_matrix = zeros([self.alternatives,self.criterias])
        self.concordance_matrix = zeros([self.alternatives,self.alternatives])
        self.disconcordance_matrix = zeros([self.alternatives,self.alternatives])

    def matrix_normalize(self):
        #Evaluate the Eq.(11) denominator for each column
        #Eq.(11) indexes doesn't match with the expected
        #result given by Table 4
        norm_denominator = sqrt(power(self.matrix,2).sum(axis=0))    
        self.norm_matrix = self.matrix/norm_denominator
    
    def weighted_eval(self):
        self.wn_matrix = self.weights * self.norm_matrix

    def concordance_matrix_eval(self):
        for a in range(0,self.alternatives):
            for b in range(0,self.alternatives):
                if a==b:
                    continue
                for j in range(0,self.criterias):
                        if j in self.nb_list:
                            if self.wn_matrix[a][j] < self.wn_matrix[b][j]:
                                self.concordance_matrix[a][b] += self.weights[j]
                            elif self.wn_matrix[a][j] == self.wn_matrix[b][j]:
                                self.concordance_matrix[a][b] += self.weights[j]*0.5
                        else:
                            if self.wn_matrix[a][j] > self.wn_matrix[b][j]:
                                self.concordance_matrix[a][b] += self.weights[j]
                            elif self.wn_matrix[a][j] == self.wn_matrix[b][j]:
                                self.concordance_matrix[a][b] += self.weights[j]*0.5

    def disconcordance_matrix_eval(self):
        pass

    def solve(self):
        self.matrix_normalize()
        self.weighted_eval()
        self.concordance_matrix_eval()
        self.disconcordance_matrix_eval()

matrix = array([[60, 0.40, 2540, 500, 990],
    [6.35,0.15,1016,3000,1041],
    [6.8,0.10,1727.2,1500,1676],
    [10,0.20,1000,2000,965],
    [2.5,0.10,560,500,915],
    [4.5,0.08,1016,350,508],
    [3,0.10,1778,1000,920]])
# The quantitative data given in Table 1 isn't
# correct. The MPS criteria for the robot no. 7
# is 1778 instead of 177

weights = array([0.036,0.192,0.326,0.326,0.120])

# repeatability (column 2) 
# is a non-beneficial attribute
decision = ELECTRE(matrix,weights,non_benefitial_att=[1])

decision.solve()
