from graph import Graph

def main():
    cont    = True
    chosen  = False
    nb_max  = 13

    while(cont):
        text_in  = "Enter the number of your graph : "

        #Verify if the input is a number
        while(not chosen):
            nb_graph = input(text_in)

            try:
                nb_graph = int(nb_graph)
                chosen = True
            except ValueError:
                print("Please enter a correct number")
        nb_graph = min(nb_graph, nb_max)

        #Create the graph with the input
        graph = Graph(nb_graph)

        print(graph.adjacency_matrix[0])
        graph.display_adjacent()
        graph.display_value()
        graph.detect_loop()

        input("Press enter to continue...")

#Main program      
main()