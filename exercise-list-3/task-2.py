from numpy import array, power, sqrt, zeros, absolute, empty_like, argsort, arange

class ELECTRE(object):
    """docstring for ELimination and Et Chouce Translating REality (ELECTRE)"""
    
    def __init__(self,matrix,weights, non_benefitial_att):
        self.matrix = matrix #array 2D
        self.weights = weights #array 1D
        self.alternatives = self.matrix.shape[0]
        self.criterias = self.matrix.shape[1] 
        self.nb_list = non_benefitial_att #list
        self.norm_matrix = empty_like(matrix)
        self.wn_matrix = empty_like(matrix)
        self.concordance_matrix = zeros([self.alternatives,self.alternatives])
        self.discordance_matrix = empty_like(self.concordance_matrix)
        self.pure_concordance_index = zeros([self.alternatives,1])
        self.pure_discordance_index = zeros([self.alternatives,1])
        self.pure_concordance_index_rank = zeros([self.alternatives,1])
        self.pure_discordance_index_rank = zeros([self.alternatives,1])
        self.index_rank = zeros([self.alternatives,1])

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

    def discordance_matrix_eval(self):
        for a in range(0,self.alternatives):
            for b in range(0,self.alternatives):
                tmp_max = zeros([1,self.criterias])
                tmp_abs = zeros([1,self.criterias])                
                if a==b:
                    continue
                for j in range(0,self.criterias):
                    tmp_abs[0][j] = self.wn_matrix[b][j]-self.wn_matrix[a][j]
                for j in range(0,self.criterias):
                    if self.wn_matrix[b][j] > self.wn_matrix[a][j]:
                        tmp_max[0][j] = self.wn_matrix[b][j]-self.wn_matrix[a][j]
                self.discordance_matrix[a][b] = tmp_max.max()/(absolute(tmp_abs).max())

    def pure_concordance_index_eval(self):
        self.pure_concordance_index = self.concordance_matrix.sum(axis=1)-self.concordance_matrix.sum(axis=0)

    def pure_discordance_index_eval(self):
        self.pure_discordance_index = self.discordance_matrix.sum(axis=1)-self.discordance_matrix.sum(axis=0)          

    def rank(self):
        tmp = -self.pure_concordance_index.argsort()
        self.pure_concordance_index_rank = empty_like(tmp)
        self.pure_concordance_index_rank[tmp] = arange(len(self.pure_concordance_index_rank))
        tmp = self.pure_discordance_index.argsort()
        self.pure_discordance_index_rank = empty_like(tmp)
        self.pure_discordance_index_rank[tmp] = arange(len(self.pure_discordance_index_rank))
        self.index_rank = (self.pure_concordance_index_rank + self.pure_concordance_index_rank)/2
        tmp = self.index_rank
        self.index_rank[tmp] = arange(len(self.pure_discordance_index_rank))

    def solve(self):
        self.matrix_normalize()
        self.weighted_eval()
        self.concordance_matrix_eval()
        self.discordance_matrix_eval()
        self.pure_concordance_index_eval()
        self.pure_discordance_index_eval()
        self.rank()

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

print(decision.index_rank)