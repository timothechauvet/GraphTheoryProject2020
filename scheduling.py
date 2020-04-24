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
                exit_points += 1
        x += 1
    
    if(exit_points != 1):
        return False
    return True

def same_weight_vertex(tmp_graph):
    x = 0
    curr = -1
    scheduling = True

    while(x < len(tmp_graph) and scheduling):
        for y in range(0, len(tmp_graph)):
            #Initialize curr when the first weight is crossed
            if(curr == -1 and tmp_graph[x][y] != '-'):
                curr = tmp_graph[x][y]
            #If the current weight isn't the same as the current
            elif(tmp_graph[x][y] not in {'-', curr}):
                scheduling = False
                break
        x += 1
        curr = -1
    
    return scheduling

def zero_entry(tmp_graph):
    entry = []
    x     = 0
    
    #Get all entry points
    while(x < len(tmp_graph)): #Width
        empty = True
        for y in range(0, len(tmp_graph)): #Height
            if(tmp_graph[y][x] != '-'):
                empty = False
                break

        #if the column is empty that means this is an entry point
        if empty:
            entry.append(x)
        x += 1
    
    #If one entry has a weight different than 0 or null, it returns false
    for i in entry:
        for x in range(0, len(tmp_graph)):
            if tmp_graph[i][x] not in {'0', '-'}:
                return False

    return True