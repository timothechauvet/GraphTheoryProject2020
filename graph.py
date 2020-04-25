import csv
import copy
from scheduling import *

class Graph:
    adjacency_matrix: list

    def __init__(self, nb_graph):
        filename = f'{nb_graph}.csv'
        self.adjacency_matrix = []
        print("\n---File reading---")

        #Read the file and store values to a 2D table named array2D
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                print(row)
                self.adjacency_matrix.append(row)

    
    #Display the adjacent matrix
    def display_adjacency_matrix(self):
        print("\n- ADJACENT MATRIX -\n\n")
        for y in range(0, len(self.adjacency_matrix)):
            for x in range(0, len(self.adjacency_matrix)):
                if self.adjacency_matrix[y][x] != '-':
                    print('1 ', end='')
                else:
                    print('0 ', end='')
            print('\n', end='')

    #Display the value matrix
    def display_value_matrix(self):
        print("\n- VALUE MATRIX -\n\n")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in self.adjacency_matrix]))

    def detect_loop(self):
        #Copy the adjacency matrix
        tmp_graph = copy.deepcopy(self.adjacency_matrix)
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
                    break
            
            #If the column is empty, remove the edge from the table
            if empty:
                tmp_graph = delete_vertex(tmp_graph, x)
                x = -1 #Go back to the beggining

            x += 1 #Increment the width

        #Detect cycle
        if len(tmp_graph) == 0:
            print("THERE IS NO CYCLE")
            return False
        else:
            print("THERE IS A CYCLE")
            return True

    def display_ranks(self):
        ranks = calculate_ranks(copy.deepcopy(self.adjacency_matrix))
        for rank, vertices in enumerate(ranks):
            print("The vertices of rank " + str(rank) + " are: " + str(vertices))
        
    def check_scheduling_graph(self):
        entry_pt = one_entry_point(self.adjacency_matrix)
        exit_pt  = one_exit_point(self.adjacency_matrix)
        cycle    = self.detect_loop()
        weight   = same_weight_vertex(self.adjacency_matrix)
        zero_etr = zero_entry(self.adjacency_matrix)
        negative = no_negative_arc(self.adjacency_matrix)

        print("ENTRY PT IS ", entry_pt, " EXIT PT IS ", exit_pt, " CYCLE IS ", cycle, " WEIGHT ", weight, " ZERO IS ", zero_etr, " NEG ", negative)
        return (entry_pt and exit_pt and not cycle and weight and zero_etr and negative)


    def find_predecessors(self):
        #predecessor per task instead of per rank?
        #initialisation
        predecessors = []
        for x in range(0,len(self.adjacency_matrix)):#for weight of graph, 2d empty list of list
            p_list = []
            predecessors.append(p_list)
        print("p", predecessors)
        #add each predecessor to corresponding task 
        for row in range(0,len(self.adjacency_matrix)):
            for column in range( 0,len(self.adjacency_matrix)):
                if self.adjacency_matrix[row][column] != '-':
                    predecessors[column].append(row)
        return predecessors

    def dates(self):
        print("----EARLIEST DATE----")
        ranked_task = calculate_ranks_no_display(copy.deepcopy(self.adjacency_matrix))
        predecessors = self.find_predecessors()
       
        #ranked predecessor
        ranked_predecessors = []
        for x in range(0,len(ranked_task)):
            ranked_predecessors.append([])

        for x in range(0,len(ranked_task)):
            for r in ranked_task[x]:
                ranked_predecessors[x].append(predecessors[r])            
      
        #task time
        task_time = self.calculate_time(ranked_task)

        tsk = 0
        t0 = 0
        path = [ranked_task[0][0]]
        for r in range(1,len(ranked_task)-1):#for rank 1...n
            tmp = []
            for x in range(0,len(ranked_predecessors[r])):  #index of each task in each rank
                #if predecessor is tsk, added in tmp
                if tsk in ranked_predecessors[r][x]: 
                    tmp.append(x)

            time = []
            for x in tmp:
                time.append(task_time[r][x]) #time of each task

            if tmp:
                mt = max(time)
                my =task_time [r].index(mt)
                tsk = ranked_task[r][my]
                t1 = mt + t0
                t0 = copy.deepcopy(t1)
                path.append(tsk)
        path.append(ranked_task[len(ranked_task)-1][0])
        print("The earliest date is",t1, "with the path ",path)


        print("----LATEST DATE----")
        #set tsk as last task
        tsk = ranked_task[len(ranked_task)-1][0]
        t0 = t1
        
        for r in range(len(ranked_task)-1,-1,-1): #r = max rank to 0
            time = []
            tmp = []
            #find predecessors of tsk
            dx = ranked_task.index([tsk])
            pred = ranked_predecessors[dx][0]
            for x in range(0,len(ranked_task[r])):
                for y in pred:
                    if y == ranked_task[r][x]:
                        tmp.append(x)
            
            #find time of predecessors of tsk
            if tmp:
                for x in tmp:
                    time.append(task_time[r][x])
                #choose min time
                mint = min(time)

                #find whose task has min
                x = time.index(mint)
                print(time[x])

                #min = new tsk



        #find wich task has this time


                #in predecessors of tsk
                
