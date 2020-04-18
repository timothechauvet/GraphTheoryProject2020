from graph import Graph

def main():
    cont    = True
    chosen  = False
    nb_max  = 13

    while(cont):

        while(not chosen):

            try:
                # Demands a number. int() throws an error if the input is not a number.
                nb_graph = int(input("Enter the number of your graph: "))
                # Chosen is set to True to break from the loop.
                chosen = True
            except ValueError:
                # A message is printed in case the input was not a number.
                print("Please enter a correct number")


        # We lock the number to the highest test file number, in our case 13.
        nb_graph = min(nb_graph, nb_max)

        # Create the graph with the input
        graph = Graph(nb_graph)

        print(graph.adjacency_matrix[0])
        graph.display_adjacency_matrix()
        graph.display_value_matrix()
        graph.detect_loop()

        input("Press enter to continue...")

# Main program
main()
