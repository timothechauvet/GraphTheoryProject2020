import csv

class Graph:
    adjacency_matrix: list

    def __init__(self, nb_graph):
        filename = f'{nb_graph}.csv'
        self.adjacency_matrix = []

        #Read the file and store values to a 2D table named array2D
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                self.adjacency_matrix.append(row)