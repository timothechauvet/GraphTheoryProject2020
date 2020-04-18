from graph import Graph

def user_input():
    chosen  = False
    nb_max  = 13
    while(not chosen):
        try:
            # Demands a number. int() throws an error if the input is not a number.
            nb_graph = int(input("Enter the number of your graph (0 to quit): "))
            if nb_graph > -1:
                # Chosen is set to True to break from the loop.
                chosen = True
            else:
                print("Please enter a positive number")
        except ValueError:
            # A message is printed in case the input was not a number.
            print("Please enter a number")

    # We lock the number to the highest test file number, in our case 13.
    return min(nb_graph, nb_max)

def main():
    nb_graph = user_input()

    while nb_graph:

        # Create the graph with the input
        graph = Graph(nb_graph)

        print(graph.adjacency_matrix[0])
        graph.display_adjacency_matrix()
        graph.display_value_matrix()
        graph.detect_loop()

        nb_graph = user_input()


# Main program
main()
