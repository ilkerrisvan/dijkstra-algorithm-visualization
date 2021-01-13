import heapq
from graph import createGraph ## used for test
from math import inf

""" 
## used for test
node = 10
graph = createGraph(node)
"""

## about the algorithm : https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
## used min-heap
def dijkstra(graph, source, dest): ## we need to know graph,source node and destination node for find the shortest path
    heap = [] ## heap
    visited = {} ## visited nodes
    cost = {}
    shortest_distance = {}
    path = [] ## shortest path
    before = {} ## parent node

    ## initialize,shortes
    for node in range(len(graph)):
        shortest_distance[node] = inf ## all values will be inf
        cost[node] = None
        visited[node] = False ## there is no visited node
        before[node] = None ## so there is no parent node too

    heapq.heappush(heap,(source)) ## used heap for get min value easily
    cost[source] = 0 ## source -> source = 0

    while len(heap) != 0:
        current = heapq.heappop(heap) ## min will current and use it
        visited[current] = True ## so we visit "current" node
        if current == dest: ## if current is destination so it's mean path is okey. source -> destination
            path = [dest]
            while path[-1] != source : ## dest -> soruce for get the path so this path is shortest path
                path.append(before[path[-1]])
            path.reverse()
            break
        else: ## if current is not the destionation need to check nodes
            for neighbor in dict(graph.adjacency()).get(current) : ## all neighbors must be checked
                if not visited[neighbor] : ## don't go visited node again and again,max one visit
                    cost[neighbor] = cost[current] + graph.get_edge_data(current, neighbor).get('weight') ##update the cost of neighbor
                    if cost[neighbor] < shortest_distance[neighbor]: ## if neigbors cost smaller use this node
                        shortest_distance[neighbor] = cost[neighbor]
                        before[neighbor] = current
                        heapq.heappush(heap,(neighbor))

    total_cost_of_path = 0
    for i in range(0,len(path)-1):
       total_cost_of_path += graph.get_edge_data(path[i], path[i+1]).get('weight')

    ## print(total_cost_of_path)
    ## print("p",path)

    return path,total_cost_of_path


