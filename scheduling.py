def one_entry_point(tmp_graph):
    x = 0
    entry_points = 0

    while(x < len(tmp_graph) and entry_points <= 1):
        for y in range(0, len(tmp_graph)):
            if(y < len(tmp_graph) and tmp_graph[y][x] != '-'):
                break; #If the curr column isn't empty
            elif(y == len(tmp_graph) - 1): #If the curr column is empty
                entry_points += 1
        x += 1
    
    if(entry_points != 1):
        return False
    return True

def one_exit_point(tmp_graph):
    x = 0
    exit_points = 0

    while(x < len(tmp_graph) and exit_points <= 1):
        for y in range(0, len(tmp_graph)):
            if(y < len(tmp_graph) and tmp_graph[x][y] != '-'):
                break; #If the curr line isn't empty
            elif(y == len(tmp_graph)-1): #If the curr line is empty
                print(tmp_graph[y])
        x += 1
    
    if(exit_points != 1):
        return False
    return True