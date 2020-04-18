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

    
    #Display the adjacent matrix
    def display_adjacent(self):
        print("\n- ADJACENT MATRIX -\n\n")
        for y in range(0, len(self.adjacency_matrix)):
            for x in range(0, len(self.adjacency_matrix)):
                if self.adjacency_matrix[y][x] != '-':
                    print('1 ', end='')
                else:
                    print('0 ', end='')
            print('\n', end='')

    #Display the value matrix
    def display_value(self):
        print("\n- VALUE MATRIX -\n\n")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in self.adjacency_matrix]))

    def detect_loop(self):
        #Copy the adjacency matrix
        tmp_graph = self.adjacency_matrix.copy()
        x = 0
        
        '''
        Main loop, get the minimal "width" of the graph.
        It will first go through the width of the graph,
        then go through the height to find if one column
        has 0 adjacent node.
        '''
        while(x < len(tmp_graph)): #Width
            empty = True
            for y in range(0, len(tmp_graph)): #Height
                if(tmp_graph[y][x] != '-'):
                    empty = False
            
            #If the column is empty, remove it from the whole table
            if empty:
                #Remove the column
                for y in range(0, len(tmp_graph)): #Height
                    del tmp_graph[y][x]
                #Remove the line
                print(tmp_graph[x])
                del tmp_graph[x]

                x = -1 #Go back to the beggining
            x += 1 #Increment the width

        #Detect cycle
        if len(tmp_graph) == 0:
            print("THERE IS NO CYCLE")
        else:
            print("THERE IS A CYCLE")