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

        # Create the graph with the input.
        graph = Graph(nb_graph)

        # Display the adjency matrix of the graph.
        graph.display_adjacency_matrix()

        # Display the value matrix of the graph.
        graph.display_value_matrix()

        # Detect if there is a loop in the graph.
        if not graph.detect_loop():
            # Display ranks
            graph.display_ranks()
        
        graph.check_scheduling_graph()

        graph.earliest_date()

        nb_graph = user_input()



# Main program
main()