#            if tmp:
#                mt = min(time)
#                my =task_time [r].index(mt)
#                tsk = ranked_task[r][my]
#                t1 = mt - t0
#                t0 = copy.deepcopy(t1)
                #print(tsk,"pour",mt)

        print("The latest date is",t1)

    
    def calculate_time(self,tmp_graph):
        time_rp = copy.deepcopy(tmp_graph)
        for row in range(0,len(self.adjacency_matrix)):
            for column in range( 0,len(self.adjacency_matrix)):
                if self.adjacency_matrix[row][column] != '-':
                    v = int(self.adjacency_matrix[row][column] )
                    for x in range(0,len(tmp_graph)):
                        for y in tmp_graph[x]:
                            if y == row:
                                time_rp[x][tmp_graph[x].index(y)] = v
        return time_rp
        
      



def delete_vertex(tmp_graph, nb_vertice, shift = 0):
    # Remove the column
    for y in range(0, len(tmp_graph)): # Height
        del tmp_graph[y][nb_vertice]

    # Remove the line
    print("removing vertice " + str(nb_vertice+shift) + ": " + str(tmp_graph[nb_vertice]))
    del tmp_graph[nb_vertice]
    return tmp_graph

# Returns a list of ranks with each containing a list of vertices.
def calculate_ranks(tmp_graph):
    rank = 0
    ranks = []

    while sum([len(x) for x in ranks]) != len(tmp_graph):
        print("tmp_graph len: " + str(len(tmp_graph)) + "\nsum ranks: " + str(sum([len(x) for x in ranks])))
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                         for row in tmp_graph]))

        ranks.append([])
        x = 0
        # We are searching for every sources and putting them into the current rank
        while(x < len(tmp_graph)): # Width
            crossed = True
            for y in range(0, len(tmp_graph)): # Height
                if(tmp_graph[y][x] != 'x'):
                    crossed = False
            
            if not crossed:
                empty = True
                for y in range(0, len(tmp_graph)): # Height
                    if(tmp_graph[y][x] != '-' and tmp_graph[y][x] != 'x'):
                        empty = False
            
            # If the column is empty, it is a source, so we add it to the current rank
            if not crossed and empty:
                print("inserting " + str(x) + " into ranks of rank " + str(rank))
                ranks[rank].append(x)

            x += 1 # Checking the next vertex

        # Now we have the sources for the current iteration
        # We delete them from the adjacency matrix
        for i in ranks[rank]:
            for y in range(0, len(tmp_graph)): # Height
                tmp_graph[y][i] = 'x'

            tmp_graph[i] = ['x' for i in range(len(tmp_graph))]

        # The current iteration is finished, we do the next iteration
        rank += 1
    
    return ranks

def calculate_ranks_no_display(tmp_graph):
    rank = 0
    ranks = []

    while sum([len(x) for x in ranks]) != len(tmp_graph):

        ranks.append([])
        x = 0
        # We are searching for every sources and putting them into the current rank
        while(x < len(tmp_graph)): # Width
            crossed = True
            for y in range(0, len(tmp_graph)): # Height
                if(tmp_graph[y][x] != 'x'):
                    crossed = False
            
            if not crossed:
                empty = True
                for y in range(0, len(tmp_graph)): # Height
                    if(tmp_graph[y][x] != '-' and tmp_graph[y][x] != 'x'):
                        empty = False
            
            # If the column is empty, it is a source, so we add it to the current rank
            if not crossed and empty:
                ranks[rank].append(x)

            x += 1 # Checking the next vertex

        # Now we have the sources for the current iteration
        # We delete them from the adjacency matrix
        for i in ranks[rank]:
            for y in range(0, len(tmp_graph)): # Height
                tmp_graph[y][i] = 'x'

            tmp_graph[i] = ['x' for i in range(len(tmp_graph))]

        # The current iteration is finished, we do the next iteration
        rank += 1
    
    return ranks



