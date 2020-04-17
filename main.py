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

        graph = Graph(nb_graph)
        