import numpy as np
from numpy.core.records import array

class NearestNeighbour(object):
    """docstring for for the Travelling Salesman Problem (TSP) 
    solving algorithm based on the constructive heuristic proposed 
    by Bellmore & Nemhauser (1968) know as the nearest neighbour 
    algorithm"""
    
    def __init__(self,initial_node,cost_matrix):
        self.initial_node = initial_node
        self.cost_matrix = np.array(cost_matrix)
        self.n = self.cost_matrix.shape[0]
        self.path = []
        pass

    def minimum_non_zero_value(self,array):
        non_zero_array = np.nonzero(array)
        return np.min(array[non_zero_array])

    def get_position_of(self,array,value):
        return np.where(array == value)[0][0]     

    def solve(self):
        self.path.append(self.initial_node)
        while len(self.path) < self.n:
            node = self.path[len(self.path)-1]
            neighbours_distance = self.cost_matrix[node-1]
            nearest_neighbour = self.get_position_of(neighbours_distance,self.minimum_non_zero_value(neighbours_distance))
            self.cost_matrix[:,node-1].fill(0)
            self.path.append(nearest_neighbour+1)
        self.path.append(self.initial_node)

if __name__ == '__main__':

    cost_matrix = [[0,2,1,7,4],
                   [2,0,3,5,3],
                   [1,3,0,3,2],
                   [7,5,3,0,4],
                   [4,3,2,4,0]]
    
    initial_node = 1

    example = NearestNeighbour(initial_node=1,
                               cost_matrix = cost_matrix)

    example.solve()

    print(example.path)