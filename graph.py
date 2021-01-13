import networkx as nx ## used for create graph, for more information : https://networkx.org/documentation/stable/tutorial.html
import matplotlib.pyplot as plt ## used for show the results, for more information :  https://matplotlib.org/tutorials/index.html

## used for create graph
def createGraph(node):
    G = nx.Graph() ## define the graph
    ## add the edges.
    ## wij = i + j, if | i - j | <= 3, and i and j are not equal.
    ## edges depends on number of node
    ## number of node = node
    for i in range(0, node) :
        for j in range(i, node) :
            if i % 2 == 0 : ## if node number is even
                if  i != j and max(i - j, j - i) <= 3 :
                    G.add_edge(i, j, weight = (i + j)) ## networkx feature,(TR) https://medium.com/cits-tech/python-networkx-ile-graf-teorisi-931699540e73
            else : ## if node number is odd
                if  i != j and max(i - j, j - i) <= 2 :
                    G.add_edge(i, j, weight=(i + j))

    ## edges depends on node number

    ## create nodes
    for i in range(node) :
        G.add_node(i, pos=(i, i))

    return G ## return the graph for use in main.

## used for draw graph
## source : https://stackoverflow.com/questions/35510095/coloring-specific-edges-in-networkx

def drawGraph(G,path):
    ## nodes are grey,used networkx property,for more information about edge properties : https://networkx.org/documentation/stable/tutorial.html#edges
    ## https://networkx.org/documentation/stable/tutorial.html

    for e in G.edges() :
        G[e[0]][e[1]]['color'] = 'grey'

    ## path will be red
    for i in range(len(path) - 1) :
        G[int(path[i])][int(path[i + 1])]['color'] = 'red'

    edge_color_list = [G[e[0]][e[1]]['color'] for e in G.edges()]
    nx.draw(G, node_color='gray', edge_color=edge_color_list, with_labels=True)
    plt.show()
