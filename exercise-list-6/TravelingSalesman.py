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
        self.path_costs = []
        self.total_cost = 0
        pass

    def minimum_non_zero_value(self,array):
        non_zero_array = np.nonzero(array)
        return np.min(array[non_zero_array])

    def get_position_of(self,array,value):
        return np.where(array == value)[0][0]     
    
    def get_nearest_neighbour(self, node):
        neighbours_distance = self.cost_matrix[node-1]
        nearest_neighbour = self.get_position_of(
            value = self.minimum_non_zero_value(neighbours_distance),
            array = neighbours_distance)
        return nearest_neighbour
    
    def get_path(self):
        self.path.append(self.initial_node)
        while len(self.path) < self.n:
            actual_node = self.path[len(self.path)-1]
            nearest_neighbour = self.get_nearest_neighbour(actual_node)
            self.cost_matrix[:,actual_node-1].fill(0)
            self.path.append(nearest_neighbour+1)
        self.path.append(self.initial_node)

    def get_total_distance(self):       
        for i in range(0,len(self.path)-1):
            self.path_costs.append(
                self.cost_matrix[self.path[i]-1,self.path[i+1]-1]
            )
        self.total_cost = np.array(self.path_costs).sum()
        pass     

    def solve(self):
        self.get_path()
        self.get_total_distance()
    
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
    print(f'The path is: {example.path}\n',
        f'With a total cost of {example.total_cost}')  

