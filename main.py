def load_graph(filename):
    g = []
    with open(filename, "r") as file:
        # "r" for read. "a" for append. "w" for write. "+" for if not exist then create the file.
        # example: "r" for read. "r+" for read and write. "a+" for append and create if not exist.
        # "w+" for write and create if not exist.
        nodes, lines = map(int, file.readline().split(" "))
        # initialize the graph according to the size and fill with 0.
        for i in range(nodes):
            row = []
            g.append(row)
            for j in range(nodes):
                row.append(0)

        # read in the graph
        for i in range(lines):
            r, c, l = map(int, file.readline().split(" "))
            g[r][c] = l
            g[c][r] = l
    return g


def get_neighbors(node, calculated_nodes, processed, graph):
    neighbors = []
    for i in range(len(graph)):
        if i not in processed and graph[node][i] != 0:  # i is a neighbour
            # calculated the neighbour distance
            distance = graph[node][i] + calculated_nodes[node]
            if i in calculated_nodes:
                if calculated_nodes[i] > distance:
                    calculated_nodes[i] = distance
            else:
                calculated_nodes[i] = distance
            # add the neighbour to the neighbour list
            neighbors.append(i)
    return neighbors


def get_nearest(nodes, calculated_nodes):
    node = None
    distance = 1000000
    for n in nodes:
        if calculated_nodes[n] < distance:
            node = n
            distance = calculated_nodes[n]
    return node, distance


def get_shortest_path(start, end, g):
    calculated_nodes = {start: 0}
    current = start
    tobe_processed = {start}
    processed = []
    
    while current != end or not tobe_processed:
        tobe_processed.remove(current)
        neighbors = get_neighbors(current, calculated_nodes, processed, g)
        tobe_processed.update(neighbors)
        node, distance = get_nearest(tobe_processed, calculated_nodes)
        processed.append(current)

        current = node

    return calculated_nodes[end]


graph = load_graph("graph.dat")

print(get_shortest_path(0, 9, graph))
